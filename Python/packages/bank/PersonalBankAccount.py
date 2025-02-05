from Python.packages.bank import BankAccount, ClientIdentity

class PersonalBankAccount(BankAccount, ClientIdentity):
    def __init__(self, account_number: str, first_name: str, last_name: str, address: str = "", balance: float = 0.0):
        BankAccount.__init__(self, account_number, balance)
        ClientIdentity.__init__(self, first_name, last_name, address)

    def __str__(self):
        return f"Compte bancaire de {ClientIdentity.__str__(self)} (N° {self.account_number}) - Solde : {self.balance:.2f}€"
