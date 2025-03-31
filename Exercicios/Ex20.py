# O usuario inputa nomes em uma lista e volta com os nomes embaralhados.

from random import shuffle

nome1 = str(input("ALuno 1: "))
nome2 = str(input("ALuno 2: "))
nome3 = str(input("ALuno 3: "))
nome4 = str(input("ALuno 4: "))

lista = [nome1, nome2, nome3, nome4]
shuffle(lista)
print(lista)
