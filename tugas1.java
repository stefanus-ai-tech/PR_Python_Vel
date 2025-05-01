
import java.util.LinkedList;


public class tugas1 {
    public static void main(String[] args) {
        // soal nomor 1
        int jumlahBaris = 12;
        System.out.println("1. Ini adalah jumlah baris: " + jumlahBaris);
        
        // soal nomor 2
        String kalimatBaru = "Saya anak UT";
        System.out.println("2. Ini adalah kalimat baru: "+ kalimatBaru);

        // soal nomor 3
        Integer[] empatAngka = new Integer[4];
        empatAngka[0] = 07;
        empatAngka[1] = 10;
        empatAngka[2] = 20;
        empatAngka[3] = 23;
        System.out.print("3. Ini adalah tampilan empatAngka: ");
        for (int i : empatAngka) {
            System.out.print(i+"\t");
        }
        System.out.println();

        Integer[][] limaAngka = new Integer[2][2];
        limaAngka[0][0] = 1;
        limaAngka[0][1] = 1;
        limaAngka[1][0] = 1;
        limaAngka[1][1] = 1; 

        for (Integer[] i : limaAngka){
            for (Integer j : i){
                System.out.println(j);
            }
        }
        

        // soal nomor 4
        String[][] alfabet = {
            {"p", "s", "n"},
            {"w", "l", "b"},
            {"f", "r", "e"}
        };

        System.out.print("4. Ini adalah tampilan alfabet: ");
        for (int i = 0; i < alfabet.length; i++) {
            for (int j = 0; j < alfabet[i].length; j++) {
                System.out.print(alfabet[i][j]+"\t");
            }
        }
        System.out.println();

        // for (String[] i : alfabet){
        //     for (String j : i) {
        //         System.out.println(j);
        //     }
        // }

        // soal nomor 5

        LinkedList<String> listAngka = new LinkedList<>();
        listAngka.add("26");
        listAngka.add("08");
        listAngka.add("23");
        listAngka.add("24");
        listAngka.add("26");

        System.out.println("5. Ini adalah linked list listAngka: " + listAngka);




    }
}
