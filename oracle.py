from enum import Enum, auto
from copy import deepcopy
from settings import BOARD_LENGTH
from square_board import SquareBoard


class ColumnClassification(Enum):
    FULL = -1      #imposible
    LOSE = 1       #derrota inminente
    BAD = 5        #muy indeseable
    MAYBE = 10     #indeseable
    WIN = 100      #la mejor opcion: gano por narices

class ColumnRecommendation():
    def __init__(self, indice, classification):
        self.indice = indice
        self.classification = classification

    def __eq__(self, other):
    #si son de clases distintas, pues son distintos
        if not isinstance(other, self.__class__):
            return False
    #solo importa la clasificacion
        else:
        #aqui hacemos una tupla para no tener que ir caso a caso
            return self.classification == other.classification
        #dos objetos equivalentes tienen que temer el mismo hash
    def __hash__(self):
        return hash((self.indice, self.classification))
            
   
class BaseOracle():
    def get_recommendation(self, board, player):
        """
        retirnamos una lista de columnRecommendation
        """
        recommendations = []
        for i in range(len(board)):
            recommendations.append(self.get_column_recommendation(board, i, player))
        return recommendations

    def get_column_recommendation(self, board, indice, player):
        """
        clasifica una columna ya sea como full o maybe y devuelve una columnRecommendation
        """
        classification = ColumnClassification.MAYBE
        if board.columna[indice].is_full():
            classification = ColumnClassification.FULL
        return ColumnRecommendation(indice, classification)

    def no_good_options(self, board, player):
        """
        Detecta que todas las clasificaciones sean BAD o FULL
        """
        # obtener las clasificaciuones
        columnRecommendations = self.get_recommendation(board, player)
        # comprobamos que todas sean del tipo correcto
        result = True
        for rec in columnRecommendations:
            if (rec.classification == ColumnClassification.WIN) or (rec.classification == ColumnClassification.MAYBE):
                result = False
                break
        return result

    #para que todos los oraculos sean iguales y ni de error vamos a implementar los metodos backtrack y update_to_bad
    #  le ponemos un pass para que no haga nada, ya que solo queremos que realmente los use LearningOracle

    def update_to_bad(self, move):
        pass

    def backtrack(self, list_of_moves):
        pass

class SmartOracle(BaseOracle):
    def get_column_recommendation(self, board, indice, player):
        """
        afina la clasificación de super e intenta encontrar columnas WIN
        """
        # llamamos a super
        recommendation = super().get_column_recommendation(board, indice, player)
        if recommendation.classification == ColumnClassification.MAYBE:
            #se puede mejorar
            if self._is_winning_move(board, indice, player):
                recommendation.classification = ColumnClassification.WIN
            elif self._is_losing_move(board, indice, player):
                recommendation.classification = ColumnClassification.LOSE
        return recommendation

    def _is_losing_move(self, board, indice, player):
        """
        si player juega en índice, ¿genera una jugada vencedora para el oponente en alguna de las demas columnas?
        """
        tmp = self._play_on_tmp_board(board, indice, player)
        will_lose = False
        for i in range(0, BOARD_LENGTH):
            if self._is_winning_move(tmp, i, player.opponent):
                will_lose = True
        return will_lose

    def _is_winning_move(self, board, indice, player):
        """
        Determina si al jugar en una posición, nos llevaría a ganar de inmediato
        """
        # hago una copia del tablero
        # juego en ella
        tmp = self._play_on_tmp_board(board, indice, player)
        # determino si hay una victoria para player o no
        return tmp.is_victory(player.caracter)
    def _play_on_tmp_board(self, board, indice, player):
        """
        Crea una copia del board y juega en él
        """
        tmp = deepcopy(board)
        tmp.add(player.caracter, indice)
        # devuelvo la copia alterada
        return tmp
        
class MemoizingOracle(SmartOracle):
    """
    el método get_recommendation esta ahora memorizado
    """
    def __init__(self):
        super().__init__()
        self._past_recommendations = {}
    def _make_key(self, board_code, player):
        """
        la clave debe de combinar el board y el player, de la forma más sencilla posible
        """
        return f"{board_code.raw_code} @ {player.caracter}"

    def get_recommendation(self, board, player):
        #creamos la clave
        key = self._make_key(board.as_code(), player)
        
        #miramos en el cache: si no esta calculo y guardo en el cache
        if key not in self._past_recommendations:
            self._past_recommendations[key] = super().get_recommendation(board, player)

        #devuelvo lo que esta en el cache
        return self._past_recommendations[key]

class LearningOracle(MemoizingOracle):
    def update_to_bad(self, move):
        # crear clave
        key = self._make_key(move.board_code, move.player)
        # obtener la clasificación erronea
        recommendation = self.get_recommendation(
            SquareBoard.fromBoardCode(move.board_code), move.player)
        # corregirla
        recommendation[move.position] = ColumnRecommendation(
            move.position, ColumnClassification.BAD)
        # sustituirla
        self._past_recommendations[key] = recommendation


    def backtrack(self, list_of_moves):
        """
        Repasa todos las jugadas y si encuentra una en la cual todo 
        estaba perdido, quiere decir que la anterior tiene que ser 
        actualizada a BAD
        """
        # los moves están en orden inverso (el primero será el último)
        print('Aprendiendo...')
        # por cada move...
        for move in list_of_moves:
            # lo reclasifico a bad
            self.update_to_bad(move)
            # evaluo si todo estaba perdido tras esta clasificación
            board = SquareBoard.fromBoardCode(move.board_code)
            if not self.no_good_options(board, move.player):
                # si no todo estaba perdido, salgo. Sino, sigo
                break


        print(f'en la base de mi conocimiento: {len(self._past_recommendations)}')


