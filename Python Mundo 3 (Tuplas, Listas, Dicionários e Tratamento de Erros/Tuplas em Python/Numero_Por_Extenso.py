numeros = ('zero', 'um', 'dois','três', 'quatro', 'Cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
num = int(input("Digite um número no interválo de 0 ate 20"))
while num > 20:
    num = int(input("Digite um número dentro do intervalo"))
print(f"você procurou o número {numeros[num]}")