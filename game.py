import pyfiglet

class Game:
    def start(self):
        #imprimo el nombre del juego
        self.print_logo()
        #configura la partida
        #arranco el game loop
        pass

    def print_logo(self):
        logo = pyfiglet.Figlet(font="stop")
        print(logo.renderText("Connecta"))