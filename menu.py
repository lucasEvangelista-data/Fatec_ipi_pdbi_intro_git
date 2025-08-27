#Implemente função menu que ofereça opção para os usuários:
# Somar , Subtrair, Dividir, Multiplicar, Dividir, Sair
import calculadora

def menu():
    while True:
        print("\n===== MENU =====")
        print("1. Somar")
        print("2. Subtrair")
        print("3. Multiplicar")
        print("4. Dividir")
        print("0. Sair")

        opcao = int(input("Digite a opção desejada: "))

        if opcao == 0:
            print("Saindo...")
            break
        elif opcao in [1, 2, 3, 4]:
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))

            if opcao == 1:
                print("Resultado:", calculadora.somar(a, b))

            if opcao ==2:
                print("Resultado:", calculadora.subtrair(a, b))

            if opcao ==3:
                print("Resultado:", calculadora.multiplicar(a, b))

            elif opcao == 4:
                if b == 0:
                    print("Erro: divisão por zero não é permitida.")
                else:
                    print("Resultado:", calculadora.dividir(a, b))
        else:
            print("Opção inválida!")

menu()
