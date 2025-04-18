print("Bem vindo ao analisador de dados por grupo")
totHomemM20 = totHomens = totIdadeMaior = totMulheres = totMulherM20 = totPessoas =  0
while True:
    res = input("Deseja cadastar uma pessoa?[S/N]").upper().strip()[0]
    while res not in "SsNn":
        res = input("Digite [S] para sim e [N] para não").upper().strip()[0]
    if res == 'S':
        totPessoas += 1
        idade = int(input("Digite a idade: "))
        if idade > 18:
            totIdadeMaior += 1
        sexo = str(input("Digite o sexo: [M] masculino / [F] femnino: ")).upper().strip()
        while sexo not in 'MF':
            sexo = str(input("Digite uma opção válida [M] para masculino e [F] para feminino")).upper().strip()
            print(sexo)
        if sexo == 'F':
            totMulheres += 1
            if idade < 20:
                totMulherM20 += 1
        else:
            totHomens += 1
            if idade < 20:
                totHomemM20 += 1
    else:
        break
print(f'''o tal de pessoas cadastadas foram {totPessoas} e pessoas acima dos 18 anos foram {totIdadeMaior}\n o total de homens foram {totHomens} e homens abaixo dos 20 anos foram {totHomemM20}\nO total de mulheres foram {totMulheres} e muheres abaixo dos 20 anos foram {totMulherM20} ''')
