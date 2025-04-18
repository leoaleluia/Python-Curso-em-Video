#Crie um número que leia vários números inteiros. o programa irá encerrar quando o usuário digitar 999. mostre o total dos númeos digitados e sua soma
controle = totNum = somaTot = 0
while controle != 999:
    controle = int(input("Digite um número: "))
    if controle != 999:
        totNum += 1
        somaTot += controle
    
print(f"O total de números digitados foram {totNum}  e a soma de todos eles é {somaTot}")
