#faaça um programa que leia  quantidade de varias pessoas e mostre a quantidade de pessoas maiores e menores de idade
from datetime import date
numPessoas = int(input("Digite a quantidade de pessoas que deseja verificar a maior ou menor idade"))
anoAtual = date.today().year
maiorIdade = 0
menorIdade = 0
for c in range(0, numPessoas):
    anoNasc = int(input("Digite o ano de nascimento"))
    idade = anoAtual - anoNasc
    if idade >= 18:
        maiorIdade += 1
    else:
        menorIdade += 1

print(f"Pessoas com a mior idade {maiorIdade}\nPessoas com a menor idade{menorIdade}")