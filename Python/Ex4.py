from Python.env import WORKING_DIR
from utils.IP_utils import IP
from utils.Tools_utils import Tools

class Ex4:
    ips = [
        "192.168.1.1",
        "10.0.0.1",
        "2001:0db8:85a3::8a2e:0370:7334",
        "256.256.256.256"
    ]
    bad_ips = [
        123, "Not an IP", None
    ]
    ips_dict = {
        "local": "127.0.0.1",
        "public": "8.8.8.8",
        "ipv6": "2001:4860:4860::8888",
        "bad": "999.999.999.999"
    }
    bad_ips_dict = ([8, 6])

    def __init__(self):
        pass

    def start(self):
        self.__check_uniq_ip()
        self.__check_ip_list()
        self.__check_ip_dict()
        self.__replace_words()

    @staticmethod
    def __check_uniq_ip():
        ip = Tools.ask('Entrez une ip')
        print(IP.detect_ip_type(ip))

    def __check_ip_list(self):
        print('Test de la liste d\'ips :')
        IP.detect_multiple_ip(self.ips)

        print('Test de la mauvaise liste d\'ips :')
        try:
            IP.detect_multiple_ip(self.bad_ips)
        except ValueError as e:
            print(e.args[0])

    def __check_ip_dict(self):
        print('Test du dictionaire d\'ips :')
        IP.detect_multiple_ip(self.ips_dict)

        print('Test du mauvais dictionaire d\'ips :')
        try:
            IP.detect_multiple_ip(self.bad_ips_dict)
        except ValueError as e:
            print(e.args[0])

    @staticmethod
    def __replace_words():
        file_path = Tools.ask('Quel fichier modifier', default=f'{WORKING_DIR}/assets/replace_my_words.txt')
        str_to_replace = Tools.ask('Que voulez-vous changer', default='ancienne_chaine')
        x = Tools.ask('Par quoi la modifier', default='x')

        try:
            Tools.search_n_replace_in_file(file_path, str_to_replace, x)
        except Exception as e:
            print(f"Erreur : {e}")
