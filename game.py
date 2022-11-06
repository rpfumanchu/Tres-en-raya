import pyfiglet
from enum import Enum, auto
from player import Player,HumanPlayer
from match import Match
from square_board import SquareBoard
from list_utils import reverse_matriz
from beautifultable import BeautifulTable
from settings import BOARD_LENGTH

class RoundType(Enum):
    COMPUTER_VS_COMPUTER = auto()
    COMPUTER_VS_HUMAN = auto()

class DifficultyLevel(Enum):
    LOW = auto()
    MEDIUM = auto()
    HIGT = auto()

class Game():

    def __init__(self,round_type = RoundType.COMPUTER_VS_COMPUTER, match = Match(Player("chip"), Player("chop"))):
        #guardar valores recividos
        self.round_type = round_type
        self.match = match

        #tablero vacio sobre el que jugar
        self.board = SquareBoard()

    def start(self):
        #imprimo el nombre del juego
        self.print_logo()
        #configura la partida
        self._configure_by_user()
        #arranco el game loop
        self._start_game_loop()
        

    def print_logo(self):
        logo = pyfiglet.Figlet(font="stop")
        print(logo.renderText("Connecta"))

    def _start_game_loop(self):
        #un cucle infinito
        while True:
            #obtengo el jugador de turno
            current_player = self.match.next_player
            #le hago jugar
            current_player.play(self.board)
            #muestro su jugada
            self.display_move(current_player)
            #imprimi el tablero
            self.display_board()
            #si el juego a terminado...
            if self._is_game_over():
                # muestro resultado final
                self.display_result()
                #salgo del bucle 
                break

    def display_move(self, player):
        print(f"\n{player.nombre} ({player.caracter}) a movido en la columna {player.last_move} ")

    def display_board(self):
        """
        imprimir el tablero en su estado actual
        """
        #obtenemos una matriz de caracteres a partir del tablero
        matriz = self.board.una_matriz()
        matriz = reverse_matriz(matriz)
        #crear la tabla de beautifultable
        bt = BeautifulTable()
        for col in matriz:
            bt.columns.append(col)
        bt.columns.header = [str(i) for i in range(BOARD_LENGTH)]
        #imprimirla
        print(bt)

    def display_result(self):
        winner = self.match.get_winner(self.board)
        if winner != None:
            print(f"\n{winner.nombre} ({winner.caracter}) ganador!!! ")
        else:
            print(f"\n hay un empate {self.match.get_player('x').nombre} (x) y {self.match.get_player('o').nombre} (o) ")

    def _is_game_over(self):
        """
        el juego se ha terminado cuabdo hay un vencedor o hay un empate
        """
        winner = self.match.get_winner(self.board)
        if winner != None:
            #hay un vencedor
            return True
        elif self.board.is_full():
            return True
        else:
            return False

    def _configure_by_user(self):
        """
        le pido al usuario los valores que el quiere para tipo de partida y el nivel de dificultad
        """
        #determinar el tipo de partida (preguntando al usuario)
        self.round_type = self._get_round_type()
        
        #crear la partida
        self.match = self._make_match()

    def _make_match(self):
        """
        player1 siempre robotico
        """
        if self.round_type == RoundType.COMPUTER_VS_COMPUTER:
            #ambos jugadores robóticos
            player1 = Player("T-X")
            player2 = Player("T-1000")
        else:
            #ordenador vs humano
            player1 = Player("T-800")
            player2 = HumanPlayer(nombre=input("introduce tu nombre  "))
        return Match(player1, player2)
    
    def _get_round_type(self):
        """
        preguntamos al usuario
        """
        print("""
        Selecciona el tipo de partida:
        1) Computer VS Computer
        2) Computer VS Human
        """)
        response = ""
        while response != "1" and response != "2":
            response = input("Por favor elige entre 1 o 2:  ")
        if response == "1":
            return RoundType.COMPUTER_VS_COMPUTER
        else:
            return RoundType.COMPUTER_VS_HUMAN

    
            

