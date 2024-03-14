import random

palavras = ["Carne", "Frango", "Arroz", "Tomate", "Queijo", "Leite", "Batata", "Cenoura"]
palavra = random.choice(palavras).lower()

letras_adivinhadas = ['_' for _ in palavra]

tentativas = 0

limite_tentativas = 7

while tentativas < limite_tentativas:
    print(' '.join(letras_adivinhadas))
    letra = input("Adivinhe uma letra: ").lower()

    if letra in palavra:
        for i in range(len(palavra)):
            if palavra[i] == letra:
                letras_adivinhadas[i] = letra
    else:
        tentativas += 1

    if '_' not in letras_adivinhadas:
        print("Parabéns, você ganhou! A palavra era " + palavra)
        break
else:
    print("Você perdeu! A palavra era " + palavra)