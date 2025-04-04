#Faça um programa que leia 3 números e diga qual o maior e o menor

numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite o segundo número: '))
numero3 = int(input('Digite o terceiro número: '))

if numero1 > numero2 and numero1 > numero2:
    Maior = numero1
else:
    if numero1 < numero2 and numero1 < numero3:
        Menor = numero1

if numero2 > numero1 and numero2 > numero3:
    Maior = numero2
else:
    if numero2 < numero1 and numero2 < numero3:
        Menor = numero2

if numero3 > numero2 and numero3 > numero1:
    Maior = numero3
else:
    if numero3 < numero1 and numero3 < numero2:
        Menor = numero3

print(f'O maior número é {Maior} e o menor é {Menor}')