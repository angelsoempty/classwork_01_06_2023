class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print("Гроші успішно додано. Новий баланс:", self.balance)
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("Гроші успішно знято. Новий баланс:", self.balance)
        else:
            print("Недостатньо коштів на рахунку.")

account1 = BankAccount("1234567890", 1000)
account1.deposit(100)
account1.withdraw(400)
