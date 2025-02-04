from Python.api.PokemonApi import PokemonApi

class Ex5:

    def __init__(self):
        pass

    @staticmethod
    def start():
        mew = PokemonApi.get_pokemon('mew')
        print(mew)