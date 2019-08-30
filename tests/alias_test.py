from app.alias import *

def test_make_alias():
    assert make_alias('krumpli', 1) == 1
    assert make_alias('burgonya', 1) == 1

def test_get_hull_id_by_alias():
    assert get_hull_id_by_alias('rumpl') == 1

#TODO gethullinfo_by_aliasból csinálni szép tesztesetet, fixtrueal, teardownal együtt vagy nemtom lehet azmár nem unit és apin keresztül kéne de legyen emg itt is

def test_get_aliases_from_hull_id():
   # assert get_aliases_from_hull_id(1)  ['krumpli', 'burgonya', 'rumpl']
    assert get_aliases_from_hull_id(-1) == []

def test_get_hullinfo_by_hull_id():
    create_hullinfo_version('test_for_get_hullinfo_aliased', 17)
    make_alias('test_alias', 17)
    assert get_hullinfo_by_alias('test_alias').name == 'test_for_get_hullinfo_aliased'