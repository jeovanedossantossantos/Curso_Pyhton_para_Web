"""1. Escreva um algoritmo que leia um valor real correspondente a um saque em um caixa eletrônico.
Escreva a menor quantidade possível de cédulas para o saque realizado, sabendo que o caixa
eletrônico possui cédulas de 100, 50, 20, 5 e 1.
Exemplo: para o saque R$ 297,00, o resultado será:
 2 cédulas de R$ 100;
 1 cédula de R$ 50;
 2 cédulas de R$ 20;
 1 cédula de R$ 5;
 2 cédulas de R$ 1
Dica: utilizar os conceitos de quociente inteiro e resto da divisão (% ou MOD) vistos em sala de
aula."""

while True:

    valor = int(input("Digite o valor a ser sacado!"))

    if (valor < 0):
        print("Valor invalido!")
    else:
        valor100 = valor//100
        resto100 = valor % 100

        valor50 = resto100//50
        resto50 = resto100 % 50

        valor20 = resto50//20
        resto20 = resto50 % 20

        valor5 = resto20//5
        resto5 = resto20 % 5

        valor1 = resto5
        print("para o saque R$ %d,00 o resultado será:" % valor)
        print("%d cédula R$ 100" % valor100)
        print("%d cédula R$ 50" % valor50)
        print("%d cédula R$ 20" % valor20)
        print("%d cédula R$ 5" % valor5)
        print("%d cédula R$ 1" % valor1)

    op = int(
        input("Deseja sair?\n0 para sair ou qualquer outro número para continuar"))

    if (op == 0):
        break
