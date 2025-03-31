# Um jogo de advinhação entre 0 e 5
import random
import time

print('-=-' * 20)
print("Vou pensar em um número entre 0 e 5, tente advinhar!")
print("-=-" * 20)
aleatorio = random.randint(0, 5)
advinha = int(input("Em que númeoro eu pensei? "))
print("PROCESSANDO...")
time.sleep(2)
if aleatorio == advinha:
    print("Parábens você acertou!!!!!!!")
else:
    print(f"Eu pensei no número {aleatorio} e você falou {advinha} Eu ganhei!")
print("--Programa Finalizado--")