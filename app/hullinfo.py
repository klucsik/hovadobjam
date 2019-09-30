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
def create_hullinfo(name):
    """
    hullinfó bejegyzés létrehozása
    https://docs.sqlalchemy.org/en/13/orm/tutorial.html#adding-and-updating-objects
    """
    new_hullinfo_row = HullInfo(name=name)
    logging.info(f"inserted hullnifo row: {new_hullinfo_row}")
    db.session.add(new_hullinfo_row)
    db.session.flush()
    db.session.commit()
    hull_id = new_hullinfo_row.hull_id
    app.alias.make_alias(name, hull_id)
    return new_hullinfo_row


def get_hullinfo_by_hull_id(hull_id):
    """
    hullinfó bejegyzés lekérdezése ID alapján
    https://docs.sqlalchemy.org/en/13/orm/tutorial.html#querying
    """
    result_row = HullInfo.query.filter_by(hull_id=hull_id).first()
    return result_row


def get_hullinfo_by_name(name,  version=-1):
    """
    hullinfó bejegyzés lekérdezése név alapján
    """
    search = "%{}%".format(name)
    result_row = HullInfo.query.filter_by(HullInfo.name.like(search)).first()

    return result_row

import app.alias # azért van itt lent mert az aliassal ezek körkörösen hívják egymást és megmekken enélkül




