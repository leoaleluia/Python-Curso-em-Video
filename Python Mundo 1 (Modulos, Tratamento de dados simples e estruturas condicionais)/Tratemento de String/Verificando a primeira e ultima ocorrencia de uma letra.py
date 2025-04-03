#faça um programa que mostre a primeira e ultima orrencia de uma letra
nome = input('Digite seu nome')
print(f'a quantidade de letras A é {nome.count('A')}')
print(f'A primeira aparição dela é: {nome.find('A') + 1}')
print(f'E a ultima é {nome.rfind('A') + 1}')