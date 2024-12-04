def desenhar_bloco(tamanho):
    for _ in range(tamanho):
        print("#" * tamanho)

tamanho = int(input("Qual o tamanho do bloco?"))
desenhar_bloco(tamanho)