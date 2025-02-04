from click import prompt

class Tools:
    @staticmethod
    def ask(str_to_show):
        return prompt(str_to_show)

