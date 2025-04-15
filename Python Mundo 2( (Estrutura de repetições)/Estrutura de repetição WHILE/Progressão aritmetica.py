numero1 = int(input("Digite o número: "))
razao = int(input("Digite a razão "))
decimoTermo = numero1 + (10 - 1) * razao
while numero1 < decimoTermo:
    numero1 += razao
    print(numero1, end=' - >')