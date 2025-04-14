operacao = 0
num1 = int(input("Digite um número"))
num2 = int(input("Digite o segundo número"))
res = input("Deseja fazer algum operção com esses números? [S/N] ").upper()
while res != 'S' or res != 'N':
    if res == 'S':
        opcao = int(input("Escolha uma opção.\n[1] Ssomar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5]Sair do programa"))
        if opcao == 1:
            operacao = num1 + num2
            print(f"O resultado da soma dos números {num1} + {num2} é {operacao}")
            res = 'N'
        elif opcao == 2:
            operacao = num1 * num2
            print(f"O resultado da multiplicação dos números {num1} * {num2} é {operacao}")
            res = 'N'
        elif opcao == 3:
            if num1 > num2:
                operacao = num1
                print(f"O número 1 {operacao} é maior que o número 2 {num2}")
                res = 'N'
            elif num2 > num1:
                operacao = num2
                print(f"O número 2 {operacao} é maior que o numero 1 {num2}")
                res = 'N'
            else:
                print(f"Os números {num1} e {num2} são iguais")
                res = 'N'  
        elif opcao == 4:
            num1 = int(input("Digite o primeiro número"))
            num2 = int(input("Digite o segundo número"))
            res = 'S'
        else:
            if opcao == 5:
                res = input("Deseja realmente sair do programa? [S/N]").upper
                if res == 'S':
                    print("Programa encerrado")
                    break 
    else:
        if res == 'N':
            print("Programa encerrado")
            break
        else:
            while res != 'S' and res != 'N':
                res = input("Digite um valor válido").upper()
