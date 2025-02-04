import fileinput
import sys
from click import prompt

class Tools:
    @staticmethod
    def ask(str_to_show):
        return prompt(str_to_show)

    @staticmethod
    def search_n_replace_in_file(file_path, string, x):
        for line in fileinput.input(files=[file_path], inplace=True, backup=".bak", encoding="utf-8"):
            sys.stdout.write(line.replace(string, x))