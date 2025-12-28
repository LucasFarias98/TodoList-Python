tarefas = []


def adicionar_tarefa():
    tarefa = input("Digite a tarefa que você quer adicionar: ")
    tarefas.append(tarefa)
    print(f"\nTarefa '{tarefa}' foi adicionada à lista.\n")


def listar_tarefas():
    if not tarefas:
        print("\nNão há tarefas no momento.\n")
        return

    print("\nTarefas atuais:")
    for indice, tarefa in enumerate(tarefas):
        print(f"{indice} - {tarefa}")
    print()


def excluir_tarefa():
    listar_tarefas()

    if not tarefas:
        return

    try:
        texto_indice = input("Digite o número da tarefa que deseja excluir: ")
        indice = int(texto_indice)

        if 0 <= indice < len(tarefas):
            tarefa_removida = tarefas.pop(indice)
            print(f"\nTarefa '{tarefa_removida}' foi removida.\n")
        else:
            print("\nÍndice inválido. Nenhuma tarefa foi removida.\n")

    except ValueError:
        print("\nEntrada inválida. Digite apenas números inteiros.\n")


def mostrar_menu():
    print("===== APLICATIVO DE LISTA DE TAREFAS =====")
    print("1 - Adicionar nova tarefa")
    print("2 - Excluir tarefa")
    print("3 - Listar tarefas")
    print("4 - Sair")
    print("===========================================")


def main():
    print("Bem-vindo ao aplicativo de lista de tarefas! :)")

    while True:
        mostrar_menu()
        escolha = input("Digite a sua opção: ")

        if escolha == "1":
            adicionar_tarefa()
        elif escolha == "2":
            excluir_tarefa()
        elif escolha == "3":
            listar_tarefas()
        elif escolha == "4":
            print("\nSaindo do aplicativo. Até logo! 👋\n")
            break
        else:
            print("\nOpção inválida. Tente novamente.\n")


if __name__ == "__main__":
    main()
