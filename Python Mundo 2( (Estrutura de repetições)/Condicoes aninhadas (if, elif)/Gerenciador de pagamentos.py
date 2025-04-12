produto = float(input("Digite o valor do produto"))
pagamento = int(input("""Digite 1 para pagamento avista com 10% de desconto\n 2 para pagamento avist no cartão 5% de desconto\n 3 para dividir em duas vezes\n 4 para dividir em 3 vezes ou mais com 20% de juros"""))

if pagamento == 1:
    precoAtual = produto * 0.1
    precoAtual = produto - precoAtual
    print(f"o produto sofreu um desconto de 10%. Preço atual R$ {produto}, preço após o desconto  R$ {precoAtual}")
elif pagamento == 2:
    precoAtual = produto * 0.05
    precoAtual = produto - precoAtual
    print(f"O produto sofreu um desconto de 5%. Preço Atual R$ {produto}, preço após o desconto R$ {precoAtual}")
elif pagamento == 3:
    precoAtual = produto / 2
    print(f"O produro será pago em duas parcelas de R$ {precoAtual}")
else:
    if pagamento == 4:
        precoAtual = produto * 0.2
        precoAtual += produto
        parcelas = precoAtual / 3
        print(f"o produto sofreu um acrescimo de 5% devido ao número de parcelas. Preço atual R$ {produto} preço apos o acrescimo R$ {precoAtual}.\n Será em 3 vezes com parcelas de {parcelas}")