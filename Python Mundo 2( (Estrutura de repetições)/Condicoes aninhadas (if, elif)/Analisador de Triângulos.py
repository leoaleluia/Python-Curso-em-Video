#faça um programa que leia 3 retas e mostre qual Triângulo é formado

lado1 = int(input("Digite o primeiro lado: "))
lado2 = int(input("Digite o segundo lado: "))
lado3 = int(input("Digite o terceiro lado: "))

if (lado1 + lado2) > lado3 and (lado2 + lado3) > lado1 and (lado3 + lado1) > lado2:
    if lado1 == lado2 == lado3: #lado1 == lado2 and lado2 == lado3
        print("Triangulo equilátero")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Triangulo Isósceles")
    else:
        print("Triangulo Escaleno")
else:
    print("Não pode ser feito um triangulo")