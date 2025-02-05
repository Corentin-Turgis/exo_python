import csv
import fileinput
import json
import sys
from click import prompt


def ask(str_to_show, default=None):
    return prompt(str_to_show, default=default)


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


def csv_find_and_replace(file_path, search_str, replace_str):
    csv.field_size_limit(sys.maxsize)
    try:
        with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier CSV: {e}")
        return

    new_rows = []
    for row in rows:
        new_row = [cell.replace(search_str, replace_str) for cell in row]
        new_rows.append(new_row)

    try:
        with open(f'{file_path}.new.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(new_rows)
        print(f"Find and replace terminé dans le fichier CSV: {file_path}")
    except Exception as e:
        print(f"Erreur lors de l'écriture du fichier CSV: {e}")


def dict_to_json(data, file_path):
    try:
        with open(file_path, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)
        print(f"Fichier JSON créé avec succès : {file_path}")
    except Exception as e:
        print(f"Erreur lors de la création du fichier JSON : {e}")


def dict_to_csv(data: dict, csv_file_path: str) -> None:
    try:
        with open(csv_file_path, "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["Clé", "Valeur"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for key, value in data.items():
                writer.writerow({"Clé": key, "Valeur": value})
        print(f"Fichier CSV créé avec succès : {csv_file_path}")
    except Exception as e:
        print(f"Erreur lors de la création du fichier CSV : {e}")
