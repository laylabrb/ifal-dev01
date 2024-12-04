def exibir_estudantes_com_casas(estudantes):
   
    for estudante, casa in estudantes.lower():
        print(estudante, casa, sep=", ")


estudantes = {
    "Hermione": "Grifinória",
    "Harry": "Grifinória",
    "Rony": "Grifinória",
    "Draco": "Sonserina",
}

# Chamada da função
exibir_estudantes_com_casas(estudantes)
