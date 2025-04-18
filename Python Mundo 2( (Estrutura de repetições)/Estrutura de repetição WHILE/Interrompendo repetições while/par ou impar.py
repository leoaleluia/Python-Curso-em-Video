from random import randint
cont = numPc = num = tentativas = vencedor = 0
res = ' '

while True:
    if cont == 0:
        print("Vamos jogar um jogo de par ou impar")
        num = int(input("Digite um número "))
        numPc = randint(0, 10)
        vencedor = num + numPc
        res = input("Desejesa par ou impar [P/I]").upper().strip()[0]
        if res == 'P'and vencedor % 2 == 0:
            cont += 1
            print(f"Você ganhou, seus números foram {num} e a máquina {numPc}")
            print(f"O total de tentativas foram {cont}")
        elif res == 'I' and vencedor % 2 == 1:
            cont += 1
            print(f"Você ganhou, seus números foram {num}  e a máquina {numPc}")
            print(f"O total de tentativas foram {cont}")
        else:
            print(f"Você perdeu, seus números foram {num} e a máquina {numPc}")
            break
    num = int(input("Digite um número: "))
    numPc = randint(0, 10)
    vencedor = num + numPc
    res = input("Deseja par ou impar [P/I]: ").upper().strip()[0]
    if res == 'P' and vencedor % 2 == 0:
        cont += 1
        print(f"VocÊ ganhou, seus números foram {num} e a máquina {numPc}")
        print(f"O total de tentativas foram {cont}")
    elif res == 'I' and vencedor % 2 == 1:
        cont += 1
        print(f"Você ganhou, seus números foram {num} e a máquina {numPc}")
        print(f"O total de tantativas foram {cont}")
    else:
        print(f"Você perdeu, seus números foram {num} e a maquina {numPc}")
        break