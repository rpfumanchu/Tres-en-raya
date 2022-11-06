from oracle import BaseOracle, ColumnClassification,ColumnRecommendation
import random

class Player():
    def __init__(self, nombre, caracter=None, opponent = None, oracle = BaseOracle()):
        self.nombre = nombre
        self.caracter = caracter
        self.oracle = oracle
        self.opponent = opponent
        self.last_move = None

    @property
    def opponent(self):
        return self._opponent

    @opponent.setter
    def opponent(self, other):
        if other != None:
            self._opponent = other
            other._opponent = self


    def play(self, board):
        """
        elije la mejor columna de aquellas que recomienda el oraculo
        """
       #pregunto al oraculo
       #esto es una tupla,una forma sencilla de empaquetar dos o más valores sin tener que crear una clase
        (best, recommendations) = self._ask_oracle(board)

       #juego en la mejor
        self._play_on(board, best.indice)

    def _play_on(self, board, position):
        #juega en la posicion
        board.add(self.caracter, position)
        #guardo mi ultima jugada
        self.last_move = position

    def _ask_oracle(self, board):
        """
        pregunta al oraculo y devuelve la mejor opción
        """
        #obtenemos las recomendaciones y seleccionamos la mejor
        recommendations = self.oracle.get_recommendation(board, self)
        best = self.choose(recommendations)
        return (best, recommendations)


    def choose(self, recommendations):
        #quitamos las no validas 
        #usmos filter para La filter()función extrae elementos de un iterable (lista, tupla, etc.) para los cuales una función devuelve True.
        valid = list(filter(lambda x : x.classification != ColumnClassification.FULL, recommendations))
        #seleccionamos entre las iguales una al azar con random.choice y una secuencia()
        return random.choice(valid)

class HumanPlayer(Player):
    
    def __init__(self, nombre, caracter=None):
        super().__init__(nombre, caracter)

    def _ask_oracle(self, board):
        #le pido al humano que es mi oraculo
        while True:
            #pedimos columna al 
            raw = input("selecciona una columna, humano o h para HELP!!!   ")
            #verificamos que su respuesta no sea una idiotez
            if is_int(raw) and is_within_column_range(board, int(raw)) and is_non_full_column(board, int(raw)):
                #si no lo es, jugamos donde ha dicho y salimos del bucle
                pos = int(raw)
                return (ColumnRecommendation(pos, None), None)


#funciones de validación de indice de columna

def is_non_full_column(board, num):
    return not board.columna[num].is_full()

#esta dentro del rango de columnas
def is_within_column_range(board, num):
    return num >= 0 and num < len(board)

#comprobar que es un enteroes un entero
def is_int(aString):
    try:
        num = int(aString)
        return True
    except:
        return False