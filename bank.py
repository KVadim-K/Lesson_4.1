class Account():
    def __init__(self, id, balance=0):
        self.id = id
        self.balance = balance
    def deposit(self, money):
        if money > 0:
            self.balance += money
            print(f"Вы успешно положили {money} рублей на счет. Сумма на счету - {self.balance}")
    def withdraw(self, money):
        if money > self.balance:
            print(f"Вы успешно положили {money} рублей на счет. Сумма на счету - {self.balance}.")
        elif money < self.balance:
            self.balance -= money
            print(f"Вы успешно сняли {money} рублей со счета. Остаток на счету - {self.balance}.")
    def info(self):
        print(f"Ваш баланс - {self.balance} рублей")
man = Account(id = "1234556789", balance = 1000)

man.info()
man.deposit(1000)
man.withdraw(500)
man.withdraw(800)
man.deposit(23000)
man.info()