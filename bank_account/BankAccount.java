public class BankAccount {
    // Info on a Bank Account
    private double checkingBalance;
    private double savingsBalance;

    // Totals of user
    public static int numberOfAccounts;
    public static double totalMoneyStored;

    // Add an account
    public void totalAccounts() {
        BankAccount.numberOfAccounts += 1;
    }

    // Getter: Check user's checking account balance
    public double getCheckingBalance() {
        return this.checkingBalance;
    }

    // Method to deposit money to either checking or savings
    // Amount added to 'totalMoneyStored'
    public void deposit(double amount, String account) {
        if (account.equals("checking")) {
            this.checkingBalance += amount;
        } else if (account.equals("savings")) {
            this.savingsBalance += amount;
        }
        BankAccount.totalMoneyStored += amount;
    }

    // Method to withdraw money to either checking or savings
    // Amount deducted from 'totalMoneyStored'
    public void withdraw(double amount, String account) {
        // Check to see if user has sufficient funds
        boolean canWithdraw = false;
        if (account.equals("checking")) {
            if (this.checkingBalance - amount >= 0) {
                canWithdraw = true;
                this.checkingBalance -= amount;
            }
        } else if (account.equals("savings")) {
            if (this.savingsBalance - amount >= 0) {
                canWithdraw = true;
                this.savingsBalance -= amount;
            }
        }
        if (canWithdraw) {
            BankAccount.totalMoneyStored -= amount;
        } else {
            System.out.println("-- Insufficient funds. --");
        }
    }

    public void displayAccountBalance() {
        System.out.println(String.format("Checking: $%.2f    Savings: $%.2f", this.checkingBalance, this.savingsBalance));
    }

}