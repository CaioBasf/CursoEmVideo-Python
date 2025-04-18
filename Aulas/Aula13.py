# O ultimo número do range ele sempre ignora, Ex: 1,6 ele ignora o 6 e vai até o 5
for c in range(1, 6):
    print(c)
print("FIM")

# Aqui ele vai contar do modo reverso do 6 até o 1, sem ignorar o último
for c in range (6, 0, -1):
    print(c)
print("FIM")

# ele vai contar de 0 a 7 pulando de 2 em 2
for c in range (0, 7, 2):
    print(c)
print("FIM")

# N+1 é para coloca o número exato que a pessoa digitou
n = int(input("Digite um número: "))
for c in range(0, n+1):
    print(c)
print("FIM")

# Teoria parecida com a do anterior porém com a possibilidade de alterar tudo
i = int(input("Inicio: "))
f = int(input("FIM: "))
p = int(input("Passo: "))
for c in range(i, f+1, p):
    print(c)
print("FIM")

# ele soma todos os valores escolhidos no for
s = 0
for c in range(0, 5):
    n = int(input("digite um valor:"))
    s += n
print(f"O somatorio de todos os valoras foi {s}")