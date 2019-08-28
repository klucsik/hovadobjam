from app import *
from app.models import *
from sqlalchemy import *


# hullinfo bejegyzés:
# id - az sor azonosítására
# hull_id - melyik hulladék
# version - hogy tudjuk a változtatásokat követni
# name 150 karakteres string
# kép - kövi sprint
# description (500 szabad karakter)
# helyettesítő - kövi sprint


# ezt fogja meghívni a post metódus, validáció majd mezőbe szúrás
def create_hullinfo(name, hull_id=-1,  version=0, description=""):
    """
    hullinfó bejegyzés létrehozása
    https://docs.sqlalchemy.org/en/13/orm/tutorial.html#adding-and-updating-objects
    """



    if hull_id is -1:
        perhaps_id = app.alias.get_hull_id_by_alias(name)
        if perhaps_id > 0:
            hull_id = perhaps_id
        else:
            t = text("SELECT hull_id FROM hullinfo ORDER BY hull_id DESC LIMIT 1")
            result = db.session.execute(t)
            last_hull_id = int(resultproxy_to_rowproxy(result)[0]['hull_id'])
            hull_id = last_hull_id+1

    try:
        t = text("SELECT hull_id,version FROM hullinfo WHERE hull_id = " + str(hull_id) + " ORDER BY version DESC LIMIT 1")
        result = db.session.execute(t)
        unproxiedresult = resultproxy_to_rowproxy(result)
        last_version = int(unproxiedresult[0]['version'])
        version = last_version + 1
    except:
        logging.debug("creating new row")
    else:
        logging.debug(f" updating row: {unproxiedresult}")

    new_hullinfo_row = hullinfo(hull_id=hull_id, version=version, name=name, description=description)
    logging.info(f"inserted hullnifo row: {new_hullinfo_row}") # TODO ezt szépen ki kell írni egyenként
    db.session.add(new_hullinfo_row)
    app.alias.make_alias(name, hull_id)
    db.session.flush()
    db.session.commit()


    return get_hullinfo_by_hull_id(hull_id, version)


def get_hullinfo_by_hull_id(hull_id,  version=-1):
    """
    hullinfó bejegyzés lekérdezése ID alapján a legfrissebb verziót
    https://docs.sqlalchemy.org/en/13/orm/tutorial.html#querying
    https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_core_selecting_rows.htm

    Az adatok a következő módon érhetőek el a váalszból: response[0]['name'] szintaktikával ( a response változik ugye)
    """
    if version == -1:
        t = text("SELECT * FROM hullinfo WHERE hull_id = " + str(hull_id) + " ORDER BY version DESC LIMIT 1")
        result = db.session.execute(t)
        result_row = resultproxy_to_rowproxy(result)
    else:
        t = text("SELECT * FROM hullinfo WHERE hull_id = " + str(hull_id) + " and version = "+ str(version) +" LIMIT 1")
        result = db.session.execute(t)
        result_row = resultproxy_to_rowproxy(result)

    return result_row


def get_hullinfo_by_name(name,  version=-1):
    """
    hullinfó bejegyzés lekérdezése név alapján a legfrissebb verziót
    https://docs.sqlalchemy.org/en/13/orm/tutorial.html#querying
    https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_core_selecting_rows.htm
    """
    if version == -1:
        t = text("SELECT * FROM hullinfo WHERE name like '%" + name + "%' ORDER BY version DESC LIMIT 1")
        result = db.session.execute(t)
        result_row = resultproxy_to_rowproxy(result)
    else:
        t = text("SELECT * FROM hullinfo WHERE name like '%" + name + "%' and version = " + str(version) +" LIMIT 1")
        result = db.session.execute(t)
        result_row = resultproxy_to_rowproxy(result)

    return result_row


def resultproxy_to_rowproxy(resultproxy):
    d, a = {}, []
    for rowproxy in resultproxy:
        # rowproxy.items() returns an array like [(key0, value0), (key1, value1)]
        for column, value in rowproxy.items():
            # build up the dictionary
            d = {**d, **{column: value}}
        a.append(d)
        # print('proxytlanítottva: ')
        # print(a)
    return a


import app.alias # azért van itt lent mert az aliassal ezek körkörösen hívják egymást és megmekken enélkül




