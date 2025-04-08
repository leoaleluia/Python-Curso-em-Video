def lenn(palavra):
    funLen = 0
    espacos = palavra.count(' ')
    for c in palavra:
        funLen += 1
    return (f'o tamanho da palavra é {funLen - espacos} ')

frase = str(input('Digite uma frase ou nome')).strip()
print(f'o tamanho sem a função é {len(frase)}')
tamFrase = print(lenn(frase))
    
