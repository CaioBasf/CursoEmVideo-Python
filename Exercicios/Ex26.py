# Verifica uma frase aleatoria
# Verfica quantas vezes a letra A aparece na setença
# Verifica quando foi a primeira vez que a letra A apareceu
# Verifica quantas vezes a ultima letra A apareceu

'''
frase = str(input("Digite uma frase: ")).strip()
fraseFormatado = str(len(frase) - frase.count(' '))


print(f"""
A letra A aparece {fraseFormatado.count('a')} vezes
A letra A aparece primeiro em {fraseFormatado.find('a')}
A letra A aparece pela ultima vez em {fraseFormatado.find('a')}
""")'
'''

frase = str(input("Digite uma frase: ")).strip().upper()
print(f"A letra A aparece {frase.count('A')}")
print(f"A primeira letra A aparece em {frase.find("A") + 1}")
print(f"A letra A aparece pela ultima vez em {frase.rfind("A") + 1}")