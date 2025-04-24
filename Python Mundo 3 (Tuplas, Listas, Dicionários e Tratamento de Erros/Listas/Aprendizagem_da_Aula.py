#Alguns comandos usados em listas

lanche = ['suco', 'pao']
lanche.append('bolacha') #adciona algo na lista. (apenas no final)
lanche.insert(0, 'refrigerante') #adciona algum elemento em um local determinado. nesse exemplo, adicionou refrigerante na posição 0, criando assim, 4 elementos na lista, e o suco passou a ser o indice 1
#dellanche[3]
#lanche.pop(3) normalmente elemina o ultimento, mas podemos usar o parametro
#lanche.remove(''pao') passamos conteudo 
#após eliminar os conteúdos a lista se refaz
#criando uma lista com o ranges:
lista = list(range(4, 11)) #criou uma lista no range de 4 ate 11, lembrando que o ultimo número é ignorado, podemos criar listas com inteiros de maneira didática
lista.sort() #ordena a lista
lista.sort(reverse=True) #ordena a lista de maneira reversa
print(lista)
print(lanche)