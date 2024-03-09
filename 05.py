palavra = input("Digite a palavra")
invertida = ""

TAM = len(palavra) -1

for i in range(TAM, -1, -1):
    invertida += palavra[i]

print('Palavra Invertida: ', invertida)
