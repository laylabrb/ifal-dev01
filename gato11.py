def miar_gato():
    while True:
        miaus = int(input("Quantas vezes o gato deve miar? "))
        if miaus <= 0:
            print("Por favor, insira um número maior que 0.")
            continue
        else:
            break

    for _ in range(miaus):
        print("😽 miau")

miar_gato()
