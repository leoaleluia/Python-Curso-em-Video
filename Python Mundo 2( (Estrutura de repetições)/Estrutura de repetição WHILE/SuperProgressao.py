numero1 = int(input("Digite um número: "))
numero1Rsv = numero1
razao = int(input("Digite a razão: "))
decimoTermo = numero1 + (10 - 1) * razao
while numero1 < decimoTermo:
    numero1 += razao
    print(numero1, end=' -> ')
    if numero1 == decimoTermo:
        res = int(input("Deseja verificar mais termos? [1/0] 1 para ok e 0 para encerrar"))
        while res != 1 and res != 0:
            res = input("Digite uma opção válida")
        if res == 1: 
            termos = int(input("Quantos termos a mais deseja vê? "))
            decimoTermo = numero1 + (10 - termos) * razao
            while numero1Rsv < decimoTermo:
                numero1Rsv += razao
                print(numero1Rsv, end=' -> ')
            break
        else:
            print("Obrigado")