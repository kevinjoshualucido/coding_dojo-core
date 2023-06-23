public class Bat extends Mammal {
    public Bat() {
        // default energy level 300, override
        super(300);
        displayEnergy();
    }

    public void fly() {
        System.out.println("Bat took off!");
        energyLevel -= 50;
    }

    public void eatHumans() {
        System.out.println("AGGHH!");
        energyLevel += 25;
    }

    public void attackTown() {
        System.out.println("The town is on fire...");
        energyLevel -= 100;
    }
}
