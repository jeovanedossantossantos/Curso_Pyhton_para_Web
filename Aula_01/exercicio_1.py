# 2- Agora modifique o código para que mostre apenas os que tem
# a menor idade e a maior.
pessoas = [
    {
        'nome': 'João',
        'idade': 25,
        'cidade': 'São Paulo'
    }, {
        'nome': 'Maria',
        'idade': 22,
        'cidade': 'Cruza da Almas'
    }, {
        'nome': 'Pedro',
        'idade': 18,
        'cidade': 'Mangabeira'
    }
]

maior = pessoas[0]["idade"]
id_maior = 0
menor = pessoas[0]["idade"]
id_menor = 0


for i in range(len(pessoas)):

    if (pessoas[i]["idade"] >= maior):
        maior = pessoas[i]["idade"]
        id_maior = i
    if (pessoas[i]["idade"] < menor):
        menor = pessoas[i]["idade"]
        id_menor = i

print("A maior idade é de:")
print(pessoas[id_maior]["nome"])


print("A menor idade é de:")
print(pessoas[id_menor]["nome"])

pessoa_menor_idade = min(pessoas, key=lambda pessoa: pessoa['idade'])
pessoa_maior_idade = max(pessoas, key=lambda pessoa: pessoa['idade'])
print(pessoa_menor_idade)
print(pessoa_maior_idade)
print("A maior idade é de:")
print(pessoa_maior_idade["nome"])


print("A menor idade é de:")
print(pessoa_menor_idade["nome"])

nome_busca = 'Pedro'
pessoas_filtradas = list(
    filter(lambda pessoa: pessoa['nome'] == nome_busca, pessoas))[0]
print(pessoas_filtradas)
