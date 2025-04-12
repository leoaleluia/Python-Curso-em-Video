from datetime import date
nome = input("Digite o nome do atleta").title()
anoNascimento = int(input("Digite o ano de nascimento do atleta"))
ano = date.today()
anoAtual = ano.year
idade = anoAtual - anoNascimento

if idade <= 9:
    print(f"{nome}, pertence à Categoria: Mirim")
elif idade <= 14:
    print(f"{nome}, pertence à Categoria: Infantil")
elif idade <= 19:
    print(f"{nome}, pertence à Categoria: Junior")
elif idade == 20:
    print(f"{nome}, pertence à Categoria: Sênior ")
else:
    print(f"{nome}, pertence  à Categoria: Master")
