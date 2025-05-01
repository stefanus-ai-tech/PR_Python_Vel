class LaguNode {
    String judulLagu;
    LaguNode selanjutnya; // Lagu setelah ini
    LaguNode sebelumnya; // Lagu sebelum ini

    LaguNode(String judulLagu) {
        this.judulLagu = judulLagu;
        // Awalnya, dia jomblo, belum punya koneksi
        this.selanjutnya = null;
        this.sebelumnya = null;
    }

    @Override
    public String toString() {
        // Biar pas di-print enak diliat
        return "🎵 " + judulLagu;
    }
}

// Kelas utama buat ngatur playlist pake Doubly Linked List
class PlaylistAnjay {
    LaguNode head; // Lagu pertama di playlist (pala)
    LaguNode tail; // Lagu terakhir di playlist (buntut)
    LaguNode laguSekarang; // Lagu yang lagi diputer atau dipilih
    boolean isCircular = false; // Status playlist muter terus apa nggak

    // Constructor: bikin playlist kosong melompong
    PlaylistAnjay() {
        this.head = null;
        this.tail = null;
        this.laguSekarang = null;
    }

    // Cek kalo playlistnya kosong, kayak hati mantan
    boolean isEmpty() {
        return head == null;
    }

    // Nambah lagu di paling belakang playlist
    void tambahLaguDiBelakang(String judul) {
        LaguNode laguBaru = new LaguNode(judul);
        System.out.println("Nambahin lagu: " + judul + " ke antrian paling belakang...");

        if (isEmpty()) {
            // Kalo kosong, dia jadi head sekaligus tail
            head = tail = laguBaru;
            laguSekarang = head; // Langsung set lagu pertama jadi lagu sekarang
            System.out.println("Ini lagu pertama, hore!");
        } else {
            // Kalo udah ada isinya, sambungin ke buntut
            tail.selanjutnya = laguBaru; // Buntut lama nunjuk ke lagu baru
            laguBaru.sebelumnya = tail; // Lagu baru nunjuk balik ke buntut lama
            tail = laguBaru; // Lagu baru sekarang jadi buntut
            System.out.println(judul + " udah masuk antrian, sabar ya!");
        }
        // Kalo circular, update koneksi ujung-ujungnya
        if (isCircular) {
            aturCircular();
        }
    }

    // Hapus lagu yang lagi dipilih (laguSekarang)
    void hapusLaguSekarang() {
        if (laguSekarang == null) {
            System.out.println("Waduh, ga ada lagu yang dipilih buat dihapus!");
            return;
        }

        System.out.println("Ngehapus lagu: " + laguSekarang.judulLagu + "... Bye bye!");
        LaguNode laguDihapus = laguSekarang;

        // --- Logika Hapus Node di Doubly Linked List ---
        // 1. Cek Node Sebelumnya
        LaguNode prevNode = laguDihapus.sebelumnya;
        // 2. Cek Node Sesudahnya
        LaguNode nextNode = laguDihapus.selanjutnya;

        // Pindahkan 'laguSekarang' dulu SEBELUM MENGHAPUS koneksi
        // Coba pindah ke lagu berikutnya, kalo ga ada ya ke sebelumnya
        if (nextNode != null && nextNode != head) { // Prioritaskan maju (kecuali kalo next itu head di circular)
            laguSekarang = nextNode;
        } else if (prevNode != null && prevNode != tail) { // Kalo ga bisa maju, coba mundur (kecuali kalo prev itu tail di circular)
             laguSekarang = prevNode;
        } else if (head == tail && head == laguDihapus) { // Kasus tinggal 1 lagu
             laguSekarang = null; // Playlist jadi kosong
             head = tail = null;
        } else {
            // Ini terjadi di circular kalo cuma sisa 1, atau kasus aneh lain
            // Pilih salah satu aja, misal head (jika tidak null)
             laguSekarang = (head != laguDihapus) ? head : null; // Kalo head bukan yg dihapus, pindah ke head, else null
             if (laguSekarang == null && tail != laguDihapus) laguSekarang = tail; // Coba tail kalo head dihapus
        }


        // 3. Update pointer 'selanjutnya' dari node SEBELUMNYA
        if (prevNode != null) {
            prevNode.selanjutnya = nextNode; // Node sebelum nunjuk ke node sesudah (skip node yg dihapus)
        } else {
            // Kalo ga ada node sebelumnya, berarti yg dihapus adalah HEAD
            head = nextNode; // Node sesudahnya jadi HEAD baru
        }

        // 4. Update pointer 'sebelumnya' dari node SESUDAHNYA
        if (nextNode != null) {
            nextNode.sebelumnya = prevNode; // Node sesudah nunjuk balik ke node sebelum (skip node yg dihapus)
        } else {
            // Kalo ga ada node sesudahnya, berarti yg dihapus adalah TAIL
            tail = prevNode; // Node sebelumnya jadi TAIL baru
        }

        // Kalo circular, benerin lagi sambungan ujung-ujungnya
        if (isCircular && head != null) { // Cek head != null krn bisa aja jadi kosong
            aturCircular();
             // Jika setelah hapus laguSekarang jadi null (misal krn tinggal 1 lagu dihapus),
             // dan playlist masih ada isinya, set laguSekarang ke head
             if(this.laguSekarang == null && head != null) {
                 this.laguSekarang = head;
             }
        } else if (head == null) { // Jika list jadi kosong
            isCircular = false; // Gak bisa circular kalo kosong
            this.laguSekarang = null;
        }

        System.out.println("Oke, " + laguDihapus.judulLagu + " udah dibuang!");
         if (laguSekarang != null) {
             System.out.println("Sekarang lagi di lagu: " + laguSekarang.judulLagu);
         } else {
             System.out.println("Playlist jadi kosong T_T");
         }
    }


