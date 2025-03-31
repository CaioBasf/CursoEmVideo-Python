print('\033[31;43mHello, World\033[m')
a = 4
b = 5
print(f'Os valores são \033[32m{a}\033[m e \033[31m{b}\033[m!!!')
nome = 'Caio'
cores = {'limpa':'\033[m',
        'azul':'\033[34m',
        'amarelo':'\033[33m',
        'pretoebranco':'\033[7;30m'}
print(f'Olá! Muito prazer em te conhecer, {cores['pretoebranco']}{nome}{cores['limpa']}!!')

# \033[STYLE;TEXT;BACK "Código" \033[m

'''
STYLE
0 = None = Nenhum
1 = Bold = Negrito 
4 = Underline = Sublinha
7 = Negative = Inverte

TEXT
30 = Branco
31 = Vermelho
32 = Verde
33 = Amarelo
34 = Azul
35 = Roxo
36 = Ciano
37 = Cinza

BACK
40 = Branco
41 = Vermelho
42 = Verde
43 = Amarelo
44 = Azul
45 = Roxo
46 = Ciano
47 = Cinza
OBS: Existem mais códigos porém esses funcionam melhor no python
Colorize = Trabalha com cores no terminal em Hexadecimal
'''