from Python.decorators.verbose_test import verbose_params, verbose_return


class BankAccount:
    def __init__(self, account_number: str, balance: float = 0.0):
        self.account_number = account_number
        self.balance = balance

    @verbose_params
    @verbose_return
    def deposit(self, amount: float):
        if amount > 0:
            self.balance += amount
        else:
            pass

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

    def __repr__(self):
        return f'BankAccount({self.account_number}, {self.balance})'