#faça um programa que mostre o primeiro e o ultimo nome de uma pessoa

nome = input('Digite seu nome: ').strip().title()
listaNome = nome.split()
print(f'o primeiro nome é {listaNome[0]}')
print(f'O ultimo nome é {listaNome[len(listaNome) - 1]}') 
print(f'o ultimo nome é.... {listaNome[-1]}')
"""nome[len(listaNome)] - 1 : o que será verificado é o len(listaNome), 
ou seja,  aparece o tamanho da llista nome que é 3, porém a lógica conta ate 2, logo
diminuimospor 1"""
