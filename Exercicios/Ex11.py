Al = float(input('Qual a Altura da sua parede? '))
La = float(input('Qual a largura da sua parede? '))
Area = Al * La
tinta = Area/2
print(f'Sua parede tem a dimensão de {Al}x{La} e sua área é de {Area}m2')
print(f'Para pintar essa parede, você precisará de {tinta:.2f}l de tinta.')