from Ex5 import Ex5
from Ex4 import Ex4
from Python.packages.bank.PersonalBankAccount import PersonalBankAccount

app = Ex4()
app.start()

app = Ex5()
app.start()

personal_account = PersonalBankAccount(account_number="AB123456", balance=1000.0, first_name="Alice", last_name="Dupont", address="123 Rue Exemple, Paris")
print(f'{personal_account}')
