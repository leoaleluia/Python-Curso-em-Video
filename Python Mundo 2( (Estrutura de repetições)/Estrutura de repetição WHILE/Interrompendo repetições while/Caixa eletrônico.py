totNotas1 = totNotas5 = totNotas10 = totNotas20 = totNotas2 = totNotas50 = 0
while True:
    valorSaque = int(input("Digite o valor do saque: "))
    valorSaque2 = valorSaque
    while valorSaque >= 50:
        valorSaque -= 50
        totNotas50 += 1
    while valorSaque >= 20:
        valorSaque -= 20
        totNotas20 += 1
    while valorSaque >= 10:
        valorSaque -= 10
        totNotas10 += 1
    while valorSaque >= 5:
        valorSaque -= 5
        totNotas5 += 1
    while valorSaque >= 2:
        valorSaque -= 2
        totNotas2 += 1
    while valorSaque == 1:
        valorSaque -= 1
        totNotas1 +=1

    if valorSaque == 0:
        break

print(f"O total sacado foi {valorSaque2}\nNotas de 50 {totNotas50}\nNotas de 20 {totNotas20}\nNotas de 10 {totNotas10}\nNotas de 5 {totNotas5}\nNotas de 2 {totNotas2}\nNotas de 1 {totNotas1}")