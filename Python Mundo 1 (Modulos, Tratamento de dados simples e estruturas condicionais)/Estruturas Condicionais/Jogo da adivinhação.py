#faça um programa que permita o computador pensar em um número para o usuário tentar acertar.
import random
numComputador = random.randint(1, 5)
numUsuario = int(input('qual o seu palpite (Digite um número de 1 a 5): '))
if numUsuario == numComputador:
    print(f'Parabéns, você acertou o número {numComputador}')
else:
    print(f'Você errou o número: numPc: {numComputador}')