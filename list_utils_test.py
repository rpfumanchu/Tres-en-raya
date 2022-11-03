import pytest
from list_utils import *

def test_find_one():
    aguja = 1
    none = [0, 0, 5, 's']
    comienzo = [1, None, 9, 6, 0, 0]
    extremo = ['x', '0', 1]
    varios = [0, 0, 3, 4, 1, 3, 2, 1, 3, 4]

    assert find_one(none, aguja) == False
    assert find_one(comienzo, aguja)
    assert find_one(extremo, aguja)
    assert find_one(varios, aguja)