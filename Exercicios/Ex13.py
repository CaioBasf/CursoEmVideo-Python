sl = float(input('Qual é o salário do funcionario? R$'))
au = sl + (sl*15 / 100)
print(f'Um funcionario que ganhava R${sl}, com 15% de aumento, passa a receber R${au:.2f}')
