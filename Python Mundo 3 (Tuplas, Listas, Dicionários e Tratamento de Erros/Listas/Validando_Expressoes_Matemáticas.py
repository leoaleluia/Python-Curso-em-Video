expressao = list ()

while True:
    expressao = input("Digite a expressão: ")
    res = input("Deseja continuar? ")
    if res.upper().strip()[0] == 'N':
        break

parentesesD = expressao.count('(')
parentesesE = expressao.count(')')

if parentesesD == parentesesE:
    print("Expressão correta")
else:
    print("Expressão errada")
