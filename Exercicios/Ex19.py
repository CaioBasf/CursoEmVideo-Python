import random

n1 = str(input("Aluno 1: "))
n2 = str(input("Aluno 2: "))
n3 = str(input("Aluno 3: "))
n4 = str(input("Aluno 4: "))

lista = [n1, n2, n3, n4]
nomeAleatorio = random.choice(lista)
print(f"O nome aleatorio é: {nomeAleatorio}")