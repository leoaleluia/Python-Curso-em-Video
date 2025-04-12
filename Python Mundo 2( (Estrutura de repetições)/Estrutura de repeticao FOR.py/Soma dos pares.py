#Escreva um programa que leia 6 números e mostre a soma dos pares
soma = 0
    
for c in range(1, 6 + 1):
    num = int(input("Digite um número"))
    if num % 2 == 0:
        soma += num

print(f"o valor final é: {soma}")