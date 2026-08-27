from modelos.petshop import PetShop

clientes = []
animais = []


def cadastrar_cliente():
    print("\n===== CADASTRO DE CLIENTE =====")

    nome = input("Nome do cliente: ")
    idade = int(input("Idade do cliente: "))

    cliente = {
        "nome": nome,
        "idade": idade
    }

    clientes.append(cliente)

    print(f"\nCliente {nome} cadastrado com sucesso!")
    return cliente


def cadastrar_animal():
    print("\n===== CADASTRO DE ANIMAL =====")

    nome = input("Nome do animal: ")
    especie = input("Espécie (cachorro/gato): ")
    idade = int(input("Idade do animal: "))
    peso = float(input("Peso do animal: "))

    animal = {
        "nome": nome,
        "especie": especie,
        "idade": idade,
        "peso": peso
    }

    animais.append(animal)

    print(f"\nAnimal {nome} cadastrado com sucesso!")
    return animal


def listar_animais():
    print("\n===== ANIMAIS CADASTRADOS =====")

    if len(animais) == 0:
        print("Nenhum animal cadastrado.")
        return

    for i in range(len(animais)):
        animal = animais[i]

        print(f"\nAnimal {i + 1}")
        print(f"Nome: {animal['nome']}")
        print(f"Espécie: {animal['especie']}")
        print(f"Idade: {animal['idade']} anos")
        print(f"Peso: {animal['peso']} kg")


def remover_animal():
    if len(animais) == 0:
        print("\nNão existem animais cadastrados.")
        return

    listar_animais()

    numero = int(input("\nDigite o número do animal que deseja remover: "))

    if numero >= 1 and numero <= len(animais):
        removido = animais.pop(numero - 1)
        print(f"Animal {removido['nome']} removido com sucesso!")
    else:
        print("Número inválido.")


def escolher_servico():
    print("\n===== SERVIÇOS =====")
    print("1 - Banho")
    print("2 - Tosa")
    print("3 - Banho e Tosa")

    opcao = int(input("Escolha o serviço: "))

    if opcao == 1:
        servico = "Banho"
        preco = 40.00
    elif opcao == 2:
        servico = "Tosa"
        preco = 50.00
    elif opcao == 3:
        servico = "Banho e Tosa"
        preco = 80.00
    else:
        print("Opção inválida.")
        return

    print(f"\nServiço escolhido: {servico}")
    print(f"Valor: R$ {preco:.2f}")

    return servico, preco


def mostrar_clientes():
    print("\n===== CLIENTES =====")

    if len(clientes) == 0:
        print("Nenhum cliente cadastrado.")
        return

    for i in range(len(clientes)):
        print(
            f"{i + 1} - {clientes[i]['nome']} "
            f"({clientes[i]['idade']} anos)"
        )


def menu():
    petshop = PetShop()

    while True:
        print("\n========== PET SHOP ==========")
        print("1 - Cadastrar cliente")
        print("2 - Cadastrar animal")
        print("3 - Listar animais")
        print("4 - Escolher serviço")
        print("5 - Remover animal")
        print("6 - Listar clientes")
        print("7 - Mostrar resumo")
        print("0 - Sair")

        opcao = int(input("\nEscolha uma opção: "))

        if opcao == 1:
            cliente = cadastrar_cliente()
            petshop.adicionar_cliente(cliente)

        elif opcao == 2:
            cadastrar_animal()

        elif opcao == 3:
            listar_animais()

        elif opcao == 4:
            escolher_servico()

        elif opcao == 5:
            remover_animal()

        elif opcao == 6:
            mostrar_clientes()

        elif opcao == 7:
            petshop.exibir_petshop()

        elif opcao == 0:
            print("\nSistema encerrado. Até mais!")
            break

        else:
            print("\nOpção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
