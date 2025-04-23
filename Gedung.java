import java.util.ArrayList;

public class Gedung {
    public static void main(String[] args) {
        // 2 lantai, 5 ruangan per lantai

        // Inisialisasi setiap ruangan denagn ArrayList kosong
        @SuppressWarnings("unchecked") // untuk menonaktifkan warning saat menggunakan ArrayList 
        // Karena secara umum Java tidak mendukung generic array creation

        ArrayList<String>[][] gedungA = new ArrayList[2][5];

        for (int lantai = 0; lantai < gedungA.length; lantai++){
            for (int ruangan = 0; ruangan < gedungA[lantai].length; ruangan++){
                gedungA[lantai][ruangan] = new ArrayList<>();

                // Untuk id setiap barang
                String id = "GdgA-L" + (lantai + 1) + "R" + (ruangan + 1);

                // Menambahkan 4 barang di setiap ruangan dan lantai
                gedungA[lantai][ruangan].add("Lampu ID: " + id);
                gedungA[lantai][ruangan].add("Lemari ID: "+ id);
                gedungA[lantai][ruangan].add("Kipas ID: " + id);
                gedungA[lantai][ruangan].add("Saklar ID: " + id);
            }
        }

        // Contoh cara mengakses dan mencetak semua barang dengan id yang tertera
        for (int lantai = 0; lantai < gedungA.length; lantai++){
            System.out.println("Lantai" + (lantai + 1) + ":");
            for (int ruangan = 0; ruangan < gedungA[lantai].length; ruangan++){
                System.out.println("Ruangan" + (ruangan + 1) + ": "+ gedungA[lantai][ruangan]);
            }
        }


    }
}
