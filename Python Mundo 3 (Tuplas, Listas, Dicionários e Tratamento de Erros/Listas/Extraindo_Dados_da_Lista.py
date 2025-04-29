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


listaReverse = listaNumeros.sort(reverse=True)
print(listaReverse)