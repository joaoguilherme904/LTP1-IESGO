#iniciar lista de tarefa vazia
lista_de_tarefas = []

def adicionar_tarefa():
    tarefa = input("Digite a tarefa que deseja adicionar: ")
    lista_de_tarefas.append({"tarefa": tarefa, "concluida": False})
    print("Tarefa adicionada com sucesso!")

def marcar_como_concluida():
    mostrar_tarefas()
    numero_tarefa = int(input("Digite o número da tarefa concluída: "))
    if numero_tarefa >= 1 and numero_tarefa <= len(lista_de_tarefas):
        lista_de_tarefas[numero_tarefa - 1]["concluida"] = True
        print("Tarefa marcada como concluída!")
    else:
        print("Número de tarefa inválido.")

def remover_tarefa():
    mostrar_tarefas()
    numero_tarefa = int(input("Digite o número da tarefa a ser removida: "))
    if numero_tarefa >= 1 and numero_tarefa <= len(lista_de_tarefas):
        tarefa_removida = lista_de_tarefas.pop(numero_tarefa - 1)
        print(f"Tarefa removida: {tarefa_removida['tarefa']}")
    else:
        print("Número de tarefa inválido.")

def mostrar_tarefas():
    print("\nLista de Tarefas:")
    for i, tarefa in enumerate(lista_de_tarefas, 1):
        status = " (Concluída)" if tarefa["concluida"] else ""
        print(f"{i}. {tarefa['tarefa']}{status}")

while True:
    print("\nOpções:")
    print("1. Adicionar Tarefa")
    print("2. Marcar Tarefa como Concluída")
    print("3. Remover Tarefa")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_tarefa()
    elif opcao == "2":
        marcar_como_concluida()
    elif opcao == "3":
        remover_tarefa()
    elif opcao == "4":
        break
    else:
        print("Opção inválida. Tente novamente.")