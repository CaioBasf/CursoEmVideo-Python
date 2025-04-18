from time import sleep
from random import randint
print("""
Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
""")

itens = ("Pedra", "Papel", "Tesoura")
jogador = int(input("Qual é a sua jogada? "))
computador = randint(0, 2)

sleep(1)
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")
sleep(1)

print(15*"-=")
print(f"Jogador jogou {itens[jogador]}")
print(f"Computador jogou {itens[computador]}")
print(15*"-=")

if computador == 0: # Pedra
    if jogador == 1:
        print("JOGADOR GANHOU")
    elif jogador == 2:
        print("COMPUTADOR GANHOU")
elif computador == 1: # Papel
    if jogador == 0:
        print("COMPUTADOR GANHOU")
    elif jogador == 2:
        print("JOGADOR GANHOU")
elif computador == 2: # Tesouro
    if jogador == 0:
        print("JOGADOR GANHOU")
    elif jogador == 1:
        print("COMPUTADOR GANHOU")
elif computador == jogador:
    print("EMPATE")
