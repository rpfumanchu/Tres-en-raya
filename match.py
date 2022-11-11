from square_board import SquareBoard

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
        

    # queremos sintaxis de propiedad para esto :puede ser usado para modificar un método para que sea un atributo o propiedad
    @property
    def next_player(self):
        next = self._round_robbin[0]
        # usaremos el metodo reverse(), para invertir la lista
        self._round_robbin.reverse()
        return next

    def get_player(self, caracter):
        return self._players[caracter]

    def get_winner(self, board):
        """
        devuelve el jugador y si no lo hay, devuelve None
        """
        if board.is_victory("x"):
            return self.get_player("x")
        elif board.is_victory("o"):
            return self.get_player("o")
        else:
            return None
        
    def is_match_over(self):
        """
        pregunta al usuario si se atreve a jugar otra partida
        """
        result = True
        while True:
            respuesta = input("¿Te atreves a jugar otra partida? (Y/N)").upper()
            if respuesta == "Y":
                result = False
                break
            elif respuesta == "N":
                result = True
                break
        return result


