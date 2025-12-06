lista = []

while True:
    print("\nLISTA DE COMPRAS:")
    print("1 - Adicionar item à lista")
    print("2 - Remover item da lista")
    print("3 - Mostrar lista")
    print("4 - SAIR")

    opcao = int(input("Escolha uma opção:"))

    if opcao == 1:

        item = input("Digite o item:")
        lista.append(item)
        print("O item {} foi adicionado à lista.".format(item))

    elif opcao == 2:

        item_removido = input("Digite o item à ser removido:")
        lista.remove(item_removido)
        print("O item {} foi removido da lista.".format(item_removido))

    elif opcao == 3:

        lista_pronta = " ".join(lista)
        print(lista_pronta)

    elif opcao == 4:

        print("Saindo...")
        break

    else:
        print("Opção inválida.")                    