def miar_gato():
    while True:
        miaus = int(input("Quantas vezes o gato deve miar? "))
        if miaus > 0:
            break
        else:
            print("Por favor, insira um número maior que 0.")

    for _ in range(miaus):
        print("😽 miau")

miar_gato()