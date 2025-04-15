'''
Escreva um programa para aprovar o empréstimo bancário
para a compra de uma casa. O programa vai perguntar
o valor da casa, o salário do comprador e em quantos anos
ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não
pode exceder 30% do salário ou então o empréstimo será negado.
'''


casa = float(input("Qual o valor da casa: R$"))
salario = float(input("Qual o seu salário: R$ "))
anos =  int(input("Em quantos anos de financiamento? "))
prestacao = casa / (anos*12)
minimo = (salario/100 *30)

print(f"Para pagar uma casa de R$\033[0;32m{casa}\033[m em \033[0;32m{anos}\033[m anos de prestação será de R$\033[0;32m{prestacao:.2f}\033[m ")
if minimo < prestacao:
    print("Seu empréstimo foi \033[0;31mNEGADO\033[m")
else:
    print(f"Seu empréstimo foi \033[0;32mAPROVADO\033[m!!!")
