# Desenvolva um programa que leia seis números inteiros 
# e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
soma = 0
cont = 0
for i in range (1, 7):
    nm = int(input(f"Digite o {i} valor: "))
    if nm %2 == 0:
        soma += nm
        cont += 1
print(f"Voce informou {cont} números e a soma deles foi {soma}")

# n += i == n + n = i