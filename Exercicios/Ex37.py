import binascii

numero = int(input("Escreva um número inteiro: "))

print("""
Escolha uma das bases para conversâo:
[ 1 ] converter oara BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL
""")

opcao = int(input("Sua opção: "))

if opcao == 1:
    print(f"{numero} convertido para BINÁRIO é igual a {bin(numero)[2:]}")
elif opcao == 2:
    print(f"{numero} convertido para OCTAL é igual a {oct(numero)[2:]}")
elif opcao == 3:
        print(f"{numero} convertido para HEXADECIMAL é igual a {hex(numero)[2:]}")
else:
    print("O caractere não entra em uma das opções acima.")
