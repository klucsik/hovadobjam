
from app.models import AliasTable, HullInfo
import logging
from app import db


def hullinfo_full_todict(hull_id):
    hull_row = get_hullinfo_by_hull_id(hull_id)
    alias_list = get_aliases_from_hull_id(hull_id)
    data = {
        'hull_id': hull_row.hull_id,
        'name': hull_row.name,
        'picurl': hull_row.picurl,
        'alias_list': alias_list
    }
    return data



def get_hull_id_by_alias(alias):
    """
    vissza adja a hull_id-t alias alapján
    """
    try:
        # "SELECT * FROM alias WHERE name like '%" + alias + "%' ")
        search = "%{}%".format(alias)
        result = AliasTable.query.filter(AliasTable.name.like(search)).first()
        result_id = result.hull_id
    except Exception as e:
        logging.error(' get_hull_id_by_alias error: ' + str(e))
        result_id = -1
    logging.debug('get_hull_id_by_alias hull_id: ' + str(result_id))
    return result_id


def get_hull_id_list_by_alias(alias):
    result_list = []
    try:
        search = "%{}%".format(alias)
        result = AliasTable.query.filter(AliasTable.name.like(search)).all()
        logging.debug(f'get_hull_id_list_by_alias nyers találatok: {result}')

        for sor in result:
            logging.debug(f'get_hull_id_list_by_alias nyers találat: {sor}')
            if sor.hull_id not in result_list:
                result_list.append(sor.hull_id)
    except Exception as e:
        logging.error(' get_hull_id_list_by_alias error: ' + str(e))
    return result_list


def get_hullinfo_by_alias(alias):
    """
    vissza adja a HullInfo-t alias alapján
    """
    # "SELECT * FROM alias WHERE name like '%" + alias + "%' ")
    search = "%{}%".format(alias)
    result = AliasTable.query.filter(AliasTable.name.like(search)).first()
    result_id = result.hull_id
    return get_hullinfo_by_hull_id(result_id)


def get_hullinfo_list_by_alias(alias):
    id_list = get_hull_id_list_by_alias(alias)
    result = []
    for id in id_list:
        result.append(get_hullinfo_by_hull_id(id))
    return result


def get_alias_row(hull_id, alias):
     result=AliasTable.query.filter_by(hull_id=hull_id, name=alias).first()
     return result


def make_alias(alias, hull_id):
    isitalready = get_alias_row(hull_id, alias)
    if isitalready:
        logging.info("alias is already made")
        new_alias_row = isitalready
    else:
        new_alias_row = AliasTable(hull_id=hull_id, name=alias)
        db.session.add(new_alias_row)
        db.session.flush()
        db.session.commit()
    return new_alias_row.hull_id


def get_aliases_from_hull_id(hull_id):
    result = AliasTable.query.filter_by(hull_id=hull_id).order_by(AliasTable.name.asc()).all()
    result_alias = []
    for row in result:
        result_alias.append(row.name)
        logging.debug(result_alias)
        logging.debug(result_alias)
    return result_alias



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
    make_alias(name, hull_id)
    return new_hullinfo_row


def get_hullinfo_by_hull_id(hull_id):
    """
    hullinfó bejegyzés lekérdezése ID alapján
    https://docs.sqlalchemy.org/en/13/orm/tutorial.html#querying
    """
    result_row = HullInfo.query.filter_by(hull_id=hull_id).first()
    return result_row


def get_hullinfo_by_name(name):
    """
    hullinfó bejegyzés lekérdezése név alapján
    """
    search = "%{}%".format(name)
    result_row = HullInfo.query.filter_by(HullInfo.name.like(search)).first()

    return result_row
