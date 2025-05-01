listaGeral = list()
listaPar = list()
listaImpar = list()

while True:
    num = int(input("Digite um número: "))
    listaGeral.append(num)
    resposta = input("Deseja continuar? ")
    if resposta.upper().strip()[0] == 'N':
        break

for c in listaGeral:
    if c % 2 == 0:
        listaPar.append(c)
    else:
        listaImpar.append(c)

print(listaImpar)
print(listaPar)
print(listaGeral)