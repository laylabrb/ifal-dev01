def calcular_nota(pontos):
    
    if 90 <= pontos <= 100:
        return "A"
    elif 80 <= pontos < 90:
        return "B"
    elif 70 <= pontos < 80:
        return "C"
    elif 60 <= pontos < 70:
        return "D"
    else:
        return "F"

# Entrada do usuário
try:
    pontos = int(input("Pontos: "))
    # Processamento e saída
    nota = calcular_nota(pontos)
    print(f"Sua nota é: {nota}")
except ValueError:
    print("Por favor, insira um valor válido.")