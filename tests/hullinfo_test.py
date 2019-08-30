from app.hullinfo import *
import time

def test_create_hullinfo_without_id():
    assert create_hullinfo_version('test_create_0').hull_id == get_hullinfo_by_name('test_create_0').hull_id

def test_create_hullinfo():
    assert create_hullinfo_version('test_create_1', 43, 0).hull_id == 43


def test_create_hullinfo_update():
    last_version = create_hullinfo_version('test_create_2', 42, 0).version
    new_version = create_hullinfo_version('test_create_2', 42, 0).version
    assert last_version + 1 == new_version

def test_get_hullinfo_by_hull_id():
    create_hullinfo_version('test_for_get_hullinfo', 666)
    row = get_hullinfo_versionated_by_hull_id(666)
    assert row.name == 'test_for_get_hullinfo'

def test_get_hullinfo_by_name():
    create_hullinfo_version('test_for_get_hullinfo_1', 333)
    assert get_hullinfo_by_name("test_for_get_hullinfo_1").hull_id == 333

def test_create_hullinfo_hull_id_creation():
    first_id = create_hullinfo_version('test_for_hull_id_increment ' + str(time.time())).hull_id
    second_id = create_hullinfo_version('test_for_hull_id_increment ' + str(time.time())).hull_id
    assert first_id + 1 == second_id


def test_update_hullinfo():
    update_hullinfo(name='test_1', hull_id=1, version=0, description='test update hullinfo')
    update_hullinfo(name='test_1', hull_id=1, version=2, description='test update hullinfo')

def test_update_hullinfo_2():
    create_hullinfo_version(name='test_1', hull_id=1, version=0, description='test update hullinfo')
