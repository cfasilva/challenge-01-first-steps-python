def inserir_contato(contatos, nome, telefone, email, favorito):
    contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "favorito": favorito
    }
    contatos.append(contato)

    print(f"\nContato {nome} inserido com sucesso!")

    return

def visualizar_contatos(contatos):
    print("\nLista de contatos cadastrados:")
    for contato in contatos:
        nome = contato["nome"]
        telefone = contato["telefone"]
        email = contato["email"]
        favorito = contato["favorito"]

        print(f"Nome: {nome}, Telefone: {telefone}, Email: {email}, Favorito: {favorito}")

    return

def editar_contato(contatos, nome, telefone, email, favorito):
    for contato in contatos:
        if contato["nome"] == nome:
            contato["telefone"] = telefone
            contato["email"] = email
            contato["favorito"] = favorito

            print(f"\nContato {nome} editado com sucesso!")

            return

    print(f"\nContato {nome} não encontrado.")

    return

def marcar_desmarcar_favorito(contatos, nome):
    for contato in contatos:
        if contato["nome"] == nome:
            if contato["favorito"] == "S":
                contato["favorito"] = "N"
            else:
                contato["favorito"] = "S"

            print(f"\nContato {nome} marcado/desmarcado como favorito com sucesso!")

            return

    print(f"\nContato {nome} não encontrado.")

    return

def visualizar_favoritos(contatos):
    print("\nLista de contatos favoritos:")
    for contato in contatos:
        if contato["favorito"] == "S":
            nome = contato["nome"]
            telefone = contato["telefone"]
            email = contato["email"]
            favorito = contato["favorito"]

            print(f"Nome: {nome}, Telefone: {telefone}, Email: {email}, Favorito: {favorito}")

    return

def excluir_contato(contatos, nome):
    for contato in contatos:
        if contato["nome"] == nome:
            contatos.remove(contato)

            print(f"\nContato {nome} excluído com sucesso!")

            return

    print(f"\nContato {nome} não encontrado.")

    return

contatos = []

while True:
    print("\nMenu de opções da Agenda de Contatos:")
    print("1 - Inserir novo contato")
    print("2 - Visualizar lista de contatos cadastrados")
    print("3 - Editar contato")
    print("4 - Marcar/Desmarcar contato como favorito")
    print("5 - Visualizar lista de contatos favoritos")
    print("6 - Excluir contato")
    print("7 - Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        email = input("Digite o email do contato: ")
        favorito = input("O contato é favorito? (S/N): ")

        inserir_contato(contatos, nome, telefone, email, favorito)
    elif opcao == "2":
        visualizar_contatos(contatos)
    elif opcao == "3":
        nome = input("Digite o nome do contato a ser editado: ")
        telefone = input("Digite o novo telefone do contato: ")
        email = input("Digite o novo email do contato: ")
        favorito = input("O contato é favorito? (S/N): ")

        editar_contato(contatos, nome, telefone, email, favorito)
    elif opcao == "4":
        nome = input("Digite o nome do contato a ser marcado/desmarcado como favorito: ")

        marcar_desmarcar_favorito(contatos, nome)
    elif opcao == "5":
        visualizar_favoritos(contatos)
    elif opcao == "6":
        nome = input("Digite o nome do contato a ser excluído: ")

        excluir_contato(contatos, nome)
    elif opcao == "7":
        break

print("Programa finalizado.")