from app import *
from app.models import *
import logging

def make_hova_dobta(user_id, hull_id, kuka_id):
    new_row = UserHovaDobta(hull_id=hull_id, user_id=user_id, kuka_id=kuka_id)
    logging.info(f"inserted hullnifo row: {new_row}")  # TODO ezt szépen ki kell írni egyenként
    db.session.add(new_row)
    db.session.flush()
    db.session.commit()
    return new_row.id

def test_make_hova_dobta():
    make_hova_dobta(hull_id=42, user_id=1, kuka_id=1)

def get_hova_dobta(hull_id):
    hovadobtalist = UserHovaDobta.query.filter_by(hull_id=hull_id).all()
    return hovadobtalist

def test_get_hova_dobta():
   logging.debug(get_hova_dobta(1))

def get_kuka_list():
   kuka_list = Kuka.query.all()
   return kuka_list

def get_kuka_count_list(hull_id):
    # https://snakify.org/en/lessons/two_dimensional_lists_arrays/
    hovadobtalist = get_hova_dobta(hull_id)
    logging.debug(get_hova_dobta(1))
    kuka_count_list = [[], [], []]
    for sor in hovadobtalist:

        if sor.kuka_id not in kuka_count_list[0]:
            kuka_count_list[0].append(sor.kuka_id)
            kuka_count_list[1].append('')
            kuka_count_list[2].append(1)
        else:
            for i in range(len(kuka_count_list[0])):
                if kuka_count_list[0][i] == sor.kuka_id:
                    kuka_count_list[2][i] = kuka_count_list[2][i]+1
    # TODO: az összes kukát adja át
    kuka_list = get_kuka_list()

    for kuka in kuka_list:
        if kuka.id not in kuka_count_list[0]:
            kuka_count_list[0].append(kuka.id)
            kuka_count_list[1].append('')
            kuka_count_list[2].append(0)

    return kuka_count_list



def test_get_kuka_list():
   logging.debug(get_kuka_count_list(42))

def get_kuka_count_list_readable(hull_id):
    kuka_count_list = get_kuka_count_list(hull_id)

    for i in range(len(kuka_count_list[0])):
        kuka_count_list[1][i] = Kuka.query.filter_by(id=kuka_count_list[0][i]).first().name
    logging.debug(kuka_count_list)
    return kuka_count_list

def test_get_kuka_readable():
    thingie = get_kuka_count_list_readable(42)
    logging.debug(thingie)
    assert  thingie[1][0]== 'műanyag'
