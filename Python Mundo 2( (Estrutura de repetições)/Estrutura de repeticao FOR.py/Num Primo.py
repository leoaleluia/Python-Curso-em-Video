numero = int(input("Digite um número para saber se é primo: "))
primo = 0

for c in range(2, numero + 1):
    if numero % c == 0:
        primo += 1

if primo > 1:
    print(f"o número  {numero} não é primo ")
else:
    print(f"o número {numero}  é primo ")    