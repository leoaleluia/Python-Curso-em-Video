#crie um programa que mostre todos os números pares no intervalo de 1 e 50
numPar = 0

for c in range(1, 50 + 1):
    if c % 2 == 0:
        numPar += 1
        print(f"{c} é par")

print(f"O total de números pares é {numPar}")