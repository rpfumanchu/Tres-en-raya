from linear_board import *
from settings import BOARD_LENGTH
from list_utils import transpose,displace_matriz,reverse_matriz

class SquareBoard():
    """
    representa un tablero cuadrado
    """
    #los metodos de clase estan vinculados a una clase en lugar de a un objeto, pueden ser llamados tanto por clase como por objeto
    @classmethod
    def fromList(cls, lista_de_listas):
        """
        transforma una lists de listas en una lista de , llevan el parametro cls
        """
        board = cls()
        #map devuelve un map object por eso tenemos que trasformarlo a una lista usando list()
        board.columna = list(map(lambda elemento : LinearBoard.fromList(elemento), lista_de_listas))
        return board


    def __init__(self):
        self.columna = [LinearBoard() for i in range(BOARD_LENGTH)]

    def is_full(self):
        """
        True si todos los LinearBoard estan llenos
        """
        resultado = True
        for lb in self.columna:
            resultado = resultado and lb.is_full()
        return resultado

    def una_matriz(self):
        """
        devuelve una representacion en formato matriz, es decir, lista de listas
        """
        return list(map(lambda x: x.columna, self.columna))

    #detectar victoria
    def is_victory(self, caracter):
        return self.victoria_vertical(caracter) or self.victoria_horizontal(caracter) or self.victoria_diago_up(caracter) or self.victoria_diago_down(caracter)

    def victoria_vertical(self, caracter):
        resultado = False
        for lb in self.columna:
            resultado = resultado or lb.is_victory(caracter)
        return resultado

    def victoria_horizontal(self, caracter):
        #trasponemos columnas, usamos una_matriz que hemos creado por que si no nos da error al no ser una matriz
        transp =transpose(self.una_matriz())
        #creamos un tablero temporal con esa matriz traspuesta
        tmp = SquareBoard.fromList(transp)
        #comprobamos si tiene una victoria temporal
        return tmp.victoria_vertical(caracter)

    def victoria_diago_up(self, caracter):
        #obtenemos las columnas como una matriz
        m = self.una_matriz()
        #luego las invertimos
        revm = reverse_matriz(m)
        #creamos tablero temporal con esa matriz
        tmp = SquareBoard.fromList(revm)
        #devolvemos si hay una victoria descendente
        return tmp.victoria_diago_down(caracter)

    def victoria_diago_down(self, caracter):
        #obtenemos las columnas como una matriz
        m = self.una_matriz()
        #las desplazamos
        d = displace_matriz(m)
        #creamos un tablero temporal con esa matriz
        tmp = SquareBoard.fromList(d)
        #averiguamos si tiene una victoria tmp
        return tmp.victoria_horizontal(caracter)

    #dunders
    #devuelve una cadena de testo que representa el objeto, te permite ver las tripas del objeto
    def __repr__(self):
        return f"{self.__class__}:{self.columna}"
    
    
