
import math
co = float(input('Número do cateto Oposto: '))
ca = float(input('Númeor do cateto Adjacente: '))
hi = math.hypot(co, ca)
print(f'O cateto Oposto é {ca}, cateto Adjacente é {ca} e a Hipotenusa é {hi:.2f}')


catOps = float(input('Comprimento do cateto Oposto: '))
catAdj = float(input('Comprimento do cateto Adjacente: '))
cal = (catOps**2 + catAdj**2) ** (1/2)
print(f'O número do cateto Oposto é {catOps}, cateto Adjacente {catAdj} e a Hipotenusa é {cal}2')


# !!!!**(1/2) = Raiz quadrada!!!!
# Aprender a pesquisar mais como funciona nas bibliotecas