#faça um programa que leia o peso de varias pessoas e mostre qual é o maior e o menor peso
numPessoas = int(input("Digite a quantidade de pessoas que deseja analisar: "))
maiorPeso = 0
menorPeso = 0
for c in range(0, numPessoas):
    pessoa = float(input(f"Digite o peso da {c}º pessoa"))
    if pessoa > maiorPeso:
        maiorPeso = pessoa
    if menorPeso == 0:
        menorPeso = pessoa
    if pessoa < menorPeso:
        menorPeso = pessoa

print(f"A pessoa mais pesada é {maiorPeso}  e a mais leve é {menorPeso}")