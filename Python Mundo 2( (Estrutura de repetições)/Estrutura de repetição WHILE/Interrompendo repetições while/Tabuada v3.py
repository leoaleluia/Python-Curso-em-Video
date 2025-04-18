#faça um programa que leia um número  e mostre a tabuada  o programa só será interrompido quando ler um número negativo
num = 1
mult = 0
while num > 0:
    num = int(input("Digite um númeo para saber a tabuada: "))
    if num > 0:
        while mult < 10:
            mult += 1
            print(f"{num} x {mult} = {num * mult}")
    
print("Programa encerrado")
