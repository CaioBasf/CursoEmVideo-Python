# O usuario deve colocar a velocidade e deve voltar se ele excedou ou não a velocidade
# Se ele ultrapassar 80 km/h ele será multado 
# A multa vai custar reais a cada km acima do limite

km = float(input("Qual a sua velocidade atual? "))

if km > 80:
    print("MULTADO! Você excedeu o limite permitido que é 80Km/h ")
    print(f"Você deve pagar uma multa de R${(km - 80) * 7.0}")
print("Tenha um bom dia! e dirija com segurança!")