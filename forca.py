import random

palavras=["janela", "laranja", "caminhão"]
palavra=(random.choice(palavras))
print(palavra)

print("Bem vindo ao jogo da forca!")
chute = input("Diga uma letra: ").lower()
print(chute)

for letra in palavra:
    if letra == chute:
        print("Certissimo")
    else:
        print("nao")