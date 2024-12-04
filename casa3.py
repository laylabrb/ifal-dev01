def verificar_casa_personagem(nome):
    match nome:
        case "Harry Potter":
            return "Grifinória"
        case "Hermione Granger":
            return "Grifinória"
        case "Rony Weasley":
            return "Grifinória"
        case "Draco Malfoy":
            return "Sonserina"
        case "Luna Lovegood":
            return "Corvinal"
        case "Cedric Diggory":
            return "Lufa-Lufa"
        case _:
            return "Personagem não encontrado"


def main():
    nome = input("Qual seu nome? ")
    casa = verificar_casa_personagem(nome)
    print(casa)


main()
