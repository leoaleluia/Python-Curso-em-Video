#Construa um programa que faça uma contagem regressiva com um intervalo de 1 segundo entre a contagem
from time import sleep

for c in range (10, 0, -1):
    print(c)
    sleep(1)
print("Fogos para todo lado")