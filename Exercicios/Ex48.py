#Faça um programa que calcule a soma entre todos os números que são múltiplos 
# de três e que se encontram no intervalo de 1 até 500.

# minha versão 
soma = 0
contador = 0
for valores in range(0, 501):
    if valores %3 == 0 and valores %2 == 1:
        soma += valores
        contador += 1
print(f"A soma de todos os {contador} valores solicitados é {soma}")

# Sr goiabada version
contador = 0
soma = 0
for valores in range(1, 501, 2):
    if valores %3 == 0:
        contador = contador + 1 # Ele vai receber todos os valores que estão na instancia if
        soma = soma + valores # Ele vai somar todo o range porém com a instancia if
print(f"A soma de todos os {contador} valores solicitados é {soma}")
