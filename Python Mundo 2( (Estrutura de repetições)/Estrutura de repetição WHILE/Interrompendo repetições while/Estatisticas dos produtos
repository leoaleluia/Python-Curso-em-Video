maisCaro = totMaisde1000 = maisBarato = totalCompras = 0
nomeMaisBarato = ''
nomeMaisBarato = ''
while True:
    produto = input("Digite o nome do produto: ").title()
    valor = float(input("Digite o valor do produto"))
    totalCompras += valor
    
    if valor > 1000:
        totMaisde1000 += 1
    if valor > maisCaro:
        maisCaro = valor
        nomeMaiscaro = produto
    if maisBarato == 0:
        maisBarato = valor
        nomeMaisBarato = produto
    elif valor < maisBarato:
        maisBarato = valor
        nomeMaisBarato = produto
    res = input("Deseja continuar? [S/N]").upper().strip()[0]
    while res not in 'SN':
        res = int(input("Digite uma opção válida [S/N]:  ")).upper().strip()[0]
    if res == 'N':
        break
print(f"O total dessa compra foi de R$ {totalCompras}\n o produto mais caro é R$ {maisCaro}  e seu nome é {nomeMaiscaro}")
print(f"O produto mais barato é R$ {maisBarato} e o nome é {nomeMaisBarato}")
print(f"Foram comprados {totMaisde1000} itens acima de R$ 1000.00")