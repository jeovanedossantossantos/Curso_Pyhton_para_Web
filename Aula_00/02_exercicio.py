# 3. Faça um programa que leia 3 valores em variáveis distintas, armazene a soma das duas primeiras
# em uma nova variável e o produto das duas últimas em outra, e mostre como resultado o produto
# das duas novas variáveis. Exemplo para as variáveis A, B e C:
#  D = A+ B
#  E = B * C
#  Resultado = D * E

# Como lação de repetição

while True:
    op = int(input("[1] - Resover a conta\n[2] - Para sair do progrma"))

    if (op == 1):

        a = int(input("Valor um!"))
        b = int(input("Valor dois!"))
        c = int(input("Valor três!"))

        d = a + b
        e = b*c

        print("Respostas ", d*e)
    elif (op == 2):
        break
    else:
        print("Valor invalido!")
