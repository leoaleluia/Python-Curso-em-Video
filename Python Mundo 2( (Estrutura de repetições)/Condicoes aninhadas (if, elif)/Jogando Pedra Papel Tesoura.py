#faça um programa que permita ao usuario interagir com o a maquina em um jogo de pedra, papel, tesoura
import random

lista = ['pedra', 'papel', 'tesoura']
maquina = random.choice(lista)
usuario = input("Escolha pedra, papel ou tesoura: ").lower().strip()

if usuario == 'pedra' and maquina == 'tesoura':
    print("usuario ganhou")
elif usuario == 'papel' and maquina == 'pedra':
    print("usuario ganhou")
elif usuario == 'tesoura' and maquina == 'papel':
    print("Usuário ganhou")

elif maquina == 'pedra' and usuario== 'tesoura':
    print("A maquina ganhou: ")
elif maquina == 'papel' and usuario == 'pedra':
    print("A maquina venceu")
elif maquina == 'tesoura' and usuario == 'papel':
    print("A maquina venceu")
else:
    if maquina == usuario:
        print("temos um empate")

print(f"a maquina escolheu {maquina}  e você escolheu {usuario}")