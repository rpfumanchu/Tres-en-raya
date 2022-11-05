from oracle import BaseOracle, ColumnClassification

class Player():
    def __init__(self, nombre, caracter=None, oracle = BaseOracle()):
        self.nombre = nombre
        self.caracter = caracter
        self.oracle = oracle



    def play(self, board):
        """
        elije la mejor columna de aquellas que recomienda el oraculo
        """
        #obten las recomendaciones
        recommendations = self.oracle.get_recommendation(board, self)
        #selecciona la mejor de todas
        best = self.choose(recommendations)
        #juega con ella
        board.add(self.caracter, best.indice)


    def choose(self, recommendations):
        #quitamos las no validas 
        #usmos filter para La filter()función extrae elementos de un iterable (lista, tupla, etc.) para los cuales una función devuelve True.
        valid = list(filter(lambda x : x.classification != ColumnClassification.FULL, recommendations))
        #pillamos la primera de las válidas
        return valid[0]