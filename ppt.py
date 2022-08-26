import random
import os 
os.system("cls")

uno = "Piedra"
dos = "Papel"
tres = "Tijera"

r = "S"
c = 0


while r =="S" or r == "s":
    n = input("Elija una de las tres opciones uno, dos o tres: ").lower()
    if n == "uno":
        print("Usted elijio ", uno )
    elif n == "dos":
        print("Usted elijio ", dos )
    elif n == "tres":
        print("Usted elijio ", tres )

    x = random.randint(1,3)
    if x == 1:
        print("La maquina elijio ", uno)
    if x == 2:
        print("La maquina elijio ", dos)
    if x == 3:
        print("la maquina elijio ", tres)

    if n == "uno" and x == 1:
        print("Es un empate")
    elif n == "dos" and x == 2:
        print("Es un empate")
    elif n == "tres" and x == 3:
        print("Es un empate")    
    elif n == "uno" and x == 2:
        print("El jugador eligio ", dos, "la maquina eligio ",uno, "\nGana la maquina\nPapel envuelve a piedra" )
    elif n == "uno" and x == 3:
        print("El jugador eligio ", uno, "la maquina eligio ", tres,"\nGanas vos \nPiedra Rompre tijera")
    elif n == "dos" and x == 1:
        print("El jugador eligio ", dos, "la maquina eligio ", uno, "\nGanas vos \nPapel envuelve tijera")
    elif n == "dos" and x == 3:
        print("El jugador eligio ", dos, "la maquina eligio " , tres, "\nGana la maquina \nTijera corta papel")
    elif n == "tres" and x == 1:
        print("El jugador eligio ", tres, "la maquina eligio " , uno, "\nGana la maquina \nPiedra rompe tijera")
    elif n == "tres" and x == 2:
        print("El jugador eligio ", tres, "la maquina eligio " , dos, "\nGanas vos \nTijera corta papel")
    r = input("¿Desea jugar de nuevo? S/N")
    
    c +=1


print("FIN DEL JUEGO")
print("Has jugado ",c, " partidas")

