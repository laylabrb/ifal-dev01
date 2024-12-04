def calcular_expressao():
    while True:
        try:
            entrada = input("Digite a expressão aritmética (número operador número) ou 'sair' para encerrar: ")
            if entrada.lower() == 'sair':
                print("Encerrando o programa.")
                break

            # Avalia a expressão aritmética
            resultado = eval(entrada, {"__builtins__": None}, {})
            print(f"Resultado: {resultado}")
        except Exception as e:
            print("Não foi possível calcular. Certifique-se de usar os símbolos corretos (ex.: 2 + 2, 5 * 3).")

# Chamada da função
calcular_expressao()
