lista = [] #or list()
for c in range(0, 5):
    lista.append(int(input("Dgite um número: ")))


print(f"o maior número é {max(lista)} e seu indíce é {lista.index(max(lista))}")
print(f"o menor número é {min(lista)} e o seu indice é {lista.index(min(lista))}")

#or

maior = menor = lista[0]
inidiceMaior = indiceMenor = 0
for idx, valor in enumerate(lista):
    if valor > maior:
        maior = valor
        indiceMaior = idx
    if valor < menor:
        menor = valor
        indiceMenor = idx

print(f"O maior valor é {maior} e sua posição é {indiceMaior}  e o menor {menor} e sua posição é {indiceMenor} ")
    