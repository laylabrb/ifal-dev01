def exibir_alunos(alunos):
    print("Alunos:")
    for nome, casa in alunos.items():
        print(f"{nome} pertence à casa {casa}.")

alunos = {
    "Hermione": "Grifinória",
    "Harry": "Grifinória",
    "Rony": "Grifinória",
    "Draco": "Sonserina",
}

# Chamada da função
exibir_alunos(alunos)

