import pytest
from player import Player,HumanPlayer
from match import Match

xavier = None
otto = None

def setup():
    global xavier
    xavier = Player("prof. Xavier")
    global otto
    otto = Player("Dr Octopus")
    

def teardown():
    global xavier
    xavier = None 
    global otto
    otto = None

def test_different_players_have_different_chars():
    t = Match(xavier, otto)
    assert xavier.caracter != otto.caracter

def test_no_player_with_none_char():
    t = Match(xavier, otto)
    assert xavier.caracter != None
    assert otto.caracter != None

def test_next_player_is_round_robbin():
    t = Match(otto, xavier)
    p1 = t.next_player
    p2 = t.next_player
    assert p1 != p2

def test_players_are_opponents():
    t = Match(otto, xavier)
    x = t.get_player("x")
    o = t.get_player("o")

    assert o.opponent == x
    assert x.opponent == o