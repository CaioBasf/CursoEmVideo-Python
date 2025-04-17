#Reforça o DESAFIO 35 dos triangulos, acrescentando o recurso de mostar que tipo de triangulo será formado:
# Escaleno: todos os lados são diferentes
# isósceles: dois lados iguais
# Equilatero: Todos os lados iguais
A = float(input("Escreva o segmento A: "))
B = float(input("Escreva o segmento B: "))
C = float(input("Escreva o segmento C: "))

if A + B > C and A + C > B and B + C > A:
    print("Os segmentos acima Podem formar um Triângulo", end=" ")
    if A != B != C and B != C != A and C != A != B:
        print("ESCALENO")
    elif A == B != C or B == C != A or C == A != B:
        print("ISÓSCELES")
    elif A == B == C:
        print("EQUILÁTERO")
else:
    print("Os segmentos acima não podem formar um triângulo")   