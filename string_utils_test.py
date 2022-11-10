
from string_utils import *
# el opuesto de collapse


def test_explode_string():
    assert explode_string("Han") == ["H", "a", "n"]
    assert explode_string("") == []


def test_explode_list_of_strings():

    assert explode_list_of_strings(["Han", "Solo"]) == [
        ["H", "a", "n"], ["S", "o", "l", "o"]]
    assert explode_list_of_strings(["", "", ""]) == [[], [], []]
    assert explode_list_of_strings([]) == []


def test_replace_all_list():
    assert replace_all_in_list([None, 3, "546", 33, None], None, "#") == [
        "#", 3, "546", 33, "#"]
    assert replace_all_in_list([1, 2, 3, 4, 5], "e", 42) == [1, 2, 3, 4, 5]
    assert replace_all_in_list([], 34, 43) == []


def test_replace_all_in_matrix():
    # caso normal tiene lo viejo
    assert replace_all_in_matrix([[1, 2, 3, "n", "n", None],
                                  [4, 5, "n"]], "n", "#") == [[1, 2, 3, "#", "#", None], [4, 5, "#"]]
    # caso raro: no tiene lo viejo
    assert replace_all_in_matrix([[None, None, 2, True], 
                                  [4, 5, "#"]], "k", 42) == [[None, None, 2, True], [4, 5, "#"]]
    # caso mas raro:lista de listas vacias
    assert replace_all_in_matrix([], None, 7) == []
    assert replace_all_in_matrix([[], []], None, 7) == [[], []]
