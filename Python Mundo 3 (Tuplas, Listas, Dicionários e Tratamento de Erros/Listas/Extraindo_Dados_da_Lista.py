listaNumeros = list()
totNum = 0

while True:
    listaNumeros.append(int(input("Digite um número")))
    totNum += 1
    resposta = input("Deseja Continuar?[S/N] ")
    while resposta.upper().strip()[0] not in 'NS':
        resposta = input("Digite uma opção válida [S/N]")

    if resposta.upper().strip()[0] == 'N':
        break


listaNumeros.sort(reverse=True)
print(listaNumeros)
print(f"O número total de elementos é {totNum}")
if 5 in listaNumeros:
    print(f"O número 5 está no indice {listaNumeros.index(5)}")
else:
    print("Não há número 5")