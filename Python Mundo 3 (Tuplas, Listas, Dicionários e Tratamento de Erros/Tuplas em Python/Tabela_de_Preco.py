tabelaProduto = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderdo', 15,'Estojo', 25, 'Transferidor', 4.20, 'Compasso',  9.99, 'Mochila', 128, 'Canetas', 22.20, 'Livro', 34.98) 

print(f"{"Lista De preço":^20}") #ao usar essa fString, podemos colocar uma string em uma chave e manipular a mesma
for pos in range(len(tabelaProduto)): #dessa maneira o pos assume o valor de indice puro, ou seja, numero inteiro
    if pos % 2 == 0:
        print(f"{tabelaProduto[pos]:.<20}", end='')#alinhou a esqueca com 20 espaços
    else:
        print(f"R${tabelaProduto[pos]:.2f}")

