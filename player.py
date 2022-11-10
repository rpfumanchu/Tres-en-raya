from list_utils import all_same
from oracle import BaseOracle, ColumnClassification,ColumnRecommendation,SmartOracle
import random
from beautifultable import BeautifulTable
from settings import BOARD_LENGTH
from move import Move

class ReportingPlayer():
    def __init__(self, nombre, caracter=None, opponent = None, oracle = SmartOracle()):
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
        self._play_on(board, best.indice, recommendations)

    def on_win(self):
        pass

    def on_lose(self):
        pass

    def _play_on(self, board, position, recommendations):
        #juega en la posicion
        board.add(self.caracter, position)
        #guardo mi ultima jugada
        self.last_move = Move(position, board.as_code(), recommendations, self)

    #para mostrar las recomendacione al usar help
    def display_recommendations(self, board):
        #mapeamos las clasificaciones, se devuelve una lista, el 1 es el rango de la fila osea una de la lista de clasificaciones
        recs = map(lambda x: str(x.classification).split('.')[1].lower(), self.oracle.get_recommendation(board, self))

        bt = BeautifulTable()
        bt.rows.append(recs)

        bt.columns.header = [str(i) for i in range(BOARD_LENGTH)]
        print(bt)

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
        #ordenamos por el valor de la clasificación
        valid = sorted(valid, key=lambda x : x.classification.value, reverse=True)
        #sin son todas iguales pillo una al azar
        if all_same(valid):
            return random.choice(valid) 
        else:
            #si no lo son oillo la mas deseable que sera la primera porque para eso las hemos ordenado
            return valid[0]
        

class HumanPlayer(ReportingPlayer):
    
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
            elif raw == "h":
                print(f"ASI ANDAS!!!!  {self.display_recommendations(board)}")

class ReportingPlayer(ReportingPlayer):
    def on_lose(self):
        """
        avisa al oraculo que su ultima recomendacion ha sido mala
        """
        board_code = self.last_move.board_code
        position = self.last_move.position
        self._oracle.update_to_bad(board_code, self, position)

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