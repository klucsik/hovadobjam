from app.hullinfo import *


def test_create_hullinfo():
    assert create_hullinfo('test_create_1', 43, 0)[0]['hull_id'] == 43


def test_create_hullinfo_update():
    last_version = create_hullinfo('test_create_1', 42, 0)[0]['version']
    new_version = create_hullinfo('test_create_1', 42, 0)[0]['version']
    assert last_version +1 == new_version

def test_get_hullinfo_by_hull_id():
    create_hullinfo('test_for_get_hullinfo', 666)
    assert get_hullinfo_by_hull_id(666)[0]['name'] == 'test_for_get_hullinfo'

def test_get_hullinfo_by_name():
    create_hullinfo('test_for_get_hullinfo_1', 333)
    assert get_hullinfo_by_name("test_for_get_hullinfo_1")[0]['hull_id'] == 333

def test_create_hullinfo_hull_id_creation():
    first_id = create_hullinfo('test_for_hull_id_increment')[0]['hull_id']
    second_id = create_hullinfo('test_for_hull_id_increment')[0]['hull_id']
    assert first_id+1 == second_id