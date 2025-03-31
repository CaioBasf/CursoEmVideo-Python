#Escreva um programa que pergunte o salário de um= funcionario e calcula 
#o valor do seu aumento.
#Para salários superiores a R$1.250.00. calcule um aumento de 10%
#Para os inferiores ou iguais, o aumento é de 15%

salario = float(input("Qual o seu salário? "))

if salario <= 1250:
    salarioNovo = ((15 / 100) * salario) + salario
else:
    salarioNovo = ((10 / 100) * salario) + salario
print(f"Seu salario é de R${salarioNovo} agora")

