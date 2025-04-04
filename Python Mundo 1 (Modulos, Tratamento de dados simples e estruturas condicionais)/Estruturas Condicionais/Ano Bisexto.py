ano = int(input('Digite o ano para saber se é bisexto: '))
if ano % 4 == 0 and (ano % 100 == 0 and ano % 400 == 0):
    print (f'O ano {ano} é bisexto')
else:
    print(f'O ano {ano} não é bisexto')