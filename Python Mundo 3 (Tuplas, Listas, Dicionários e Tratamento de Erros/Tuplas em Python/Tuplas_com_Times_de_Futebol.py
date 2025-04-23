classificacao = ('Botafogo', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Internacional', 'São Paulo', 'Corinthians', 'Bahia', 'Cruzeiro', 'Vasco', 'Vitória', 'Atletico- Mg', 'Fluminense', 'Grêmio', 'Juventude', 'Red Bull Bragantino', 'Athletico-PR', 'Criciúma', 'Atlético-GO', 'Cuiabá')

print(f"Os cinco primeiros colocados são {classificacao[:5]}")
for c in range(0, len(classificacao) - 15):
    print(f"{c + 1}º {classificacao[c]}")


print(f"Os ultimos 4 Colocados são {classificacao[16:]}")
for c in range(16, len(classificacao)):
    print(f"{c + 1}º {classificacao[c]}")

print(f"A classificação em ordem alfabetica é {sorted(classificacao)}")

print(f"O Vitória está na posição {classificacao.index('Vitória') + 1}")