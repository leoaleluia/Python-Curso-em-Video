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
lista.insert(0, 5) #Insira na posição 0 o número 5, o indice do númeo 4 passa a ser 1 e o do 11 passa a ser 2
del lista[1] #elimina o valor do indice 1
lista.pop() #elimina o ultimo ítem, mas podemos passar um indice como parâmetro
lanche.remove('11') #nesse caso colocamos o valor do indice, o que ele armazena.

