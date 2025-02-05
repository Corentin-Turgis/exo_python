from collections import namedtuple

class Card(namedtuple('CardBase', ['rank', 'color'])):
    __slots__ = ()

    def get_color_symbol(self):
        symbol_map = {
            'heart': '♥',
            'diamond': '♦',
            'club': '♣',
            'spade': '♠'
        }
        return symbol_map.get(self.color, self.color)

    def get_color(self):
        colors = {
            'spade': '\033[30m',
            'heart': '\033[91m',
            'diamond': '\033[92m',
            'club': '\033[93m'
        }
        return colors.get(self.color, '\033[0m')

    @property
    def ascii_lines(self):
        return [
            f"{self.get_color()}+-----+\033[0m",
            f"{self.get_color()}| {self.rank:<2}  |\033[0m",
            f"{self.get_color()}|  {self.get_color_symbol()}  |\033[0m",
            f"{self.get_color()}|  {self.rank:>2} |\033[0m",
            f"{self.get_color()}+-----+\033[0m"
        ]

    def __str__(self):
        return "\n" + "\n".join(self.ascii_lines)

    def __repr__(self):
        return f"Card(rank={self.rank}, color={self.color})"

    @staticmethod
    def display_cards(cards):
        cards = list(cards)
        if not cards:
            print("No cards here")
            return

        for i in range(0, len(cards), 5):
            chunk = cards[i:i+5]

            for line_i in range(len(chunk[0].ascii_lines)):
                line_parts = [card.ascii_lines[line_i] for card in chunk]
                print(" ".join(line_parts))
