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



def get_hova_dobta(hull_id):
    hovadobtalist = UserHovaDobta.query.filter_by(hull_id=hull_id).all()
    return hovadobtalist

def get_kuka_id_by_name(name):
    id = Kuka.query.filter_by(name=name).first().id
    return id

def get_kuka_name_by_id(id):
    name = Kuka.query.filter_by(id=id).first().name
    return name

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
    kuka_list = get_kuka_list()

    for kuka in kuka_list:
        if kuka.id not in kuka_count_list[0]:
            kuka_count_list[0].append(kuka.id)
            kuka_count_list[1].append('')
            kuka_count_list[2].append(0)

    for o in range(len(kuka_count_list[0])):
        kuka_count_list[1][o] = get_kuka_name_by_id(kuka_count_list[0][o])

    kuka_count_list_ordered = []
    for p in range(len(kuka_count_list[0])):
        kuka_count_list_ordered.append([kuka_count_list[0][p], kuka_count_list[1][p], kuka_count_list[2][p]])
    kuka_count_list_ordered.sort(key=lambda x: x[2], reverse=True)

    return kuka_count_list_ordered





def get_kuka_count_dict(hull_id):
    hovadobtalist = get_hova_dobta(hull_id)
    logging.debug(get_hova_dobta(1))
    kuka_count_dict = {}
    kuka_list = get_kuka_list()
    for kuka in kuka_list:
        kuka_count_dict[kuka.name] = 0
        for sor in hovadobtalist:
            if sor.kuka_id == kuka.id:
                kuka_count_dict[kuka.name] = kuka_count_dict.get(kuka.name) + 1
    return kuka_count_dict

