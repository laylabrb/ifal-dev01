def main():
    resposta = input ("Você concorda?:").lower()
    obterResposta(resposta)

def obterResposta(resposta):
    match resposta:
        case "S" | "sim" | "SIM" | "s":
            print("Eu concordo")
        case "n" | "não" | "NÃO"  | "N":
            print("Eu não concordo")
        case "NÃO SEI" | "não sei":
            print("Não sei se concordo")
        case _:
            print("Resposta inválida")

main()

    
