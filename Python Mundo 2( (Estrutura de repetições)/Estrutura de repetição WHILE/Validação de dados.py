#Faça um programa que leia o Sexo de uma pessoa, caso esteja errado, solicite o valor correto

sexo = str(input("Digite seu sexo [M] ou [F]")).upper()
while sexo != 'M' or sexo != 'F':
    sexo = input("Digite um valor válido [M] ou [F]").upper()

print(f"Seu sexo é {sexo}")