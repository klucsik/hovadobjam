from app import app, db
from app.models import *
# hullinfo bejegyzés:
# id - az sor azonosítására
# hull_id - melyik hulladék
# version - hogy tudjuk a változtatásokat követni
# name 150 karakteres string
# kép - kövi sprint
# description (500 szabad karakter)
# helyettesítő - kövi sprint


# ezt fogja meghívni a post metódus, validáció majd mezőbe szúrás
def create_hullinfo(name, hull_id=0,  version=0, description=""):
    """
    hullinfó bejegyzés létrehozása
    https://docs.sqlalchemy.org/en/13/orm/tutorial.html#adding-and-updating-objects
    """
    #validation goes here: nem lehet ugyanolyan hull_id-vel adatot feltenni, mert az put és verziószámot kell növelni
    if hull_id is not 0:
        new_hullinfo_row = hullinfo(hull_id=hull_id, version=version, name=name, description=description)
    else:
        new_hullinfo_row = hullinfo(version=version, name=name, description=description)
        #generálni kell hull_id-t

    db.session.add(new_hullinfo_row)
    db.session.flush()
    db.session.commit()
    db.session.refresh(new_hullinfo_row)
    return new_hullinfo_row




