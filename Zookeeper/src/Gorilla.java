// subclass of superclass Mammal
public class Gorilla extends Mammal {
    public Gorilla(int energyLevel) {
        // call superclass' attribute method to set Gorilla's energyLevel default
        super(energyLevel);
    }

    // instructions doesn't specify to return a data type, so will use return type void
    // method doesn't need parameters
    // method itself has fixed method body variables
    public void throwSomething() {
        System.out.println("Gorilla has thrown something!");
        energyLevel -= 5;
    }

    public void eatBananas() {
        System.out.println("Gorilla enjoyed their banana!");
        energyLevel += 10;
    }

    public void climb() {
        System.out.println("Gorilla climbed a tree.");
        energyLevel -= 10;
    }
}
