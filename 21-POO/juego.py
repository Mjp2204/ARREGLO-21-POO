from Cartas import *

class Juego:
    def __init__(self):
        self.mazo = mazo()
        self.casa = mazo(True)
        self.jugador = mazo(True)

    def iniciar_juego(self):
        print("BIENVENIDO A BLACKJACK")
        print("** VAMOS A EMPEZAR **")
        self.casa.agregar_carta(self.mazo.dar_carta())
        self.casa.agregar_carta(self.mazo.dar_carta())
        self.jugador.agregar_carta(self.mazo.dar_carta())
        self.jugador.agregar_carta(self.mazo.dar_carta())

    def mostrar_juego(self):
        print("Jugador: ")
        self.jugador.mostrar_carta(True)
        print("La sumatoria de sus cartas es: ", self.jugador.dar_valor())
        while self.jugador.dar_valor() == 21:
            print("!HAZ GANADO¡")
            break
        print("Casa: ")
        self.casa.mostrar_carta()

    def Plant_casa_juego(self):
        self.casa.dar_valor()
        print("TURNO DE LA CASA")
        while self.casa.dar_valor() < 17:
            self.casa.agregar_carta(self.mazo.dar_carta())
            self.casa.dar_valor()

        rest_casa= 21 - self.casa.dar_valor()
        rest_jugador= 21 - self.jugador.dar_valor()
            
        if self.casa.dar_valor() > 21:
            print("La casa ha obtenido un valor de: ", self.casa.dar_valor(), "por lo tanto !LA CASA HA PERDIDO Y HAZ GANADO¡")
            return
        if rest_casa < 0:
            print("El valor total de la casa es: ", self.casa.dar_valor(), " y el de el jugador es: ", self.jugador.dar_valor())
            print("!HAZ GANADO¡")
            return
        elif rest_jugador < 0:
            print ("El valor total de la casa es: ", self.casa.dar_valor(), " y el de el jugador es: ", self.jugador.dar_valor())
            print("!LA CASA HA GANADO¡")
            return
        
        if rest_casa < rest_jugador:
            print("El valor total de la casa es: ", self.casa.dar_valor(), " y el de el jugador es: ", self.jugador.dar_valor())
            print("!HAZ GANADO¡")
        elif rest_casa > rest_jugador:
            print ("El valor total de la casa es: ", self.casa.dar_valor(), " y el de el jugador es: ", self.jugador.dar_valor())
            print("!LA CASA HA GANADO¡")
        else:
            print("El valor total de la casa es: ", self.casa.dar_valor(), " y el de el jugador es: ", self.jugador.dar_valor())
            print("!ES UN EMPATE¡")


    def Plan_juego(self):
        while len(self.jugador.cartas) == 2:
            cont_juego = int(input("Desea plantarse (1) o desea otra carta(2): " ))
            print(cont_juego)
            if cont_juego == 1:
                self.Plant_casa_juego()
                break
            elif cont_juego == 2:
                self.jugador.agregar_carta(self.mazo.dar_carta())
                self.jugador.mostrar_carta(True)
                print("La sumatoria ahora es de: ", self.jugador.dar_valor())
                if self.jugador.dar_valor() > 21:
                    print ("Haz pasado el limite de puntos, por lo cual !HAZ PERDIDO Y LA CASA GANA¡")
                    break

    

