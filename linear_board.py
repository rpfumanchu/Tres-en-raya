from settings import BOARD_LENGTH, VICTORY_STRIKE
from list_utils import find_streak

class LinearBoard():
    """
    clase que representa un tablero de una sola columna
    x un jugador
    o otro jugador
    None un espacio vacio
    """
    # aqui también usaremos @classmethod fromList porque si no no estaria definido en square_board
    @classmethod
    def fromList(cls, list):
        board = cls()
        board.columna = list
        return board

    def __init__(self):
        """
        una lista de nada None
        """
        self.columna = [None for i in range(BOARD_LENGTH)]

    def add(self, caracter):
        """
        esto hara que juegue en la primera posion disponible
        """
        #siempre que no este lleno..
        if not self.is_full():
            #tengo que buscar la primera posicion libre None
            i = self.columna.index(None)
            #lo sustituimos por un caracter
            self.columna[i] = caracter
        

    def is_full(self):
        return self.columna[-1] != None
        

    def is_victory(self, caracter):
        return find_streak(self.columna, caracter, VICTORY_STRIKE)

    def is_tie(self, caracter1, caracter2):
        """
        esto es que no hay victoria ni de caracter1 ni de caracter2
        """
        return (self.is_victory("x") == False and self.is_victory("o") == False)