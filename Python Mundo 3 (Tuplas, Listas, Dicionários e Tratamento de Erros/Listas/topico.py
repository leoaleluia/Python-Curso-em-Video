lista = [] #ou list()
iCont = numAmzd = 0

while True:
    numero = int(input("Digite um número: ")) 
    
    if len(lista) == 0 or numero > lista[-1]:
        lista.append(numero)
    else:
        while numero in lista: #Verifica se o número ja está na lista
            numero = int(input("Digite um número que não contenha  na lista: "))

        for c in range(len(lista)):
            if numero <= lista[c]:
                lista.insert(c, numero)
                break

        resposta = input("Deseja Continuar? [S/N]")

        while resposta.upper().strip()[0] not in "SN":
            resposta = input("Digite uma opção valoda [S/N]: ")

        if resposta.upper().strip()[0] == 'N':
            break

print(lista)