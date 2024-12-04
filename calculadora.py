def realizar_operacoes(x, y):
    print(f"A soma de {x} + {y} é {x + y}")
    print(f"A subtração de {x} - {y} é {x - y}")
    print(f"A multiplicação de {x} * {y} é {x * y}")
    print(f"A divisão de {x} / {y} é {round(x / y, 2)}")
    print(f"O resto de {x} % {y} é {x % y}")


def main():
    x = float(input("Digite o primeiro número: "))
    y = float(input("Digite o segundo número: "))
    realizar_operacoes(x, y)


main()
