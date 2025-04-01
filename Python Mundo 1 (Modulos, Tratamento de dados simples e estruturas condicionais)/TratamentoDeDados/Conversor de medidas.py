#faça um programa que leia um valor em metros e mostre em Centimetros e milimetros

metro = int(input('Digite o valor em metros'))
centimetros = metro * 100
milimetros = metro * 1000
print(f'{metro} metros equivalem à {centimetros} centimetros e {milimetros} milimetros')