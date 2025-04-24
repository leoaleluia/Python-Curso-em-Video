numeros = (int(input("Digite um númeo")), int(input("Digite o segundo número")), int(input("Digite o terceio número")), int(input("Digite o quarto número")))

print(f"o número 9 apaececeu {numeros.count(9)} vez")
for c in numeros:
    if c % 2 == 0:
        print(f"O número {c} é par", end='')
if 3 in numeros:
    print(f"o número 3 esta na posição {numeros.index(3)}")
else:
    print("o número 3 não foi digitado em nenhuma tupla")