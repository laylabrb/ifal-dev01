def calcular_potencia(base, expoente):
    resultado = base ** expoente

    resultado = f"{resultado:_.2f}"  
    resultado = resultado.replace(".", ",").replace("_", ".")

    # Exibe o resultado formatado
    print(f"{base} elevado ao {expoente} é {resultado}")


def main():
    base = float(input("Digite o primeiro número (base): "))
    expoente = float(input("Digite o segundo número (expoente): "))
    calcular_potencia(base, expoente)



main()
