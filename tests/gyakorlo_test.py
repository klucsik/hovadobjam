from app.gyakorlo import *


def test_keres_elso_leghoszabb_szo_1():
    assert keres_elso_leghoszabb_szo("szépséges leg hosz abb szó") == "szépséges"

def test_keres_elso_leghoszabb_szo_2():
    assert keres_elso_leghoszabb_szo("aaaa bbb c ddd eeee") == "aaaa"

def test_keres_utolso_leghoszabb_szo():
    assert keres_utolso_leghoszabb_szo("aaaa bbb c ddd eeee") == "eeee"