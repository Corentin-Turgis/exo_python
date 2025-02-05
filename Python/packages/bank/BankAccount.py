class BankAccount:
    def __init__(self, account_number: str, balance: float = 0.0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount: float):
        if amount > 0:
            self.balance += amount
            print(f"Dépôt de {amount} effectué. Nouveau solde: {self.balance:.2f}€")
        else:
            print("Le montant du dépôt doit être positif.")

    def withdraw(self, amount: float):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Retrait de {amount} effectué. Nouveau solde: {self.balance:.2f}€")
            else:
                print("Fonds insuffisants.")
        else:
            print("Le montant du retrait doit être positif.")

    def __str__(self):
        return f"Compte #{self.account_number} avec un solde de {self.balance:.2f}€"