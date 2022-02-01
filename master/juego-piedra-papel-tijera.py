import random

print("===================================================")
print("Juego de piedra, papel o tiejera con la computadora")
print("===================================================")

def jugar():

    usuario = input("Escribe lo siguiente: 'pi' para piedra, 'pa' para papel, 'ti' para tijera.\n => ").lower()
    computadora = random.choice(["pi", "pa", "ti"])

    if(ganoJugador(usuario, computadora)):
        
        return "Ganastes"
    return "Perdiste"


def ganoJugador(jugador, oponente):

    if(jugador == "pi" and oponente == "ti") or (jugador == "pa" and oponente == "pi") or (jugador == "ti" and oponente == "pa"):
        return True
    else:
        False

print(jugar())