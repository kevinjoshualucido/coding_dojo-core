class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.acc = BankAccount(int_rate=0.001, bal=0)

    def make_deposit(self, amt):
        print('User:', self.name, 'Deposit:', self.acc.deposit(amt))
    
    def make_withdrawal(self, amt):
        print('User:', self.name, 'Withdrew:', self.acc.withdraw(amt))
    
    def display_user_balance(self):
        self.acc.disp_acc_info()


class BankAccount:
    balance = 0

    def __init__(self, int_rate, bal):
        self.int_rate = int_rate
        self.bal = bal

    def deposit(self, amt):
        self.bal += amt
        return amt

    def withdraw(self, amt):
        if self.bal < amt:
            print('- Insufficient funds: Charging a 5.00 fee')
            self.bal -= 5
        else:
            self.bal -= amt
        return amt

    def disp_acc_info(self):
        print('Balance:', self.bal)

    def int_yld(self):
        yielded_interest = self.bal * self.int_rate
        self.bal += yielded_interest
        print('Yielded interest:', round(yielded_interest, 2))
        return self


# account1 = BankAccount(0.0431, 150.00)
# account2 = BankAccount(0.0392, 380.00)


# account1.deposit(150.00).deposit(1_000.00).deposit(
#     1_347.00).withdraw(2_513.00).int_yld().disp_acc_info()
# account2.deposit(1001.17).deposit(1343.57).withdraw(25.04).withdraw(9999.99).withdraw(
#     571.73).withdraw(550.00).int_yld().disp_acc_info()  # should initiate a $5 insufficient funds fee


user1 = User('Kevin', 'kevin@email.com')
user1.display_user_balance()
user1.make_deposit(100)
user1.display_user_balance()
user1.make_withdrawal(25)
user1.display_user_balance()