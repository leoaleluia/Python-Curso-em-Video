#faça um algoritmo que leia um número real e mostre a parte inteira dele
from math import trunc
numero = float(input('Digite um número real'))
print('O número {} truncado é {}'.format(numero, trunc(numero)))
