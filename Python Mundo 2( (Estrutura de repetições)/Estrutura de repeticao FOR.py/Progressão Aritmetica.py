digito1 = int(input("Digite o primeiro termo da PA: "))
digito2 = int(input("Digite o segundo termo da PA"))
progressao = digito2 - digito1

for c in range (1, 11):
    digito2 += progressao
    print(f"{c}º termo da PA {digito2}")