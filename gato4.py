def miar_gato():
    while True:
        miaus= int(input("Quantas vezes seu gato mia?"))
        if miaus>0:
            break
        print("miau\n" * miaus, end="")

miar_gato()