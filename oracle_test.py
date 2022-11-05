from oracle import *
from square_board import SquareBoard
from settings import BOARD_LENGTH

def test_base_oracle():
    board = SquareBoard.fromList([[None, None, None, None],
                                  ['x', 'o', 'x', 'o'],
                                  ['o', 'o', 'x', 'x'],
                                  ['o', None, None, None ]])
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
    assert cr == ColumnRecommendation(2, ColumnClassification.MAYBE)  # equivalentes
    # no equivalentes (puesto qu eno tienen la misma clasificación)
    assert cr != ColumnRecommendation(2, ColumnClassification.FULL)
    assert cr != ColumnRecommendation(3, ColumnClassification.FULL)

def test_hash():
    a = 1
    b = 2 - 1
    assert a == b
