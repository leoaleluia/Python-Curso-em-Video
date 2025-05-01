teste = list()
teste.append('leo')
teste.append(26)
galera = list()
galera.append(teste[:]) #Usamos o fatiamento de string para fazer uma cópia da lista, assim, nós evitamos a exclusão de itens ao adiocnarmos algo
teste[0] = ('Maria')
teste[1] = (25)
galera.append(teste[:]) #usamos o fatiamento para evitar que a lista se altere automaticamente, pois, o append cria uma relação com a lista, caso mudarmos uma, altera a outra, independente da lógica

print(galera)