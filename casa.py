def verificar_casa_personagem(nome):
    if nome == "Harry Potter":
        return "Grifinória"
    elif nome == "Hermione Granger":
        return "Grifinória"
    elif nome == "Rony Weasley":
        return "Grifinória"
    elif nome == "Draco Malfoy":
        return "Sonserina"
    elif nome == "Luna Lovegood":
        return "Corvinal"
    elif nome == "Cedric Diggory":
        return "Lufa-Lufa"
    else:
        return "Personagem não encontrado"


def main():
    nome = input("Qual seu nome? ")
    casa = verificar_casa_personagem(nome)
    print(casa)


main()

   