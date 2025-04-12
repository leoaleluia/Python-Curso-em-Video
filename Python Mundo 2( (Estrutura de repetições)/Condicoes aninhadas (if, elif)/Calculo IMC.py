from colorama import Fore, Style
nome = str(input("Digite seu nome: "))
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / pow(altura, 2) 

if imc < 18.5:
    print(Fore.RED + f"{nome}, Está abaixo do peso com o imc de {imc:.2f}")
elif imc >= 18.5 and imc < 25.0:
    print(Fore.GREEN + f"{nome}, Está no peso ideal com o imc de {imc:.2f}")
elif imc >= 25.0 and imc < 30:
    print(Fore.YELLOW + f"{nome}, Está com sobre pesoa com o imc de {imc:.2f}")
elif imc >= 30 and imc < 40:
    print(Fore.RED + f"{nome}, Está com obesidade com o imc de {imc:.2f}")
else:
    print(Fore.RED + f"{nome}, Está com obesidade morbida com o imc de {imc}")

print(Style.RESET_ALL)
