public class Mammal {
    // class attributes/member variable
    public int energyLevel = 100;

    // getter
    public int displayEnergy() {
        System.out.println("Energy Level: " + energyLevel);
        return energyLevel;
    }

    // we want to set the energyLevel as a default
    // logic, don't need setter because all objects should have a set default energy level
    // constructor method
    public Mammal(int energyLevel) {
        this.energyLevel = energyLevel;
    }
}