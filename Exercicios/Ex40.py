n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))
media = (n1 + n2) / 2

print(f"Tirando {n1} e {n2} sua média foi {media}")
if media >= 7.0:
    print("O aluno PASSOU!")
elif media >= 5.0 <= 6.9:
    print("O aluno está de RECUPERAÇÃO")
elif media <= 5.0:
    print("O aluno está REPROVADO")