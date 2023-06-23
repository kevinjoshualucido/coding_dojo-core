public class GorillaTest {
    public static void main(String[] args) {
        Gorilla ape = new Gorilla(100);
        System.out.println("Energy Level: " + ape.energyLevel);

        // throw something 3 times
        ape.throwSomething();
        ape.throwSomething();
        ape.throwSomething();
        System.out.println("Energy Level: " + ape.energyLevel);

        // eat bananas 2 times
        ape.eatBananas();
        ape.eatBananas();
        System.out.println("Energy Level: " + ape.energyLevel);

        // climb 1 time
        ape.climb();
        System.out.println("Energy Level: " + ape.energyLevel);
    }
}