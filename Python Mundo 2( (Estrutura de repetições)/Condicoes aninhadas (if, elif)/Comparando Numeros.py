#faça um programa que leia dois números e mostre qual é o maior e se há valores iguais

valor1 = int(input("Digite um valor: "))
valor2 = int(input("Digite o segundo valor: "))

if valor1 > valor2:
    print(f'O valor {valor1} é maior')
elif valor2 > valor1:
    print(f"O valor {valor2} é maior")
else:
    if valor1 == valor2:
        print(f"Os valores {valor1} e {valor2} são iguais")