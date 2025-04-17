'''
Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, 
considerando o seu preço normal e condição de pagamento:
à vista dinheiro/cheque: 10% de desconto
à vista no cartão: 5% de desconto
em até 2x no cartão: preço normal
3x ou mais no cartão: 20% de juros
'''

print(8*"=", "Lojiho do Tadeu", 8*"=")
preco = float(input("Preço das compras: R$"))

print("""
FORMAS DE PAGAMENTO
[ 1 ] a vista dinheiro/cheque
[ 2 ] a vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
""")
opcao = int(input("Qual é a opcão? "))

if opcao == 1:
    desconto = (preco / 100) * 10
    print(f"Sua compra de R${opcao} vai custar {desconto} no final.")
elif opcao == 2:
    desconto = (preco / 100) * 5
    print(f"Sua compra de R${opcao} vai custar {desconto} no final")
elif opcao == 3:
    print(f"Sua compra vai custar R${opcao}")
elif opcao == 4:
    parcelas = int(input("Quantas parcelas? "))
    juros = ((preco / 100) * 20) + preco
    print(f"Sua compra será parcelada em {parcelas} de R${juros / parcelas}")
    print(f"Sua compra de R${preco} vai custar R${juros} no final")