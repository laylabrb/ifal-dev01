def processar_texto_e_nome():
    # Texto de exemplo
    texto = "Olá, Mundo! Olá IFAL MD!"

    # Conta quantas vezes "olá, mundo" aparece no texto (case insensitive)
    count_olamundo = texto.lower().count("olá, mundo")
    print(f'Quantidade de vezes que "olá, mundo" aparece: {count_olamundo}')

    # Encontra a posição de "mundo" no texto (case insensitive)
    pos_mundo = texto.lower().find("mundo")
    print(f'Posição da palavra "mundo" no texto: {pos_mundo}')

    # Capitaliza a primeira palavra do texto e substitui "mundo" por "IFAL"
    texto_modificado = texto.capitalize().replace("mundo", "IFAL")
    print(f'Texto modificado: {texto_modificado}')

    # Solicita o nome do usuário
    nome = input("Qual seu nome e último nome? ")

    # Coloca cada parte do nome com a primeira letra maiúscula
    nome_formatado = nome.title().split()
    nome_formatado = " ".join(nome_formatado)

    # Separa o primeiro nome e o sobrenome
    primeiro_nome, sobrenome = nome_formatado.split()
    print(f"Olá, {nome_formatado}")
    print(f"Olá, {primeiro_nome} {sobrenome}")

    # Remove espaços desnecessários antes e depois do nome (várias formas de fazer isso)
    print(f"Nome com espaços removidos: {nome_formatado.strip()}")
    print(f"Nome com espaços à direita removidos: {nome_formatado.rstrip()}")
    print(f"Nome com espaços à esquerda removidos: {nome_formatado.lstrip()}")

    # Diferentes maneiras de formatar o nome
    print(f"Nome com cada palavra capitalizada: {nome_formatado.title()}")
    print(f"Nome com a primeira palavra capitalizada: {nome_formatado.capitalize()}")
    print(f"Nome em maiúsculas: {nome_formatado.upper()}")
    print(f"Nome em minúsculas: {nome_formatado.lower()}")


processar_texto_e_nome()

