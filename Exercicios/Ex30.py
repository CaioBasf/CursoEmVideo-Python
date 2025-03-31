#Um programa para ver se é par ou impar

numero = int(input("Escreva um número "))
conta = numero % 2

if conta == 0:
    print(f"O número {numero} é par")
else:
    print(f"O número {numero} é impar")