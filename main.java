import java.util.Scanner;

public class main {
    public static void main(String[] args) {
        // Scanner anjai = new Scanner(System.in);
        // double number = anjai.nextDouble();
        // String name = anjai.next(); // return only 1 word
        // String line = anjai.nextLine(); // return one line

        // anjai.close();

        Scanner obj = new Scanner(System.in);
        System.out.println("Enter your modafuka name!");
        String nama = obj.nextLine();
        System.out.println("Enter your bloody age!");
        int age = obj.nextInt();
        System.out.println("Hello "+ nama + " you are " + age + " years old");
 
    }
}
