numeros = list()
while True:
    num = int(input("Digite um número: "))
    
    while num in numeros:
        num = int(input(f"Digite um número que não tenha sido inserido na lista, confira: {numeros}"))

    numeros.append(num) #após verificar o num digitado, adiciona a variável num à lista
    resposta = input("Deseja continuar? [S/N]")

    while resposta.upper().strip()[0] not in 'SN':
        resposta = input("Digite uma opção válida. [S/N]").upper().strip()

    if resposta[0].upper().strip() == 'N':
        break

numeros.sort()#Oganiza em ordem crescente
print(numeros) 
