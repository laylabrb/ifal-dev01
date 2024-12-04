def exibir_informacoes_estudantes(estudantes):
   
    for estudante in estudantes:
        print(estudante["nome"], estudante["casa"], estudante["patrono"], sep=", ")

estudantes = [
    {"nome": "Hermione", "casa": "Grifinória", "patrono": "Lontra"},
    {"nome": "Harry", "casa": "Grifinória", "patrono": "Veado"},
    {"nome": "Rony", "casa": "Grifinória", "patrono": "Jack Russell terrier"},
    {"nome": "Draco", "casa": "Sonserina", "patrono": None},
]

# Chamada da função
exibir_informacoes_estudantes(estudantes)
