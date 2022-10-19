import requests
from random import randint


def pokeApi(number_name):
    api = f'https://pokeapi.co/api/v2/pokemon/{number_name}'
    res = requests.get(api)
    pokemon = res.json()
    return pokemon


def namePokemon(data):
    id_pokemon = data['id']
    name_pokemon = data['species']['name']
    print(f'#{id_pokemon}')
    print(f'Nome do pokemon: {name_pokemon.title()}')


def pokeAbility(data):
    for n, i in enumerate(data['abilities']):
        print(f"Abilidade_{n + 1}: {i['ability']['name']}")


def pokeMoves(data):
    move = []
    for n, i in enumerate(data['moves']):
        move.append(i['move']['name'])
    move1 = move[randint(0, len(move))]
    move2 = move[randint(0, len(move))]
    move3 = move[randint(0, len(move))]
    move4 = move[randint(0, len(move))]
    print('Movimentos: ')
    print(f"1-{move1}\t2-{move2}\n3-{move3}\t4-{move4}")


def typePokemon(data):
    type = 'Tipo: '
    for t in data['types']:
        type += f"{t['type']['name']}\t"
    print(type)


reset = True
while reset:
    select_pokemon = input('Digite nome ou id do pokemon: ')
    print()
    try:
        namePokemon(pokeApi(select_pokemon))
        typePokemon(pokeApi(select_pokemon))
        pokeAbility(pokeApi(select_pokemon))
        pokeMoves(pokeApi(select_pokemon))
        print()
        reset = False
    except ValueError:
        print('Esse pókemon não existe')
        print()
