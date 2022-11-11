from oracle import *
from square_board import SquareBoard
from settings import BOARD_LENGTH
from player import Player, ReportingPlayer


def test_base_oracle():
    board = SquareBoard.fromList([[None, None, None, None],
                                  ['x', 'o', 'x', 'o'],
                                  ['o', 'o', 'x', 'x'],
                                  ['o', None, None, None]])
    expected = [ColumnRecommendation(0, ColumnClassification.MAYBE),
                ColumnRecommendation(1, ColumnClassification.FULL),
                ColumnRecommendation(2, ColumnClassification.FULL),
                ColumnRecommendation(3, ColumnClassification.MAYBE)]
    rappel = BaseOracle()
    assert len(rappel.get_recommendation(board, None)) == len(expected)
    assert rappel.get_recommendation(board, None) == expected


def test_equality():
    cr = ColumnRecommendation(2, ColumnClassification.MAYBE)

    assert cr == cr  # son idénticos
    assert cr == ColumnRecommendation(
        2, ColumnClassification.MAYBE)  # equivalentes

    # no equivalentes (puesto qu eno tienen la misma clasificación)
    assert cr != ColumnRecommendation(2, ColumnClassification.FULL)
    assert cr != ColumnRecommendation(3, ColumnClassification.FULL)


def test_hash():
    a = 1
    b = 2 - 1
    assert a == b


def test_is_winning_move():
    winner = Player("xavier", "x")
    loser = Player("otto", "o")

    empty = SquareBoard()
    almost = SquareBoard.fromList([['o', 'x', 'o', None],
                                   ['o', 'x', 'o', None],                          
                                   ['x', None, None, None],
                                   [None, None, None, None]])
    oracle = SmartOracle()

    #sobre tablero vacio
    for i in range(0, BOARD_LENGTH):
        assert oracle._is_winning_move(empty, i, winner) == False
        assert oracle._is_winning_move(empty, i, loser) == False

    #sobre el tablero de verdad
    for i in range(0, BOARD_LENGTH):
        assert oracle._is_winning_move(almost, i, loser) == False

    assert oracle._is_winning_move(almost, 2, winner)

def test_no_good_options():
    x = Player('xavier', caracter='x')
    o = Player('Otto', caracter='o', opponent=x)
    oracle = SmartOracle()
    maybe = SquareBoard.fromBoardRawCode('....|o...|....|....')
    bad_and_full = SquareBoard.fromBoardRawCode('x...|oo..|o...|xoxo')
    all_bad = SquareBoard.fromBoardRawCode('x...|oo..|o...|....')
    assert oracle.no_good_options(maybe, x) == False
    assert oracle.no_good_options(bad_and_full, x)
    assert oracle.no_good_options(all_bad, x)