#Desenvolva um programa que leia o comprimento de três retas e diga
#ao usuário se elas podem ou não formar um triângulo.

A = float(input("Escreva se segmento 1: "))
B = float(input("Escreva seu segmento 2: "))
C = float(input("Escreva seu segmento 3: "))

# Se a soma das medidas de dois deles é sempre maior que a medida do terceiro
# Então eles podem formar um triângulo

if A + B > C and A + C > B and B + C > A:
    print("Os segmentos acima podem formar um triângulo")
else: 
    print("Os segmentos acima não podem formar um triângulo")