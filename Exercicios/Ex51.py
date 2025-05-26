"""
Desenvolva um programa que leia o primeiro 
termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
"""

print(20*"=")
print("10 TERMOS DE UMA PA")
print(20*"=")

pt = int(input("Primeiro termo: "))
r = int(input("Razão: "))
decimo = pt + (10-1)*r
for i in range (pt, decimo + r, r):
    print(f"{i}", end = " -> ")

print("Acabou")