tabelaProduto = ('Lápis', 'Borracha', 'Caderdo', 'Estojo','Transferidor', 'Compasso', 'Mochila',  'Canetas', 'Livro',)
tabelaPreco = ( 1.75, 2.00, 15.00, 25.00, 4.20, 9.99, 128.32, 22.20, 34.98)

for c in range(len(tabelaProduto)):
    print(f"{tabelaProduto[c]}..........R${tabelaPreco[c]}")

