tuplaPalavras = ('Aprender', 'Programar', 'Linguagem', 'Python', 'Curso', 'Gratis', 'Estudar', 'Praticar','Praticar', 'Trabalhar', 'Mercado', 'Programador', 'Futuro')

for palavra in tuplaPalavras:
    print(f"\nA palavra {palavra} contem as vogais: ", end=' ')
    if 'a' in palavra.lower():
        print("a", end='')
    if 'e' in palavra.lower():
        print("e", end='')
    if 'i' in palavra.lower():
        print("i", end='')
    if 'o' in palavra.lower():
        print("o", end='') 
    if 'u' in palavra.lower():
        print("u", end='')   