
nome = str(input('Qual é seu nome? '))
print(nome * 20)
print('Prazer em te conhecer {:20}!'.format(nome))
print('Prazer em te conhecer {:>20}!'.format(nome))
print('Prazer em te conhecer {:<20}!'.format(nome))
print('Prazer em te conhecer {:^20}!'.format(nome))
print('Prazer em te conhecer {:=^20}!'.format(nome))
print(f'Prazer em te conhecer {nome:=^20}!')

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print(f'A soma vale {n1+n2}')
print('A soma é {}, \n o produto é {}, e a divisão é {:.3f}.'.format(s, m, d), end=' ')
print(f' Divisão inteira {di}, potência {e}.')

#Dois modos de formatar agora hehehe
#end='' serve para continuar a linha para linha de baixo não querbrando a linha
#De uma forma contrária o \n quebra a linha atual, sem precisar fazer prints
