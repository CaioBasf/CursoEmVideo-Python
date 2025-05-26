#Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

nm = int(input("Escreva um número: "))

for i in range(1, nm+1):
    print(f"{i}", end=" ")
    if nm % i:
        cont += 1
    
print(f"O número {nm} foi divisivel {cont} vezes")
if cont == 2:
    print("Ele é primo")
else:
    print("Ele não é primo")