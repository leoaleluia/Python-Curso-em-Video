#faça um programa que aprove um emprestimo bancário. O valor das parcelas mensais não pode exceder 30% do salario do usuário
salario = int(input("Digite seu salário: "))
casa = int(input("Qual o valor da casa: "))
meses = int(input("Em quantos meses deseja pagar? "))
porcentagemSal = salario * 0.3
parcelasSolicitada = casa / meses

mesesSugerido = meses

if parcelasSolicitada <= porcentagemSal:
    print("Emprestimo Garantido")
    print(parcelasSolicitada)
else:
    parcelasSolicitada2 = parcelasSolicitada
    while parcelasSolicitada > porcentagemSal:
        mesesSugerido += 1
        parcelasSolicitada = casa / mesesSugerido
        parcelaAtual = parcelasSolicitada
    
    print(f'Não podemos oferecer o emprestimo com sua opção de parcela sugerida de R$ {parcelasSolicitada2} durante {meses} meses, mas podemos te oferecer com essas parcelas de R$ {parcelaAtual} durante {mesesSugerido} meses ')