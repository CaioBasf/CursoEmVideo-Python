from unicodedata import numeric


n1 = input('Digite um número qualquer')
an1 = int(input('Digite um número'))
an2 = int(input('Digite outro número'))
soma = an1 + an2
print('a soma entre {an1} e {an2} vale {soma}'.format(an1, an2, soma))

"""
Comentário
"""

#comentário

n = input('Digite algo: ')
print(n.islower())
print(type(n))

var1 = str(input('Digite algo '))
print(type(var1))
print(var1.islower())
print('Oq vc escreveu é númerico? {}'.format(var1.isnumeric()))
#O espaço afeta como ele identifa o valor