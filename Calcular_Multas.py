def multa_localidade(velocidade):
    if velocidade <= 50:
        return 0
    elif velocidade >= 120:
        return 320
    elif velocidade >= 90:
        return 120
    else:
        return 60


def multa_fora_localidade(velocidade):
    if velocidade <= 90:
        return 0
    elif velocidade >= 120:
        return 120
    else:
        return 60


def multa_autoestrada(velocidade):
    if velocidade <= 120:
        return 0
    elif velocidade > 175:
        return 360
    elif velocidade > 150:
        return 120
    else:
        return 60


def menu():
    print("\n Menu de Tipos de Via ")
    print("1. Localidade")
    print("2. Fora da localidade")
    print("3. Autoestrada")
    print("0. Sair")


def main():
    while True:
        menu()
        opcao = input("Escolha o tipo de via (0 para sair): ")

        if opcao == "0":
            print("Programa encerrado.")
            break

        try:
            velocidade = float(input("Introduza a velocidade do carro (km/h): "))
        except ValueError:
            print("Por favor, introduza um número válido.")
            continue

        if opcao == "1":
            multa = multa_localidade(velocidade)
        elif opcao == "2":
            multa = multa_fora_localidade(velocidade)
        elif opcao == "3":
            multa = multa_autoestrada(velocidade)
        else:
            print("Opção inválida.")
            continue

        if multa == 0:
            print("Não há multa a pagar.")
        else:
            print(f"Multa a pagar: {multa}€")


if __name__ == "__main__":
    main()
