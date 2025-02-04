import fileinput
import sys
from click import prompt

class Tools:
    @staticmethod
    def ask(str_to_show, default=None):
        return prompt(str_to_show, default=default)

    @staticmethod
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