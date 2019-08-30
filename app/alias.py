from app.hullinfo import *


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
        logging.debug(result)
        logging.error(' get_hull_id_by_alias error: ' + str(e))
        result_id = -1
    logging.debug('get_hull_id_by_alias hull_id: ' + str(result_id))
    return result_id



def get_hullinfo_by_alias(alias):
    """
    vissza adja a HullInfo-t alias alapján
    """
    # "SELECT * FROM alias WHERE name like '%" + alias + "%' ")
    search = "%{}%".format(alias)
    result = AliasTable.query.filter(AliasTable.name.like(search)).first()
    result_id = result.hull_id
    return get_hullinfo_versionated_by_hull_id(result_id)


def make_alias(alias, hull_id):
    """
    vissza adja a HullInfoVersionated-t alias alapján
    """
    if get_hull_id_by_alias(alias) > 0:
       logging.info("alias is already made")
    else:
        new_alias_row = AliasTable(hull_id=hull_id, name=alias)
        db.session.add(new_alias_row)
        db.session.flush()
        db.session.commit()
    return get_hull_id_by_alias(alias)


def get_aliases_from_hull_id(hull_id):
    # "SELECT name FROM alias WHERE hull_id = " + str(hull_id))
    result = AliasTable.query.filter_by(hull_id=hull_id).order_by(AliasTable.name.asc()).all()
    result_alias = []
    for row in result:
        result_alias.append(row.name)
        logging.debug(result_alias)
        logging.debug(result_alias)
    return result_alias



