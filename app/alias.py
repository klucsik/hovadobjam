from app.hullinfo import *


def get_hull_id_by_alias(alias):
    """
    vissza adja a hull_id-t alias alapján
    """
    try:
        t = text("SELECT * FROM alias WHERE name like '%" + alias + "%' ")
        logging.debug('get hull_Id by alias query:' + str(t))
        result = db.session.execute(t)
        result = resultproxy_to_rowproxy(result)
        result_id = resultproxy_to_rowproxy(result)[0]['hull_id']
    except Exception as e:
        logging.error('error:' + str(e))
        result_id = -1
    logging.debug('get_hull_id_by_alias hull_id:' + str(result_id))
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
    if get_hull_id_by_alias(alias) > 0:
       logging.info("alias is already made")
    else:
        new_alias_row = aliasTable(hull_id=hull_id, name=alias)
        db.session.add(new_alias_row)
        db.session.flush()
        db.session.commit()
    return get_hull_id_by_alias(alias)


def get_aliases_from_hull_id(hull_id):

        t = text("SELECT name FROM alias WHERE hull_id = " + str(hull_id))
        logging.debug('get_aliases_from_hull_id query:' + str(t))
        result = db.session.execute(t)
        result = resultproxy_to_rowproxy(result)
        result_alias= []
        for row in result:
            result_alias.append(row['name'])
            logging.debug(result_alias)
        logging.debug(result_alias)
        return result_alias



