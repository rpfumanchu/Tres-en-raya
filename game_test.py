import pytest
from square_board import SquareBoard
from game import Game


def test_creation():
    g = Game()

    assert g != None

def test_is_game_over():
    game = Game()
    win_x = SquareBoard.fromList([['x', 'o', None, None, ],
                                  ['o', 'x', None, None, ],
                                  ['x', 'o', 'x', 'o', ],
                                  ['x', 'o', None, None, ],
                                  ])

    win_o = SquareBoard.fromList([['x', 'o', 'x', 'o', ],
                                  ['x', 'x', 'o', None, ],
                                  ['o', 'o', None, None, ],
                                  ['o', 'x', None, None, ]])

    tie = SquareBoard.fromList([['o', 'x', 'x', 'o', ],
                                ['x', 'o', 'o', 'x', ],
                                ['o', 'x', 'x', 'o', ],
                                ['x', 'o', 'o', 'x', ]])

    unfinished = SquareBoard.fromList([['o', 'x', 'x', 'o', ],
                                       [None, None, None, None, ],
                                       [None, None, None, None, ],
                                       [None, None, None, None, ]])

    game.board = win_x
    assert game._is_game_over() == True

    game.board = win_o
    assert game._is_game_over() == True

    game.board = tie
    assert game._is_game_over() == True

    game.board = unfinished
    assert game._is_game_over() == False
    
