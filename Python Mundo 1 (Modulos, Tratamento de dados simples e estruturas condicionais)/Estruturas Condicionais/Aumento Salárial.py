Salario = float(input(f'Digite o seu salário: '))
if Salario >  1250.00:
    Aumento = Salario * 0.1
    NovoSalario = Salario + Aumento
else:
    Aumento = Salario * 0.15
    NovoSalario = Salario + Aumento

print(f'Seu Salario foi alterado de R$ {Salario:.2f} para R$ {NovoSalario:.2f}')