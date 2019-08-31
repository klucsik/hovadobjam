from app import *
from app.models import *
from sqlalchemy import *


# HullInfoVersionated bejegyzés:
# id - az sor azonosítására
# hull_id - melyik hulladék
# version - hogy tudjuk a változtatásokat követni
# name 150 karakteres string
# kép - kövi sprint
# description (500 szabad karakter)
# helyettesítő - kövi sprint


# ezt fogja meghívni a post metódus, validáció majd mezőbe szúrás
def create_hullinfo_version(name, hull_id=-1, version=0, description=""):
    """
    hullinfó bejegyzés létrehozása
    https://docs.sqlalchemy.org/en/13/orm/tutorial.html#adding-and-updating-objects
    """

    if hull_id is -1:
        perhaps_id = app.alias.get_hull_id_by_alias(name)
        if perhaps_id > 0:
            hull_id = perhaps_id
        else:
            # SELECT hull_id FROM HullInfoVersionated ORDER BY hull_id DESC LIMIT 1
            result = HullInfoVersionated.query.order_by(HullInfoVersionated.hull_id.desc()).first()
            last_hull_id = result.hull_id
            hull_id = last_hull_id+1

    try:
        # SELECT hull_id,version FROM HullInfoVersionated WHERE hull_id = " + str(hull_id) + " ORDER BY version DESC LIMIT 1
        result = HullInfoVersionated.query.filter_by(hull_id=hull_id).order_by(HullInfoVersionated.version.desc()).first()
        last_version = result.version
        version = last_version + 1
    except:
        logging.debug("creating new row")
    else:
        logging.debug(f" updating row: {result}")

    new_hullinfo_row = HullInfoVersionated(hull_id=hull_id, version=version, name=name, description=description)
    logging.info(f"inserted hullnifo row: {new_hullinfo_row}")  # TODO ezt szépen ki kell írni egyenként
    db.session.add(new_hullinfo_row)
    app.alias.make_alias(name, hull_id)
    db.session.flush()
    db.session.commit()

    update_hullinfo(name=name, hull_id=hull_id, version=version, description=description)

    return get_hullinfo_versionated_by_hull_id(hull_id, version)


def update_hullinfo(name, hull_id, version, description):
   hullinfo = HullInfo(hull_id=hull_id, version=version, name=name, description=description)
   db.session.merge(hullinfo)
   db.session.commit()
   return hullinfo


def get_hullinfo_versionated_by_hull_id(hull_id, version=-1):
    """
    hullinfó bejegyzés lekérdezése ID alapján a legfrissebb verziót
    https://docs.sqlalchemy.org/en/13/orm/tutorial.html#querying
    https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_core_selecting_rows.htm

    Az adatok a következő módon érhetőek el a váalszból: response[0]['name'] szintaktikával ( a response változik ugye)
    """
    if version == -1:
        result_row = HullInfoVersionated.query.filter_by(hull_id=hull_id).order_by(HullInfoVersionated.version.desc()).first()
    else:
        result_row = HullInfoVersionated.query.filter_by(hull_id=hull_id).filter_by(version=version).first()

    return result_row


def get_hullinfo_by_name(name,  version=-1):
    """
    hullinfó bejegyzés lekérdezése név alapján a legfrissebb verziót
    https://docs.sqlalchemy.org/en/13/orm/tutorial.html#querying
    https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_core_selecting_rows.htm
    """
    search = "%{}%".format(name)
    if version == -1:
        result_row = HullInfoVersionated.query.filter(HullInfoVersionated.name.like(search)).order_by(HullInfoVersionated.version.desc()).first()
    else:

        result_row = HullInfoVersionated.query.filter_by(HullInfoVersionated.name.like(search)).filter_by(version=version).first()

    return result_row


def get_hullinfo_by_hull_id(hull_id):
    result_row = HullInfoVersionated.query.filter_by(hull_id=hull_id).first()
    return result_row


import app.alias # azért van itt lent mert az aliassal ezek körkörösen hívják egymást és megmekken enélkül




