#faça um algoritmo que some todos os multiplos de 3 impares no intervalo de 1 a 500
totDiv3 = 0

for c in range(1, 500 + 1):
    if c % 3 == 0 and c % 2 == 1:
        totDiv3 += c

print(f"a soma de todos os divisores de 3 no intevalo de 1 ate 500 é {totDiv3}")