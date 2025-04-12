digito1 = int(input("Digite o primeiro termo da PA: "))
progressao = int(input("Digite a progressão (razao)"))
decimoTermo = digito1 + (10 - 1) * progressao
print(decimoTermo)

for c in range (digito1, decimoTermo + progressao, progressao):
    print(f"{c}", end=' > ')
    