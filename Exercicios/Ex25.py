# Input de um nome completa e verifica se possui um sobrenome especifico nele

nome = str(input("Digite seu nome inteiro: ")).strip()
print(f"Seu nome tem Silva? {'SILVA' in nome.upper()}")