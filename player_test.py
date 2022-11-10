from square_board import SquareBoard
from oracle import BaseOracle
from player import ReportingPlayer, is_non_full_column, is_within_column_range,is_int
         
         #ESTE TEST LO COMENTO POR QUE YA NO HACE FALTA AL HABER CORREGIDO QUE NO JUEGUE SIEMPRE EN LA PRIMERA POSICION DISPONIBLE Y HACER QUE SEA ALEATORIO

# def test_play():
#     """
#     comprobar que se juega en la primera columna disponible
#     """

#     before = SquareBoard.fromList([[None, None, None, None],
#                                    ['x', 'o', 'x', 'o'],
#                                    ['x', 'o', 'x', 'o'],
#                                   ['x', None, None, None]])

#     after = SquareBoard.fromList([['x', None, None, None],
#                                    ['x', 'o', 'x', 'o'],
#                                    ['x', 'o', 'x', 'o'],
#                                   ['x', None, None, None]])

#     player = Player('Chip', 'x', oracle = BaseOracle())

#     player.play(before)
#     assert before == after

def test_is_within_column_range():
    board = SquareBoard.fromList([['x', None, None, None, ],
                                  ['x', 'o', 'x', 'o', ],
                                  ['o', 'o', 'x', 'x', ],
                                  ['o', None, None, None, ]])
    assert is_within_column_range(board, 0)
    assert is_within_column_range(board, 1)
    assert is_within_column_range(board, 2)
    assert is_within_column_range(board, 3)
    assert is_within_column_range(board, 5) == False
    assert is_within_column_range(board, -10) == False
    assert is_within_column_range(board, 10) == False

def test_is_non_full_column():
    board = SquareBoard.fromList([['x', None, None, None, ],
                                  ['x', 'o', 'x', 'o', ],
                                  ['o', 'o', 'x', 'x', ],
                                  ['o', None, None, None, ]])
                                  
    assert is_non_full_column(board,0) 
    assert is_non_full_column(board, 1) == False
    assert is_non_full_column(board,2) == False
    assert is_non_full_column(board, 3) 


def test_is_int():
    assert is_int('42')
    assert is_int('0')
    assert is_int('-32')
    assert is_int('  32   ')
    assert is_int('hola') == False
    assert is_int('') == False
    assert is_int('3.14') == False

