from app.hullinfo import *


def test_create_hullinfo():
    assert create_hullinfo('test_create_1', 42, 0).hull_id == 42