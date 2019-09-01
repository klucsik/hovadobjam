from app.hova_dobjam_kimutatas import *

def test_get_hova_dobta():
   logging.debug(get_hova_dobta(1))

def test_make_hova_dobta():
    make_hova_dobta(hull_id=42, user_id=1, kuka_id=1)


def test_get_kuka_list():
   logging.debug(get_kuka_count_list(42))

def test_get_kuka_count_dict():
    thingie = get_kuka_count_dict(42)
    logging.debug(thingie)


