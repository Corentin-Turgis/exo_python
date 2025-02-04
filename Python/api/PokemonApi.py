import requests

class PokemonApi:
    @staticmethod
    def get_pokemon(name):
        url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
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