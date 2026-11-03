contagem = {}

with open ("auth.log") as arquivo:
    for linha in arquivo:
        if "Failed password" in linha:
            palavras = linha.split()
            posicao = palavras.index("from")
            ip = palavras[posicao + 1]
            contagem[ip] = contagem.get(ip, 0) + 1

for ip, total in sorted(contagem.items(), key=lambda item: item[1], reverse=True):
    print(ip, total)