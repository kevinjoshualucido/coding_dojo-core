class BankAccount:
    all_instances = []

    def __init__(self, int_rate, bal):
        self.int_rate = int_rate
        self.bal = bal

    def deposit(self, amt):
        self.bal += amt
        print('Deposit:', round(self.bal, 2))
        return self

    def withdraw(self, amt):
        if self.bal < amt:
            print('Insufficient funds: Charging a 5.00 fee')
            self.bal -= 5
        else:
            self.bal -= amt
        print('Withdraw:', round(self.bal, 2))
        return self

    def disp_acc_info(self):
        print('Your balance is:', round(self.bal, 2))
        return self

    def int_yld(self):
        yielded_interest = self.bal * self.int_rate
        self.bal += yielded_interest
        print('Yielded interest:', round(yielded_interest, 2))
        return self
    
    


account1 = BankAccount(0.0431, 150.00)
account2 = BankAccount(0.0392, 380.00)


account1.deposit(150.00).deposit(1_000.00).deposit(1_347.00).withdraw(2_513.00).int_yld().disp_acc_info()
account2.deposit(1001.17).deposit(1343.57).withdraw(25.04).withdraw(9999.99).withdraw(571.73).withdraw(550.00).int_yld().disp_acc_info()  # should initiate a $5 insufficient funds fee
