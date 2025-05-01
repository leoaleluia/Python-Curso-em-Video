listaNumeros = list()
totNum = 0

while True:
    numero = int(input("Digite um número: "))
    listaNumeros.append(numero)
    totNum += 1
    resposta = input("Deseja Continuar?[S/N] ")
    while resposta.upper().strip()[0] not in 'NS':
        resposta = input("Digite uma opção válida [S/N]")

    
    if resposta.upper().strip()[0] == 'N':
        break


if 5 in listaNumeros:
    print(f"O número 5 está no indice {listaNumeros.index(5)}")
else:
    print("Não há número 5")
listaNumeros.sort(reverse=True)
print(listaNumeros)