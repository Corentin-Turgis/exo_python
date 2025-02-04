import requests

from Python.decorators.verbose_test import verbose_return


class PokemonApi:
    @staticmethod
    @verbose_return
    def get_pokemon_atk(name):
        url = f"https://pokeapi.co/api/v2/ability/{name.lower()}"
        try:
            res = requests.get(url)
            res.raise_for_status()
            data = res.json()
            return data
        except requests.exceptions.HTTPError as http_err:
            print(f"Erreur HTTP : {http_err}")
        except Exception as e:
            print(f"Erreur : {e}")

        return {}
