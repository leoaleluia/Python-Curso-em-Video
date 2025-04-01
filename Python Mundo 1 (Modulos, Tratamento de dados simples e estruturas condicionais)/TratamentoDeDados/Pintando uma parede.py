#faça um programa que calcure a área de uma pare e mostre a quantidade de litros de tinta necessário para pintá-la
altura = float(input('Qual a altura da parede? '))
largura = float(input('Qual a largura da parede? '))
area = largura * altura
tinta  = 2 * area #um litro de tinta pinta 2m² de parede.

print(f'O total de tinta será {tinta}')