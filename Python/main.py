from Python.packages.bank.PersonalBankAccount import PersonalBankAccount

personal_account = PersonalBankAccount(account_number="AB123456", balance=1000.0, first_name="Alice", last_name="Dupont", address="123 Rue Exemple, Paris")
print(f'{personal_account}')

personal_account.deposit(10.5)
print(f'{personal_account}')