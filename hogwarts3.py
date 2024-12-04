def exibir_casa_estudantes(estudantes):
   
    for nome, casa in estudantes.lower():
        print(f"{nome}: {casa}")

estudantes = {
    "Hermione": "Grifinória",
    "Harry": "Grifinória",
    "Rony": "Grifinória",
    "Draco": "Sonserina",
}


exibir_casa_estudantes(estudantes)