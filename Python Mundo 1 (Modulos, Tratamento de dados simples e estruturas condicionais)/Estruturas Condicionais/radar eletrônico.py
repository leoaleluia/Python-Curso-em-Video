velocidadeCar = int(input('Qual a velocidade do carro'))
if velocidadeCar >= 80:
    print('Você foi multado')
    if velocidadeCar == 80:
        multa = 7
        print(f'O valor da sua multa é R$ {multa}.00')
    else:
        multa = ((velocidadeCar - 80) * 7) + 7
        print(f'O valor da sua multa é R$ {multa}.00')
else:
    print('Não houve multa')