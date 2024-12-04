def desenhar_coluna(altura):
    for _ in range(altura):
        print("#")

altura = int(input("Qual a altura da coluna?"))
desenhar_coluna(altura)