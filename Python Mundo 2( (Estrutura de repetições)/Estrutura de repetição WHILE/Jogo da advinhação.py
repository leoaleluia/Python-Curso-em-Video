#faça um programa que gere um número entre 0 e 10. O usuário tenterá acertar o número gerado pelo programa. Além disso, o programa deve retornar quantos palpites foram necessários para acertar

from random import randint

totTentativas = 0
numPc = randint(0, 10)
numUsuario = int(input("Digite seu número"))
if numUsuario == numPc:
    print(f"Parabéns vc acertou de primeira, seu número é {numUsuario} e o da maquina é {numPc} ")

while numUsuario != numPc:
    totTentativas += 1
    numUsuario = int(input("Errou! Tente Novamente"))

print(f"Você acertou, seu número é {numUsuario} e o da maquina é {numPc}\nTotal de {totTentativas}")