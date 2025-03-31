# O usuario coloca o input do seu nome inteiro e ele retorna o primeiro nome e ultimo nome

nome = str(input("Digite seu nome: ")).strip().split()

print(f"""
Muito prazer em te conhecer!
Seu primeiro nome é {nome[0]}
Seu ultimo nome é {nome[len(nome) - 1]}
""")