#faça um programa que leia o nome de uma cidade e diga se ela começa com santo

cidade = input('Digite o nome da cidade').title()
nomesSeparados = cidade.split()
print('Santo' in nomesSeparados[0])
