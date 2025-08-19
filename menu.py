#Implemente função menu que ofereça opção para os usuários:
# Somar , Subtrair, Dividir, Multiplicar, Dividir, Sair
import calculadora

def opcoes():
    opcao = input(int("Digite a opção desejada: 1.Somar / 2.Subtrair / 3.Multiplicar / 4.Dividir / 0.Sair"))
    if opcao == 1:
        return calculadora.somar()

