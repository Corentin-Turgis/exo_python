class ClientIdentity:
    def __init__(self, first_name: str, last_name: str, address: str = ""):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

    def __str__(self):
        return f"{self.first_name} {self.last_name}" + (f", {self.address}" if self.address else "")

    def __repr__(self):
        return f'ClientIdentity({self.first_name}, {self.last_name}, {self.address})'
