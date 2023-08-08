# 3. Faça um programa que leia 3 valores em variáveis distintas, armazene a soma das duas primeiras
# em uma nova variável e o produto das duas últimas em outra, e mostre como resultado o produto
# das duas novas variáveis. Exemplo para as variáveis A, B e C:
#  D = A+ B
#  E = B * C
#  Resultado = D * E


a = int(input("Valor um!"))
b = int(input("Valor dois!"))
c = int(input("Valor três!"))

d = a + b
e = b*c

print("Respostas ", d*e)
