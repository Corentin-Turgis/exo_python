import ipaddress
import fileinput
import requests
import csv
import json

def get_ip():
    ip = input("Entrez une adresse IP (IPv4 ou IPv6) : ")
    return ip

def is_valid_ipv4(ip):
    try:
        ipaddress.IPv4Address(ip)
        return True
    except ipaddress.AddressValueError:
        return False

def is_valid_ipv6(ip):
    try:
        ipaddress.IPv6Address(ip)
        return True
    except ipaddress.AddressValueError:
        return False

def detect_ip_version(ip):
    if is_valid_ipv4(ip):
        return "IPv4"
    elif is_valid_ipv6(ip):
        return "IPv6"
    else:
        return "Adresse invalide"

def validate_ip_dict(ip_dict):
    result = {}
    for host, ip in ip_dict.items():
        try:
            result[host] = detect_ip_version(ip)
        except Exception as e:
            result[host] = f"Erreur: {str(e)}"
    return result

def replace_letters_in_file(file_path, letters_to_replace, replacement="x"):
    try:
        with fileinput.FileInput(file_path, inplace=True, backup='.old') as file:
            for line in file:
                for letter in letters_to_replace:
                    line = line.replace(letter, replacement)
                print(line, end='')
    except Exception as e:
        print(f"Erreur lors de la modification du fichier : {e}")

def file_to_dict(file_path):
    content_dict = {}
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for i, line in enumerate(file, 1):
                content_dict[i] = line.strip()
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier : {e}")
    return content_dict

def display_file_content(file_dict):
    for line_number, content in file_dict.items():
        print(f"Ligne numéro {line_number} : {len(content)} caractères → \"{content}\"")

def fetch_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        print(f"Erreur HTTP: {e}")
        return None

def save_json(data, filename):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Erreur lors de la sauvegarde JSON: {e}")

def save_csv(data, filename):
    try:
        with open(filename, "w", newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(data.keys())
            writer.writerow(data.values())
    except Exception as e:
        print(f"Erreur lors de la sauvegarde CSV: {e}")

if __name__ == "__main__":
    ip_dict = {"host1": "192.168.1.1", "host2": "2001:db8::ff00:42:8329", "host3": "invalid_ip"}
    print(validate_ip_dict(ip_dict))

    file_path = "test.txt"
    replace_letters_in_file(file_path, ["a", "e", "i", "o", "u"])

    file_content = file_to_dict(file_path)
    display_file_content(file_content)

    pokemon_name = "pikachu"
    pokemon_data = fetch_pokemon_data(pokemon_name)
    if pokemon_data:
        save_json(pokemon_data, "pokemon_data.json")
        save_csv(pokemon_data, "pokemon_data.csv")
        file_content = file_to_dict("pokemon_data.json")
        display_file_content(file_content)
