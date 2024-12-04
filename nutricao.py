alimentos = [
    {"nome": "maçã", "calorias": "52", "proteinas": "0.3", "carboidratos": "14", "gorduras": "0.2"},
    {"nome": "banana", "calorias": "89", "proteinas": "1.1", "carboidratos": "23", "gorduras": "0.3"},
    {"nome": "arroz", "calorias": "130", "proteinas": "2.4", "carboidratos": "28", "gorduras": "0.3"},
    {"nome": "frango", "calorias": "165", "proteinas": "31", "carboidratos": "0", "gorduras": "3.6"},
    {"nome": "ovo", "calorias": "155", "proteinas": "31", "carboidratos": "1.1", "gorduras": "11"},
    {"nome": "uva", "calorias": "67", "proteinas": "0.6", "carboidratos": "17", "gorduras": "0.4"},
    {"nome": "pão", "calorias": "265", "proteinas": "9", "carboidratos": "49", "gorduras": "3.2"},
    {"nome": "leite", "calorias": "42", "proteinas": "3.4", "carboidratos": "5", "gorduras": "1"},
    {"nome": "melancia", "calorias": "30", "proteinas": "0.6", "carboidratos": "8", "gorduras": "0.2"},
    {"nome": "melão", "calorias": "34", "proteinas": "0.6", "carboidratos": "8", "gorduras": "0.2"},
]

def informacao_alimento(nome, alimentos):
    for alimento in alimentos:
        if alimento["nome"].lower() == nome.lower():
            return alimento
    return None

def main():
    nome_alimento = input("Digite o nome do alimento: ")
    alimento_encontrado = informacao_alimento(nome_alimento, alimentos)

    if alimento_encontrado:
        print("\nInformações do alimento:")
        print(f"Nome: {alimento_encontrado['nome']}")
        print(f"Calorias: {alimento_encontrado['calorias']}")
        print(f"Proteínas: {alimento_encontrado['proteinas']}")
        print(f"Carboidratos: {alimento_encontrado['carboidratos']}")
        print(f"Gorduras: {alimento_encontrado['gorduras']}")
    else:
        print("Esse alimento não foi encontrado. Tente novamente com outro!")

# Chamada da função principal
main()
