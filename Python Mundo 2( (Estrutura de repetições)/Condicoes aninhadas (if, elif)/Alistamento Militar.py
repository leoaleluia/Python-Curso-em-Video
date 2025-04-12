from datetime import date

nome = input("Digite seu nome: ")
anoNasc = int(input("Digite o ano de nascimento"))
ano = date.today()
anoAtual = ano.year
idade = anoAtual - anoNasc

if idade == 18:
    print(f"{nome}, já está na hora de se alistar as Forças Armadas ")
elif idade > 18:
    atrasoEmAno = idade - 18
    atrasoEmMeses = atrasoEmAno * 12
    print(f"{nome}, você está atrasado para o alistamento, pois ja se passaram {atrasoEmMeses} meses ou {atrasoEmAno} anos.")
else:
    tempoParaAlistar = 18 - idade
    tempoParaAlistarMeses = tempoParaAlistar * 12
    print(f"Seu período de alistamento ainda não chegoum, faltam {tempoParaAlistarMeses} meses ou {tempoParaAlistar} anos ")
