peso = int(input("Qual é seu peso? (Kg) "))
altura = float(input("QUal é sua altura? (m) "))
imc = peso / altura**2
print(f"O IMC dessa pessoa é de {imc:.1f}")
if imc < 18.5:
    print("Você está abaixo do peso ideal")
elif imc <= 25:
    print("Você está no peso ideal, parabéns")
elif imc <= 30:
    print("Você está com sobrepeso")
elif imc <= 40:
    print("Você está obeso")
elif imc > 40:
    print("Você está com obesidade morbida, cuidado")