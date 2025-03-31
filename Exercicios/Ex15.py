km = float(input("Quantos Kilometros você percorreu? "))
dias = int(input("Quantos dias você andou no carro? "))
pagamento = (km * 0.15) + (dias * 60)
print(f"Você deve a nós R${pagamento:.2f} de pagamento.")