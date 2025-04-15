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
    while parcelasSolicitada > porcentagemSal:
        mesesSugerido += 1
        parcelasSolicitada = casa / mesesSugerido
        parcelaAtual = parcelasSolicitada
    
    print(f'Não podemos oferecer o emprestimo com sua opção de parcela sugerida com parcelas de {parcelasSolicitada} durante {meses}, mas podemos te oferecer com essas parcelas de {parcelaAtual} durante {mesesSugerido} ')