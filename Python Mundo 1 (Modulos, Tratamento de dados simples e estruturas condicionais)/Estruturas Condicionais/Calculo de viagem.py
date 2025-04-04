"""faça um programa que calcule o preço da viagem seguindo os seguintes parâmetros: R$ 0.50 até 200Km, acima de 200Km R$ 0.45 """

quilometros = int(input('Digite o total de km: '))

if quilometros <= 200:
    valorPassagem = 0.50 * quilometros
else:
    valorPassagem = 0.45 * quilometros

print(f'O valor total da passagem é {valorPassagem}')