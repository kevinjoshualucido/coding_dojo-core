public class BatTest {
    public static void main(String[] args) {
        Bat batty = new Bat();

        // attack 3 towns
        batty.attackTown();
        batty.attackTown();
        batty.attackTown();
        System.out.println("Battery Level: " + batty.energyLevel);

        // eat 2 humans
        batty.eatHumans();
        batty.eatHumans();
        System.out.println("Battery Level: " + batty.energyLevel);

        // fly 2 times
        batty.fly();
        batty.fly();
        System.out.println("Battery Level: " + batty.energyLevel);
    }
}
