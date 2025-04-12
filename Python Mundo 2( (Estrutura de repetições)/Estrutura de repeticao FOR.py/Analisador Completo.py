
totMenorDe20 = 0
mediaIdade = 0
maisVelho = 0
nomeMaisVelho = ''

numPessoas = int(input("Digite a quantidade de pessoas que deseja analisar"))

for c in range (0, numPessoas):
    sexo = input("Qual é o sexo da pessoa? [M / F]: ").upper()
    if sexo == 'F':
        nomeFeminino = input("Digite o nome: ")
        idade = int(input("Digite a idade: "))
        mediaIdade += idade
        if idade < 20:
            totMenorDe20 += 1
    if sexo == 'M':
        nomeMasculino = input("Digite o nome: ")
        idade = int(input("Digite a idade: "))
        mediaIdade += idade
        if idade > maisVelho:
            maisVelho = idade
            nomeMaisVelho = nomeMasculino
mediaIdade //= numPessoas

print(f"a pessoa mais velha é {nomeMaisVelho} com a idade de {maisVelho} e há {totMenorDe20} mulheres abaixo dos 20 anos. A media de idade é de {mediaIdade}")