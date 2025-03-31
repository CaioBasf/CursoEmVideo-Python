#Um programa que ve a cidade que vc nasceu retornando um valor true caso a primeira palavra seja santo

#Maneira errada pois se a palavra Santo estiver depois vai contar como True
'''
cidade = str(input("Qual cidade você nasceu? ")).strip()
print('SANTO' in cidade.upper())'
'''

#Maneira 2 de fazer isso (Guanabara)
cidade = str(input("Qual cidade você nasceu? ")).strip()
print(cidade[:5].upper() == 'SANTO')