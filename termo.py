from random import randint
import os
import termo_defs

os.system("cls") or None

termo_defs.title(10)

underlines = ["_", "_", "_", "_", "_"]

termo_defs.underlines(underlines)

termo_defs.line()
termo_defs.line()

sorteio = randint(1, 1000)
palavra_sorteada = ""

with open("palavras.txt", "r", encoding = "utf-8") as arquivo:
    banco_de_palavras = arquivo.readlines()

for pos, palavra in enumerate(banco_de_palavras):
    if pos == sorteio:
        palavra_sorteada = palavra

letras_resposta = []

for letra in palavra_sorteada:
    if letra == "á" or letra == "ã" or letra == "à" or letra == "â":
        letra = "a"
    elif letra == "é" or letra == "ê":
        letra = "e"
    elif letra == "ó" or letra == "ô":
        letra = "o"
    elif letra == "ü" or letra == "ú":
        letra = "u"
    elif letra == "í" or letra == "î":
        letra = "i"
    letras_resposta.append(letra)
letras_resposta.pop()

letras_resposta2 = letras_resposta[:]

while True:
    while True:
        palpite = input("Digite uma palavra com no máximo 5 letras (sem acentos): ")
        palpite = palpite.strip()
        
        if letra == "á" or letra == "ã" or letra == "à" or letra == "â":
            letra = "a"
        elif letra == "é" or letra == "ê":
            letra = "e"
        elif letra == "ó" or letra == "ô":
            letra = "o"
        elif letra == "ü" or letra == "ú":
            letra = "u"
        if len(palpite) > 5 or len(palpite) < 5:
            print("Você digitou uma palavra inválida, por favor, tente novamente\n")
        else:
            break

    termo_defs.line()

    letras_palpite = []

    for letra in palpite:
        letras_palpite.append(letra)

    for pos, letra in enumerate(letras_palpite):
        if letra in letras_resposta:
            print(f"tem a letra {letra.upper()}", end=" e ")

            if letras_resposta.index(letra) == pos:
                print("está na posição certa")
                underlines[pos] = letra.upper()
                letras_resposta[letras_resposta.index(letra)] = "#"
            else:
                cont = 0
                for letter in letras_resposta:
                    if letter == letra:
                        cont += 1
                
                if cont == 2:
                    seccond = palavra_sorteada.find(letra, palavra_sorteada.find(letra) + 1)
                    underlines[seccond] = letra.upper()
                    letras_resposta[seccond] = "#"
                    print("está na posição certa")
                else:
                    print("está na posição errada")
            
        else:
            print(f"não tem a letra {letra.upper()}")

    termo_defs.line()
    termo_defs.underlines(underlines)
    termo_defs.line()

    if letras_palpite == letras_resposta2:
        print("\nVOCÊ ACERTOU A PALAVRA!")
        break
    else:
        print("\nVOCÊ ERROU A PALAVRA")
        letras_palpite = []
        letras_resposta = letras_resposta2[:]
