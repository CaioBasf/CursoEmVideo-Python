#Fazer um progama que informe qual é a unidade, dezena, centena e milhar

'''numero = str(input('Insira seu número: ')).split()
print(f"""Unidade = {numero[0] [3]}
Dezena = {numero[0] [2]}
Centena = {numero[0] [1]}
Milhar = {numero[0] [0]}""")'''

'''
numero = str(input('Insira seu número: '))
print(f"""
Milhar = {numero[0:1]}
Centena = {numero[1:2]}
Dezena = {numero[2:3]}
Unidade = {numero[3:4]}
""")'''


numero = int(input('Insira seu número: '))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print(f"""
Analisando o número {numero}
Unidade = {unidade}
Dezena = {dezena}
Centena = {centena}
Milhar = {milhar}
""")
