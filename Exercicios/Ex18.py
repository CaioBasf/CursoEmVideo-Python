#Faça um programa que leia o ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

# "as" siginifica que a biblioteca vai passara ser o descrito depois da sigla, no caso de precisar chamala
import math 
''''
anguloQualquer = float(input("Coloque o número do seu ângulo para ver os valores seno, cosseno e tangente "))
conversorRadianos = math.radians(anguloQualquer)
cosseno = math.cos(conversorRadianos)
seno = math.sin(conversorRadianos)
tangente = math.tan(conversorRadianos) 

print(f"O seu angûlo tem os seno de {seno:.2f} o seno de {cosseno:.2f} e a tangente de {tangente:.2f}")
'''
#jeito mais fácil

anguloQualquer = float(input("Coloque seu ângulo qualquer para ver seno, cosse e tangente "))
cosseno = math.cos(math.radians(anguloQualquer))
print(f"{cosseno:.2f} é o cosseno de {anguloQualquer:.2f}")
seno = math.sin(math.radians(anguloQualquer))
print(f"{seno:.2f} é o seno de {anguloQualquer}")
tangente = math.tan(math.radians(anguloQualquer))
print(f"{tangente:.2f} é a tangente de {anguloQualquer:.2f}")