from enum import Enum, auto


class ColumnClassification(Enum):
    FULL = auto()
    MAYBE = auto()

class ColumnRecommendation():
    def __init__(self, indice, classification):
        self.indice = indice
        self.classification = classification

    def __eq__(self, other):
    #si son de clases distintas, pues son distintos
        if not isinstance(other, self.__class__):
            return False
    #si son de la misma clase, pues comparo las propiedades de uno y otro
        else:
        #aqui hacemos una tupla para no tener que ir caso a caso
            return (self.indice, self.classification) == (other.indice, other.classification)
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