import csv

from Python.config import WORKING_DIR
from Python.packages.api.pokemon_api import get_pokemon_atk
from Python.packages.tools import csv_find_and_replace, file_to_dict, dict_to_json, dict_to_csv


class Ex5:

    def __init__(self):
        pass

    def start(self):
        battle_armor = get_pokemon_atk('battle-armor')
        self.__create_sample_csv()
        csv_find_and_replace(f'{WORKING_DIR}/assets/sample.csv', "Alice", "Bob")

        my_dict = file_to_dict(f'{WORKING_DIR}/assets/replace_my_words.txt')
        dict_to_json(my_dict, f'{WORKING_DIR}/assets/words.json')
        dict_to_csv(my_dict, f'{WORKING_DIR}/assets/words.csv')


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