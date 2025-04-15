controle = True

numMenor = numMaior =  totNum = posNumMaior = posNumMenor = contNum = 0
while controle == True:
    numero = int(input("Digite um número"))
    if totNum == 0:
        numMenor = numero
        if numero > numMaior:
            numMaior = numero
            posNumMaior = totNum + 1
        if numero < numMenor:
            numMenor = numero
            posNumMaior = totNum + 1
    else:
        if numero > numMaior:
            numMaior = numero
            posNumMaior = totNum + 1

        if numero < numMenor:
            numMenor = numero
            posNumMenor = totNum + 1
    totNum += 1
    contNum += numero
    res = input("Deseja Continuar: Sim ou Não: ").upper().strip()[0]
    while res not in "SsNn":
        res = input("Digite uma opção válida: Sim ou Não").upper().strip()[0]
    if res == 'S':
        controle = True
    else:
        controle = False

mediaNum = contNum // totNum
print(f"O total de números digitados foram {totNum}\nA media foi {mediaNum}\nO maior número foi digitado pela {posNumMaior} vez  e o menor foi digtado pela {posNumMenor} vez.\nSão eles respectivamente {numMaior} e {numMenor}")

    
