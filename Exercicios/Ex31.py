#Desenvolva um programa que pergunta a diatancia de uma viagem
#em Km. Calcule o preço da passage, cobrando R$0,50 por KM para viagens
# de até 200km e R$0,45 para viagens mais longas

distancia = float(input("Qual a distancia da sua viagem em Km? "))
print(f"Você está prestes a começar uma viagem de {distancia}Km")

if distancia <= 200:
    preco = distancia * 0.50
else:
    preço = distancia * 0.45
print(f"O custo dessa viagem vai ser R${preco:.2f}")