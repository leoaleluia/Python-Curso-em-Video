#faça um programa que calcule as despesas de um carro alugado. Diária R$ 60.00, km R$ 0.15 POR km
nome = input('Digite o seu nome: ')
dias = int(input('por quantos dias você usará esse carro? '))

km = int(input('Digite quantos km você percorreu nesse período (R$ 0.15 POR KM RODADO)'))

despesasTot = ((dias * 60) + (km * 0.15))

print(f'{nome}, o total de dias de uso foi de {dias} com {km} Km percorridos, totalizando um valor de R$ {despesasTot}')

