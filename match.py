
class Match():

    def __init__(self, player1, player2):
        player1.caracter = "x"
        player2.caracter = "o"
        player1.opponent = player2

        # los guardamos dentro de un diccionario para poder luego recuperarlos
        self._players = {"x" : player1, "o":player2}
        # los guardamos en una lista normal y corriente por que son solo dos jugadores y asi al invertirla el ultimo sera el primero y etc etc
        # este nonbre le pone por hacer referencia a una lista circular
        self._round_robbin = [player1, player2]
        assert (player1.opponent is not None) and (player2.opponent is not None), "Players are required to have an opponent for recommendations"

    # queremos sintaxis de propiedad para esto :puede ser usado para modificar un método para que sea un atributo o propiedad
    @property
    def next_player(self):
        next = self._round_robbin[0]
        # usaremos el metodo reverse(), para invertir la lista
        self._round_robbin.reverse()
        return next

    def get_player(self, caracter):
        return self._players[caracter]
