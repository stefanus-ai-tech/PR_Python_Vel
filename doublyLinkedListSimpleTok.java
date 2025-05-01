// Class NodeAnjai ini representasi 1 titik data di linked list
class NodeAnjai {
    int data; // Data yang disimpen di node ini, kayak nilai 1, 2, 3 dsb
    NodeAnjai stlah, sblum; // stlah = sambungan ke node setelahnya, sblum = sambungan ke node sebelumnya

    // Constructor ini dipanggil kalo kita mau bikin Node baru
    NodeAnjai(int data){
        this.data = data; // Langsung simpen nilai data yang dikasih pas bikin node
    }
}

// Ini class utama buat doubly linked list
public class doublyLinkedListSimpleTok {
    NodeAnjai pala, buntut; // pala = node pertama (head), buntut = node terakhir (tail)

    // Kenapa ada pala dan buntut?
    // ➔ Supaya gampang kalau mau nambah data di depan atau belakang tanpa harus kelilingin seluruh list.
    // ➔ Operasinya jadi lebih cepet (O(1)) daripada harus cari satu-satu.

    // Method buat nambahin data baru ke belakang list
    void nambahin(int data){
        NodeAnjai NodeBaruCuy = new NodeAnjai(data); // Bikin node baru pake data yang dikasih
        if (pala == null){ // Cek dulu, kalo pala kosong, berarti listnya masih kosong
            pala = buntut = NodeBaruCuy; // Karena kosong, pala dan buntut langsung nunjuk ke node baru
            return; // Selesai nambah, ga perlu lanjut ke bawah
        }
        // Kalau udah ada isinya (list gak kosong)
        buntut.stlah = NodeBaruCuy; // Buntut lama sambung ke node baru (buntut.next = NodeBaru)
        NodeBaruCuy.sblum = buntut; // Node baru sambung balik ke buntut lama (biar 2 arah)
        buntut = NodeBaruCuy; // Update buntut ke node baru, karena dia sekarang jadi ujung
    }

    // Method buat cetak isi list dari depan (pala ke buntut)
    void cetakKeDepan(){
        NodeAnjai saatIniGengs = pala; // Mulai dari pala (head)

        // Loop selama belum ketemu null (null artinya udah abis)
        while (saatIniGengs != null) {
            System.out.print(saatIniGengs.data + " => "); // Cetak isi datanya
            saatIniGengs = saatIniGengs.stlah; // Geser ke node berikutnya (maju ke depan)
        }
        System.out.println(); // Biar setelah cetak semua, cursor pindah ke baris baru
    }

    // Method buat cetak isi list dari belakang (buntut ke pala)
    void cetakKeBelakang(){
        NodeAnjai saatIniGengs = buntut; // Mulai dari buntut (tail)

        // Loop selama belum ketemu null (null artinya udah abis ke arah belakang)
        while (saatIniGengs != null) {
            System.out.print(saatIniGengs.data + " => "); // Cetak isi datanya
            saatIniGengs = saatIniGengs.sblum; // Geser ke node sebelumnya (mundur ke belakang)
        }
        System.out.println(); // Pindah baris setelah cetak semua
    }
    
    // Program utama yang pertama dijalankan waktu jalanin file
    public static void main(String[] args){
        // Bikin objek linked list kosong
        doublyLinkedListSimpleTok daftar = new doublyLinkedListSimpleTok();

        // Masukin data satu per satu
        daftar.nambahin(1); // nambah angka 1
        daftar.nambahin(2); // nambah angka 2
        daftar.nambahin(3); // nambah angka 3

        // Print semua data dari depan
        daftar.cetakKeDepan();
        
        // Print semua data dari belakang
        daftar.cetakKeBelakang();
    }
}
