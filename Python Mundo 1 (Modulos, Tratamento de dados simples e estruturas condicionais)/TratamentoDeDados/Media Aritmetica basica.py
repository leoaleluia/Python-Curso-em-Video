#faça um programa que leia duas notas de um aluno e mostre sua média

nome = input('Qual o nome do aluno? ').title()
nota1 = int(input(f'Digite a primeira nota do aluno {nome} '))
nota2 = int(input(f'Digite a segunda nota do aluno {nome} '))
media = (nota1 + nota2) / 2
print(f'O aluno {nome} obteve uma media de {media}')