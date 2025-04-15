
num = 0
somaTot = TotNum = 0
while num != 999:
    num = int(input("Digite um número: "))
    if num != 999:
        somaTot += num
        TotNum += 1
print(f"O total de números lidos foram {TotNum} e a soma de todos eles é {somaTot}")
