#Fazer o nome aparecer em maisculas
#Fazer o nome aparecer em minusculas
#Quantidade de letras do nome sem o espaço
#Aparecer primeiro nome e quantidade de letras

nome = str(input("Digite seu nome: ")).strip()

print("Seu nome em maísculas é: " + nome.upper())
print(f"Seu nome em mínusculas é: {nome.lower()}")
#maneira mais dificil de fazer criando outra variavel
nomeDividido = nome.split()
print(f"""A quantidade de letras do seu nome inteiro é: {len(nome) - nome.count(' ')}
O seu primeiro nome é: {nomeDividido[0]} e a quantidade de letras é: {len(nomeDividido[0])}""")
print(f'Seu primeiro nome tem {nome.find(' ')} letras')