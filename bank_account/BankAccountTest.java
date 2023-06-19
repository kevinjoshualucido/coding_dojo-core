class BankAccountTest {
    public static void main(String[] args) {
        BankAccount ba = new BankAccount();
        ba.deposit(100.49, "checking");
        ba.deposit(3.00, "savings");
        ba.displayAccountBalance();

        System.out.println(BankAccount.totalMoneyStored);

        ba.withdraw(50, "checking");
        ba.withdraw(50, "savings");
        ba.displayAccountBalance();

        System.out.println(BankAccount.totalMoneyStored);

        BankAccount ba2 = new BankAccount();
        ba2.deposit(3, "checking");
        ba2.deposit(99, "savings");
        ba2.displayAccountBalance();
        ba2.withdraw(50, "checking");
    }
}