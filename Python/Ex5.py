import csv

from Python.api.PokemonApi import PokemonApi
from Python.env import WORKING_DIR
from Python.utils.Tools_utils import Tools


class Ex5:

    def __init__(self):
        pass

    def start(self):
        mew = PokemonApi.get_pokemon('mew')
        self.__create_sample_csv()
        Tools.csv_find_and_replace(f'{WORKING_DIR}/assets/sample.csv', "Alice", "Bob")

        my_dict = Tools.file_to_dict(f'{WORKING_DIR}/assets/replace_my_words.txt')
        Tools.dict_to_json(my_dict, f'{WORKING_DIR}/assets/words.json')


    @staticmethod
    def __create_sample_csv():
        data = [
            ["Name", "Age", "City"],
            ["Alice", "30", "Paris"],
            ["Bob", "25", "Lyon"],
            ["Charlie", "35", "Marseille"]
        ]
        with open(f"{WORKING_DIR}/assets/sample.csv", "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data)