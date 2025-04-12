from colorama import Fore, Style
nome =input("Qual o nome do aaluno? ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2

if media < 5:
    print(Fore.RED + f"Você foi reprovado com media {media}!")
elif media >= 5 and media <= 6.9:
    print(Fore.YELLOW + f"Você está na recuperação com media {media}")
else:
    print(Fore.GREEN + f"Parabéns, {nome}, você foi aprovado com media {media}! ")

print(Style.RESET_ALL)