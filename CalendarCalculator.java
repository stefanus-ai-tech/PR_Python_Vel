
import java.util.InputMismatchException;
import java.util.Scanner;

public class CalendarCalculator {

    private int currentDay;
    private int currentMonth;
    private int currentYear;

    public CalendarCalculator(int startDay, int startMonth, int startYear){
        if (!isValidDate(startDay, startMonth, startYear)){
            throw new IllegalArgumentException(
                String.format("Invalid starting date: %d-%02d-%02d", startYear, startMonth, startDay)
            );
        }
        this.currentDay = startDay;
        this.currentMonth = startMonth;
        this.currentYear = startYear;
    }

    public static boolean isValidDate(int day, int month, int year){
        if (year < 1){
            return false;
        }

        if (month < 1 || month > 12){
            return false;
        }
        int daysInMonth = getDaysInMonth(month, year); 
        return day >= 1 && day <= daysInMonth;
    }

    private static int getDaysInMonth(int month, int year){
        return switch (month) {
            case 4, 6, 9, 11 -> 30;
            case 2 -> isLeapYear(year)? 29:28;
            default -> 31;
        }; 
    }
    
    private static boolean isLeapYear(int year){
        return (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0);
    }

    public void addDays (int numberOfDaysToAdd){
        if (numberOfDaysToAdd > 0 ){
            for (int i = 0; i < numberOfDaysToAdd; i++) {
                stepForwardOneDay();   
            }
        } else if ( numberOfDaysToAdd < 0){
            for (int i = 0; i < Math.abs(numberOfDaysToAdd); i++) {
                stepBackwardOneDay();   
            }
        }
    }

    private void stepForwardOneDay() {
        int daysInCurrentMonth = getDaysInMonth(this.currentMonth, this.currentYear);
        if (this.currentDay < daysInCurrentMonth){
            this.currentDay++;
        } else {
            this.currentDay = 1;
            if (this.currentMonth < 12) {
                this.currentMonth++;
            } else {
                this.currentMonth = 1;
                this.currentYear++;
            }
        }
    }

    private void stepBackwardOneDay(){
        if (this.currentDay > 1){
            this.currentDay--;
        } else {
            if (this.currentMonth > 1){
                this.currentMonth--;
            } else {
                this.currentMonth = 12;
                this.currentYear--;
            }
            this.currentDay = getDaysInMonth(this.currentMonth, this.currentYear);
        }
    }

    public String getCurrentDateAsString(){
        return String.format("%02d-%02d-%04d", this.currentDay, this.currentMonth, this.currentYear);
    }

    public static void main(String[] args) {
        Scanner nyeken = new Scanner(System.in);
        int startYear = 0, startMonth = 0, startDay = 0, daysToAdd = 0;
        boolean validInput = false;

        System.out.println("------------ Calendar Calculator ---------------");

        while (!validInput){
            try {
                System.out.println("Enter Starting Year (e.g., 2024): ");
                startYear = nyeken.nextInt();
                System.out.println("Enter Starting Month (1-12): ");
                startMonth = nyeken.nextInt();
                System.out.println("Enter Starting Days (1-31): ");
                startDay = nyeken.nextInt();

                if (isValidDate(startDay, startMonth, startYear)){
                    validInput = true;
                } else {
                    System.out.println("Error: Date ga valid bos, coba lagih!");
                } 
            } catch (InputMismatchException e) {
                System.out.println("Error: Masukin angka, jangan yang lain, hehe");
                nyeken.next();

            } catch (Exception e) {
                System.out.println("Error: unexpected error" + e.getMessage());
                nyeken.next();
            }

        }

        validInput = false;

        while (!validInput){
            try {
                System.out.println("Enter number of days to add/subtract (+/-): ");
                daysToAdd = nyeken.nextInt();
                validInput = true;
            } catch (InputMismatchException e) {
                System.err.println("Please enter an integer number");
                nyeken.next();
            } catch (Exception e) {
                System.err.println("Error: unexpected error" + e.getMessage());
                nyeken.next();
            } 
        }

        try {
            CalendarCalculator calculator = new CalendarCalculator(startDay, startMonth, startYear);

            System.out.println("\nStarting Date: " + calculator.getCurrentDateAsString());
            System.out.println("Days to Add/Subtract: " + daysToAdd);

            calculator.addDays(daysToAdd);

            System.out.println("------------------------------");
            System.out.println("Calculated Date: " + calculator.getCurrentDateAsString());
            System.out.println("------------------------------");
        } catch (IllegalArgumentException e) {
            System.err.println("Error initializing calculator: " + e.getMessage());
        } catch (Exception e) {
            System.err.println("Error: unexpected error" + e.getMessage());
        } finally{
            nyeken.close();
            System.out.println("Calculator finished!");
        }

    }
}
