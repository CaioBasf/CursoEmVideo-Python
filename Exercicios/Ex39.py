"""faça um programa que leia o ano de nascimento de um jovem e informe
de acordo com sua idade, se ele ainda vai se alistar ao serviço militar,
se está na hora de se alistar ou se ja passou o tempo do alistamento.
seu programa também deve mostrar o tempo que falta ou que passou do prazo.
"""
import datetime

atual = datetime.date.today().year
nascimento = int(input("Qual sua data de nascimento? "))
idade = atual - nascimento

print(f"Quem nasceu em {nascimento} tem {idade} anos em {atual}")

if nascimento >= atual:
    print("Você digitou errado")
elif idade > 18:
    print(f"Você já deveria ter se alistado há {idade - 18} anos")
    print(f"Seu alistamento foi em {nascimento + 18}")
elif idade < 18:
    print(f"Você ainda não precisa se alistar, apenas em {18 - idade} anos")
    print(f"Seu alistamento deve acontecer em {nascimento + 18}")
elif idade == 18:
    print("Você tem que se alistar IMEDIATAMENTE!")
