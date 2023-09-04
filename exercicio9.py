#Iniciar
agenda_telefonica = {}

def adicionar_contato():
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o número de telefone: ")
    agenda_telefonica[nome] = telefone
    print("Contato adicionado com sucesso!")

def pesquisar_contato():
    nome = input("Digite o nome do contato que deseja pesquisar: ")
    if nome in agenda_telefonica:
        print(f"Nome: {nome}, Telefone: {agenda_telefonica[nome]}")
    else:
        print("Contato não encontrado na agenda.")

def editar_contato():
    nome = input("Digite o nome do contato que deseja editar: ")
    if nome in agenda_telefonica:
        novo_telefone = input("Digite o novo número de telefone: ")
        agenda_telefonica[nome] = novo_telefone
        print("Contato atualizado com sucesso!")
    else:
        print("Contato não encontrado na agenda.")

def excluir_contato():
    nome = input("Digite o nome do contato que deseja excluir: ")
    if nome in agenda_telefonica:
        del agenda_telefonica[nome]
        print("Contato excluído com sucesso!")
    else:
        print("Contato não encontrado na agenda.")

def listar_contatos():
    if not agenda_telefonica:
        print("A agenda telefônica está vazia.")
    else:
        print("Lista de Contatos:")
        for nome, telefone in agenda_telefonica.items():
            print(f"Nome: {nome}, Telefone: {telefone}")

while True:
    print("\nOpções:")
    print("1. Adicionar Contato")
    print("2. Pesquisar Contato")
    print("3. Editar Contato")
    print("4. Excluir Contato")
    print("5. Listar Contatos")
    print("6. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_contato()
    elif opcao == "2":
        pesquisar_contato()
    elif opcao == "3":
        editar_contato()
    elif opcao == "4":
        excluir_contato()
    elif opcao == "5":
        listar_contatos()
    elif opcao == "6":
        break
    else:
        print("Opção inválida. Tente novamente.")