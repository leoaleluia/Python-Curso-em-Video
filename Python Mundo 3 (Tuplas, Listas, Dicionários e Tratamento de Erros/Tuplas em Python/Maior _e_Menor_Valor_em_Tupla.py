from random import randint 



numeros = (randint(0, 35), randint(0, 35), randint(0, 35), randint(0, 35), randint(0, 35))
Maior = Menor = numeros[0]

for c in numeros:
    if c > Maior:
        Maior = c
    if c < Menor:
        Menor = c

print(f"Os números sorteados foram {numeros} e o maior é {Maior} e o menor {Menor}")