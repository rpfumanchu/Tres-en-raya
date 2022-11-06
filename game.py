import pyfiglet
from enum import Enum, auto
from player import Player,HumanPlayer
from match import Match
from square_board import SquareBoard

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
        pass

    def _configure_by_user(self):
        """
        le pido al usuario los valores que el quiere para tipo de partida y el nivel de dificultad
        """
        #determinar el tipo de partida (preguntando al usuario)
        self.round_type = self._get_round_type()
        
        #crear la partida
        self.match = self._make_match()

        

        
        
        

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
            player2 = HumanPlayer(name=input("introduce tu nombre"))
        return Match(player1, player2)
            

