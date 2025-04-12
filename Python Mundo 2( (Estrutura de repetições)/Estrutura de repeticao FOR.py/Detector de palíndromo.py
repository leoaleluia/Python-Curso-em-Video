#faça um programa que detecte uma palavra palíndroma 
frase = input("Digite uma frase: ")
frase2 = "".join(frase.split())
controle = len(frase2)
contador = 0
controle2 = 0
for c in range(len(frase2)- 1, -1, -1):
   if frase2[c] == frase2[contador]:
      controle2 += 1
   contador += 1
   
   

print(f"{controle2} contador, controle{controle}")
if controle == controle2:
   print("Palíndromo")
else:
   print("não é um palíndromo")