    // Pindah ke lagu selanjutnya
    void nextLagu() {
        if (laguSekarang == null) {
            System.out.println("Playlist kosong, mau next ke mana bro?");
            return;
        }
        if (laguSekarang.selanjutnya != null) {
            laguSekarang = laguSekarang.selanjutnya;
            System.out.println("Pindah ke lagu selanjutnya: " + laguSekarang);
        } else {
            // Kalo udah di ujung dan bukan circular, ya stop
            // Kalo circular, dia otomatis ke head (sudah dihandle di aturCircular)
            System.out.println("Udah lagu terakhir nih.");
            if(isCircular) System.out.println("Balik lagi ke awal...");
        }
    }

    // Pindah ke lagu sebelumnya
    void prevLagu() {
        if (laguSekarang == null) {
            System.out.println("Playlist kosong, mau prev ke mana bro?");
            return;
        }
        if (laguSekarang.sebelumnya != null) {
            laguSekarang = laguSekarang.sebelumnya;
            System.out.println("Pindah ke lagu sebelumnya: " + laguSekarang);
        } else {
            // Kalo udah di awal dan bukan circular, ya stop
            // Kalo circular, dia otomatis ke tail (sudah dihandle di aturCircular)
            System.out.println("Udah lagu pertama nih.");
             if(isCircular) System.out.println("Muter ke paling belakang...");
        }
    }

    // Cetak semua lagu dari depan ke belakang
    void cetakPlaylistDariDepan() {
        System.out.println("\\n--- Playlist Saat Ini (Depan ke Belakang) ---");
        if (isEmpty()) {
            System.out.println("Kosong melompong...");
            return;
        }
        LaguNode current = head;
        int i = 1;
        // Loop sampe ketemu null (atau balik ke head kalo circular)
        do {
            System.out.print(i + ". " + current.judulLagu);
            if (current == laguSekarang) {
                System.out.print(" <-- LAGI DI SINI");
            }
            System.out.println();
            current = current.selanjutnya;
            i++;
        } while (current != null && current != head); // Berhenti kalo null ATAU balik ke head (circular)
        System.out.println("------------------------------------------\\n");
    }

     // Cetak semua lagu dari belakang ke depan
    void cetakPlaylistDariBelakang() {
        System.out.println("\\n--- Playlist Saat Ini (Belakang ke Depan) ---");
        if (isEmpty()) {
            System.out.println("Kosong melompong...");
            return;
        }
        LaguNode current = tail;
        int i = 1;
        // Loop sampe ketemu null (atau balik ke tail kalo circular)
        do {
            System.out.print(i + ". " + current.judulLagu);
            if (current == laguSekarang) {
                System.out.print(" <-- LAGI DI SINI");
            }
            System.out.println();
            current = current.sebelumnya;
            i++;
        } while (current != null && current != tail); // Berhenti kalo null ATAU balik ke tail (circular)
        System.out.println("------------------------------------------\\n");
    }

