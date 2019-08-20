from app import app, db
from app.models import *
from sqlalchemy import text
from app.hullinfo import *

def get_hull_id_by_alias(alias):
    """
    vissza adja a hull_id-t alias alapján
    """
    t = text("SELECT * FROM alias WHERE name like '%" + alias + "%' ")
    result = db.session.execute(t)
    result_id = resultproxy_to_rowproxy(result)[0]['hull_id']
    return result_id

def get_hullinfo_by_alias(alias):
    """
    vissza adja a hullinfo-t alias alapján
    """
    t = text("SELECT * FROM alias WHERE name like '%" + alias + "%' ")
    result = db.session.execute(t)
    result_id = resultproxy_to_rowproxy(result)[0]['hull_id']
    return get_hullinfo_by_hull_id(result_id)

def make_alias(alias, hull_id):
    """
    vissza adja a hullinfo-t alias alapján
    """
    try:
        get_hull_id_by_alias(alias)
    except:
        print("it's already made")
    else:
        t = text("INSERT INTO alias (name, hull_id) VALUES ('" + alias + "'," + str(hull_id) + ") ")
        db.session.execute(t)
    return get_hull_id_by_alias(alias)

def test_make_alias():
    assert make_alias('krumpli', 1) == 1