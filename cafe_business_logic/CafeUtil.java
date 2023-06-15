import java.util.ArrayList;

public class CafeUtil {
    /*
     * Calculate how many drinks they need after 10 weeks, write a method that sums
     * together every consecutive integer from 1 to 10 and returns the sum
     */
    public int getStreakGoal() {
        int sum = 0;
        for (int i = 0; i <= 10; i++) {
            sum += i;
        }
        return sum;
    }

    /*
     * Given an array of item prices from an order, sum all of the prices in the
     * array and return the total
     */
    public double getOrderTotal(double[] lineItems) {
        double sum = 0;
        for (double itemPrice : lineItems) {
            sum += itemPrice;
        }
        return sum;
    }

    /*
     * Given an ArrayList of menu items (strings), print out each index and menu
     * item.
     */
    public void displayMenu(ArrayList<String> menu) {
        for (int menuItem = 0; menuItem < menu.size(); menuItem++) {
            String name = menu.get(menuItem);
            System.out.println(menuItem + " " + name);
        }
    }

    public void addCustomer(ArrayList<String> customers) {
        System.out.println("Please enter your name: ");
        String userName = System.console().readLine();
        String greeting = String.format("Hello there, %s!", userName);
        System.out.println(greeting);
        String customerLine = String.format("There are %s people ahead of you in line", customers.size());
        customers.add(userName);
        System.out.println(customerLine);
    }
}
