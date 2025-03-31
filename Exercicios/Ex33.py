# Requisita três valores e devolve o menor e maior entre os três

numero1 = int(input("Escreva o primeiro valor: "))
numero2 = int(input("Escreva o segundo valor: "))
numero3 = int(input("Escreva o terceiro valor: "))

# Verificando menor valor 
menor = numero1
if numero2 < numero1 and numero2 < numero3:
    menor = numero2
elif numero3 < numero1 and numero3 < numero2:
    menor = numero3

# Verificando maior valor
maior = numero1
if numero2 > numero1 and numero2 > numero3:
    maior = numero2
elif numero3 > numero1 and numero3 > numero2:
    maior = numero3
print(f"O menor número é {menor}")
print(f"O maior númeor é {maior}")
