nome = input('Digite seu nome: ').title()
print(f'O nome em maiuculo {nome.upper()}')
print(f'O nome com todas letras minusculas {nome.lower()}')
print(f'O tamanho total do nome é {len(nome.strip())}')#Mostra o tamanho do nome sem espaços
lista = nome.split()#Divide os nomes e insere em uma lista  
print(f'O tamanho do primeiro nome é {len(lista[0])}')
print('O seu primeito tem o tamanho de  {}'.format(nome.find(' ')))