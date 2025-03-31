import math #Importa toda a biblioteca
from math import sqrt, floor #importa apenas a função/ funçoes escolhidas
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
# Quando é importado apenas a função não é necessario colocar Math apenas a função desejada
print(f'A raiz de um {num} é outro {math.ceil(raiz)} arredondado para cima')
print(f'A raiz de um {num} é {math.floor(raiz)} arredondado para baixo')
#Mesmo formato caso eu apenas tenho importado a fução no floor
print(f'A raiz de um {num} é exatamente {raiz}')



import random
num1 = random.randint(1,10)
print(num1)


import emoji
print(emoji.emojize('Olá, :globe_showing_americas:', language='alias'))
#sempre instalar tudo que pede nas bibliotecas

