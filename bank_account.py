class BankAccount:
    all_transc = []

    def __init__(self, int_rate, bal):
        self.int_rate = int_rate
        self.bal = bal

    def deposit(self, amt):
        self.bal += amt
        print('Deposit:', self.bal)
        return self

    def withdraw(self, amt):
        self.bal -= amt
        print('Withdraw:', self.bal)
        return self

    def disp_acc_info(self):
        print('Your balance is:', round(self.bal, 2))
        return self

    def int_yld(self):
        yielded_interest = self.bal * self.int_rate
        self.bal += yielded_interest
        print('Yielded interest:', round(yielded_interest, 2))
        return self
    
    @classmethod
    def get_transc(cls):
        print(cls.all_transc)


account1 = BankAccount(0.0431, 150.00)
account2 = BankAccount(0.0392, 380.00)


account1.deposit(150.00).deposit(1_000.00).deposit(1_347.00).withdraw(2_513.00).int_yld().disp_acc_info()
account2.deposit(1001.17).deposit(1343.57).withdraw(25.04).withdraw(9.99).withdraw(571.73).withdraw(550.00).int_yld().disp_acc_info()

account1.get_transc()
account2.get_transc()
