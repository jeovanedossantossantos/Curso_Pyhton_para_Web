# 1- Acesse os atributos nome, idade e cidade das pessoas dentro
# da lista de dicionários.

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

for i in pessoas:
    print(i['nome'], i['idade'], i['cidade'])
