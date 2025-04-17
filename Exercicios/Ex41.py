import datetime as dt

nascimento = int(input("Ano de Nascimento: "))
idade = dt.date.today().year - nascimento

print(f"O atleta tem {idade} anos")
if 0 < idade <= 9:
    print("É um atleta MIRIM")
elif idade <= 14 :
    print("É um atleta INFANTIL")
elif idade <= 19:
    print("É um atleta JUNIOR")
elif idade <= 25:
    print("É um atleta SÊNIOR")
elif idade > 25:
    print("É um atleta MASTER")
else:
    print("Tente novamente")