import fileinput
import sys
from click import prompt

from Python.decorators.verbose_test import *


class Tools:
    @staticmethod
    def ask(str_to_show, default=None):
        return prompt(str_to_show, default=default)

    @staticmethod
    @verbose_params
    def search_n_replace_in_file(file_path, string, x):
        try:
            for line in fileinput.input(files=[file_path], inplace=True, backup=".bak", encoding="utf-8"):
                sys.stdout.write(line.replace(string, x))
        except FileNotFoundError as fnf_error:
            print(f"Erreur : le fichier '{file_path}' n'a pas été trouvé. Détails : {fnf_error}")
        except UnicodeDecodeError as ude_error:
            print(f"Erreur d'encodage lors de la lecture du fichier '{file_path}'. Détails : {ude_error}")
        except Exception as e:
            print(f"Une erreur est survenue lors du traitement du fichier '{file_path}'. Détails : {e}")

    @staticmethod
    def file_to_dict(file_path):
        res = {}
        try:
            for i, line in enumerate(fileinput.input(files=[file_path], encoding="utf-8"), start=1):
                res[i] = line.rstrip("\n")
        except FileNotFoundError as fnf_error:
            print(f"Erreur : le fichier '{file_path}' n'a pas été trouvé. Détails : {fnf_error}")
        except UnicodeDecodeError as ude_error:
            print(f"Erreur d'encodage lors de la lecture du fichier '{file_path}'. Détails : {ude_error}")
        except Exception as e:
            print(f"Une erreur est survenue lors du traitement du fichier '{file_path}'. Détails : {e}")
        finally:
            fileinput.close()
        return res

    @staticmethod
    def display_file_dict(file_dict):
        if not isinstance(file_dict, dict):
            raise ValueError("Erreur : file_dict doit etre un dictionnaire.")
        for key, value in file_dict.items():
            if not isinstance(key, int):
                raise ValueError(f"Erreur : la clé '{key}' n'est pas de type int.")
            if not isinstance(value, str):
                raise ValueError(f"Erreur : la valeur associée à la clé {key} n'est pas une chaîne de caractères.")
        for line_number in sorted(file_dict.keys()):
            line_content = file_dict[line_number]
            char_count = len(line_content)
            print(f"Ligne numéro {line_number} : {char_count} caractères → \"{line_content}\"")