    // **BONUS: Bikin playlist jadi circular**
    void aktifkanCircular() {
        if (!isEmpty() && head != tail) { // Minimal ada 2 lagu buat circular
            this.isCircular = true;
            aturCircular();
            System.out.println("Playlist sekarang muter terus! Kayak hamster lari di roda.");
        } else if (head == tail && head != null) {
             this.isCircular = true;
             // Kalau cuma 1 lagu, next dan prev nunjuk ke diri sendiri
             head.selanjutnya = head;
             head.sebelumnya = head;
             System.out.println("Playlist cuma 1 lagu, muter di situ aja ya.");
        }
        else {
            System.out.println("Playlist kosong atau cuma 1 lagu, belum bisa dibikin circular.");
        }
    }

    void nonaktifkanCircular() {
         if (this.isCircular) {
            this.isCircular = false;
            // Putusin sambungan circularnya
            if (head != null) head.sebelumnya = null;
            if (tail != null) tail.selanjutnya = null;
            System.out.println("Playlist udah gak muter lagi. Normal.");
         } else {
             System.out.println("Playlist emang udah gak circular kok.");
         }
    }

    // Helper buat nyambungin ujung-ujungnya kalo circular
    private void aturCircular() {
        if (isCircular && head != null && tail != null) {
            tail.selanjutnya = head; // Buntut nyambung ke kepala
            head.sebelumnya = tail; // Kepala nyambung balik ke buntut
        }
         // else: kalo ga circular atau kosong, biarin aja (atau dihandle di nonaktifkanCircular)
    }


    // --- Main Method buat Demo ---
    public static void main(String[] args) {
        PlaylistAnjay playlistKu = new PlaylistAnjay();

        playlistKu.tambahLaguDiBelakang("Bohemian Rhapsody - Queen");
        playlistKu.tambahLaguDiBelakang("Stairway to Heaven - Led Zeppelin");
        playlistKu.tambahLaguDiBelakang("Hotel California - Eagles");
        playlistKu.tambahLaguDiBelakang("Smells Like Teen Spirit - Nirvana");

        playlistKu.cetakPlaylistDariDepan(); // Cetak awal
        System.out.println("Lagu sekarang: " + playlistKu.laguSekarang);

        playlistKu.cetakPlaylistDariBelakang();
        System.out.println("Lagu sekarang: " + playlistKu.laguSekarang);

        playlistKu.nextLagu(); // Pindah ke Led Zeppelin
        playlistKu.nextLagu(); // Pindah ke Eagles

        playlistKu.prevLagu(); // Balik ke Led Zeppelin
        playlistKu.cetakPlaylistDariDepan();

        playlistKu.hapusLaguSekarang(); // Hapus Led Zeppelin
        playlistKu.cetakPlaylistDariDepan(); // Cek setelah hapus

        System.out.println("Lagu sekarang: " + playlistKu.laguSekarang); // Harusnya Eagles
        playlistKu.nextLagu(); // Ke Nirvana
         System.out.println("Lagu sekarang: " + playlistKu.laguSekarang);
        playlistKu.nextLagu(); // Udah terakhir


        System.out.println("\\n=== AKTIFKAN CIRCULAR ===");
        playlistKu.aktifkanCircular();
        playlistKu.nextLagu(); // Dari Nirvana harusnya ke Queen (head)
        System.out.println("Lagu sekarang (setelah next di akhir circular): " + playlistKu.laguSekarang);
        playlistKu.prevLagu(); // Dari Queen harusnya ke Nirvana (tail)
        System.out.println("Lagu sekarang (setelah prev di awal circular): " + playlistKu.laguSekarang);
        playlistKu.cetakPlaylistDariDepan();

        System.out.println("\\n=== HAPUS DI CIRCULAR ===");
        playlistKu.prevLagu(); // Mundur ke Eagles
        playlistKu.hapusLaguSekarang(); // Hapus Eagles
        playlistKu.cetakPlaylistDariDepan();
        System.out.println("Lagu sekarang: " + playlistKu.laguSekarang); // Harusnya Queen atau Nirvana
        playlistKu.nextLagu();
        System.out.println("Lagu sekarang: " + playlistKu.laguSekarang);
        playlistKu.nextLagu();
         System.out.println("Lagu sekarang: " + playlistKu.laguSekarang); // Harusnya balik lagi


        System.out.println("\\n=== NONAKTIFKAN CIRCULAR ===");
        playlistKu.nonaktifkanCircular();
        playlistKu.nextLagu(); // Harusnya gak bisa muter lagi
         System.out.println("Lagu sekarang: " + playlistKu.laguSekarang);


    }
}
