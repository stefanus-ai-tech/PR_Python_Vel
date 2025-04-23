import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Random;
import java.util.Scanner;

public class hangman {

    public static List<Integer> findCharIndices(Character search_char, String word){
        List<Integer> indices = new ArrayList<>();
        
        for (int i = 0; i < word.length(); i++) {
            if (word.charAt(i) == search_char) {
                indices.add(i);
            }
        }
        return (indices);
    }
    public static void main(String[] args) {
        System.out.println("Welcome to the hangman game! choose a letter from the chosen word until complete,choose wrong letter then the Man will be hanged");
        List<String> word_list = Arrays.asList(
    "quasar", "verdant", "eclipse", "synthesis", "gargantuan",
    "labyrinth", "ephemeral", "crescendo", "radiance", "solstice",
    "chrysalis", "eloquent", "resonance", "paradox", "serendipity",
    "luminescent", "mosaic", "zephyr", "voyage", "allegory",
    "cascade", "inertia", "jubilant", "myriad", "odyssey",
    "palindrome", "reverie", "silhouette", "tranquil", "vortex",
    "whimsy", "xenith", "yonder", "zealot", "amethyst",
    "buoyant", "crystalline", "diaphanous", "euphony", "fugue",
    "gossamer", "halcyon", "incandescent", "jubilance", "kaleidoscope",
    "luminous", "mellifluous", "nebulous", "opalescent", "pristine",
    "quintessence", "resplendent", "sublime", "talisman", "umbra",
    "verdure", "wanderlust", "xylophone", "yearning", "zenith"
);
        Random rand = new Random();
        String choosen_word = word_list.get(rand.nextInt(word_list.size()));
        // System.out.println("The word in the question is: " + choosen_word); //for debugging
        char[] placeholder_string = new char[choosen_word.length()];
        for (int i = 0; i < placeholder_string.length; i++) {
            placeholder_string[i] = '_';
        }
        int lives = 10;
        Boolean game_over = false;
        List<Character> guessedList = new ArrayList<>();

        Scanner scanned = new Scanner(System.in);

        while (!game_over){
            System.out.println("Your current lives is: " + lives);
            System.out.println(Arrays.toString(placeholder_string));
            Character choice = null;
            while (true) { 
                
                System.out.println("Guess a letter that is correct to the word: ");
                String user_choice = scanned.next();
                if (user_choice.length() != 1) {
                    System.out.println("Please enter a single character.");
                    continue;
                }
                choice = user_choice.charAt(0);
                break;
              
            }
            if(guessedList.contains(choice)){
                System.out.println("The letter "+ choice + " has been guessed. Try again!");
            }
            guessedList.add(choice);

            if(choosen_word.indexOf(choice) != -1){
                System.out.println("Right");
                List<Integer> foundAt = findCharIndices(choice, choosen_word);

                for (int index : foundAt) {
                    placeholder_string[index] = choice;
                }

                // System.out.println("Current word: " + String.valueOf(placeholder_string));
                System.out.println("====================");
                if (String.valueOf(placeholder_string).indexOf('_') == -1) {
                    game_over = true;
                    System.out.println("====================");
                    System.out.println("Congrats, you win!");
                    System.out.println("The word was: " + choosen_word);
                    System.out.println("====================");
                    scanned.close();
                }
            } else{
                System.out.println("Wrong");
                lives--;
                System.out.println("====================");

                if (lives == 0) {
                    game_over = true;
                    System.out.println("====================");
                    System.out.println("Damn, you lose!");
                    System.out.println("The word was: " + choosen_word);
                    System.out.println("====================");
                    scanned.close();
                }
            }

        }
    }
}
