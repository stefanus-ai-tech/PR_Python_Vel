---

**Seri Latihan JavaScript Dasar - Membangun Fondasi**

Tujuan dari latihan ini adalah untuk membiasakan Anda dengan sintaks dasar JavaScript, perulangan (`loop`), kondisi (`if/else`), fungsi, dan manipulasi data dasar seperti string dan array. Kerjakan soal-soal ini secara berurutan.

---

**Soal 1: Perkenalan dengan Output dan Loop Sederhana**

*   **Tujuan:** Mengerti cara menampilkan output dan membuat perulangan paling dasar.
*   **Tugas:** Buat kode JavaScript menggunakan `loop` (`for`) untuk menghasilkan output berikut di console:
    ```
    Halo JavaScript!
    Halo JavaScript!
    Halo JavaScript!
    Halo JavaScript!
    Halo JavaScript!
    ```
*   **Tips:** Gunakan `console.log()` untuk menampilkan teks. Tentukan berapa kali perulangan perlu dijalankan.

---

**Jawaban***

const a = "Halo"
const b = "JavaScript!"

for (let i = 0; i <= 4; i++) {
  console.log(`${a} ${b}`)
}

---

**Soal 2: Loop dengan Angka Berurutan**

*   **Tujuan:** Memahami cara menggunakan variabel counter dalam loop.
*   **Tugas:** Buat kode JavaScript menggunakan `loop` (`for`) untuk menampilkan angka 1 hingga 5 di console, masing-masing di baris baru:
    ```
    1
    2
    3
    4
    5
    ```
*   **Tips:** Perhatikan nilai awal, kondisi berhenti, dan penambahan (increment) pada `for loop`.

---

 **Jawaban**
 
 for (let i = 0; i <= 4; i++) {
  console.log(i+1)
}

---

**Soal 3: Pengenalan Kondisi (if/else) dalam Loop**

*   **Tujuan:** Menggabungkan loop dengan logika kondisional sederhana.
*   **Tugas:** Buat kode JavaScript menggunakan `loop` (`for`) yang mengiterasi angka dari 1 hingga 5. 
Untuk setiap angka, cetak apakah angka tersebut "Kecil" (jika kurang dari atau sama dengan 3) atau 
"Besar" (jika lebih dari 3). Output yang diharapkan:
    ```
    Angka 1 adalah Kecil
    Angka 2 adalah Kecil
    Angka 3 adalah Kecil
    Angka 4 adalah Besar
    Angka 5 adalah Besar
    ```
*   **Tips:** Gunakan `if...else` di dalam `loop` untuk memeriksa nilai angka pada setiap iterasi. Manfaatkan *template literals* (backticks `` `${variabel}` ``) untuk membuat string output lebih mudah dibaca.

---

**Jawaban** 

let status = {};

for (let i = 1; i <= 5; i++) {
  
  
  if (i <= 3){
    status = "Kecil";
  } else {
    status = "Besar";
  }
  console.log(`Angka ${i} adalah ${status}`);
}
---

**Soal 4: Menggunakan Modulo dan Kondisi (Genap/Ganjil)**

*   **Tujuan:** Memperkenalkan operator modulo (`%`) untuk logika umum seperti cek genap/ganjil. Mirip dengan contoh Soal 2 Anda.
*   **Tugas:** Buat kode JavaScript menggunakan `loop` (`for`) untuk angka dari 0 hingga 5. Untuk setiap angka, tentukan dan cetak apakah bilangan tersebut genap atau ganjil. Output yang diharapkan:
    ```
    Bilangan 0 adalah bilangan genap
    Bilangan 1 adalah bilangan ganjil
    Bilangan 2 adalah bilangan genap
    Bilangan 3 adalah bilangan ganjil
    Bilangan 4 adalah bilangan genap
    Bilangan 5 adalah bilangan ganjil
    ```
*   **Tips:** Ingat, bilangan genap adalah bilangan yang habis dibagi 2 (sisa pembagiannya 0). Gunakan operator `%`.

---
**Jawaban**
let status = {};

for (let i = 0; i <= 5; i++) {
  
  
  if (i % 2 == 0){
    status = "genap";
  } else {
    status = "ganjil";
  }
  console.log(`Bilangan ${i} adalah bilangan ${status}`);
}

---

**Soal 5: Mengontrol Alur Loop (break)**

*   **Tujuan:** Memahami cara menghentikan loop sebelum selesai secara normal menggunakan 
`break`. Mirip dengan contoh Soal 3 Anda.
*   **Tugas:** Buat kode JavaScript menggunakan `loop` (`for`) untuk angka dari 0 hingga 9.
 Periksa setiap angka. Jika angka tersebut ganjil, cetak pesan bahwa program berhenti dan hentikan loop. 
 Jika genap, cetak bahwa bilangan itu genap. Output yang diharapkan:
    ```
    Bilangan 0 adalah bilangan genap
    Bilangan 1 adalah bilangan ganjil, program berhenti.
    ```
*   **Tips:** Gunakan `if` untuk memeriksa kondisi ganjil. Jika terpenuhi, cetak pesan dan gunakan `break;` 
untuk keluar dari loop.



---
**Jawaban**

let status = {};
for (let i = 0; i <= 9; i++) {
  if (i % 2 == 0){
    status = "genap";
  } else {
    status = "ganjil";
  }
  let text = `Bilangan ${i} adalah bilangan ${status}`;
  let text_2 = ", program berhenti.";
  if ( status == "ganjil" ) {
    console.log(`${text}${text_2}`);
    break;
  } else {
    console.log(text);
  }
 
}

---

**Soal 6: Loop Bersarang (Nested Loop) - Membuat Pola Sederhana**

*   **Tujuan:** Mengerti cara kerja loop di dalam loop untuk membuat struktur yang lebih kompleks 
seperti pola atau tabel.
*   **Tugas:** Buat kode JavaScript menggunakan *nested loop* (loop di dalam loop) untuk menghasilkan
pola bintang segitiga siku-siku seperti berikut:
    ```
    *
    **
    ***
    ****
    *****
    ```
*   **Tips:** Loop luar akan mengontrol jumlah baris. Loop dalam akan mengontrol 
jumlah bintang yang dicetak per baris. Gunakan `console.log()` untuk pindah baris setelah 
loop dalam selesai. Anda mungkin perlu membangun string di dalam loop dalam sebelum mencetaknya.


---
**Jawaban**
const bintang = "*";
const batas = 4;
let cetak = {};

for (let i = 0; i <= batas; i++){
  for (let j = batas-i; j <= batas; j++){
    process.stdout.write(bintang);
  }
  process.stdout.write(`\n`);
}
---

**Soal 7: Pengenalan Fungsi (Function)**

*   **Tujuan:** Memahami cara membuat dan memanggil fungsi sederhana untuk melakukan tugas spesifik.
*   **Tugas:** Buat sebuah *fungsi* JavaScript bernama `sapaPengguna` yang menerima satu argumen (
parameter) berupa `nama` (string). Fungsi ini harus mencetak pesan sapaan ke console.
    Contoh pemanggilan dan output:
    ```javascript
    sapaPengguna("Budi"); // Output: Halo, Budi! Selamat datang!
    sapaPengguna("Ani");  // Output: Halo, Ani! Selamat datang!
    ```
*   **Tips:** Gunakan keyword `function` untuk mendefinisikan fungsi. Gunakan parameter di dalam 
fungsi. Panggil fungsi dengan memberikan nilai argumen.

---
**Jawaban**


function sapaPengguna(nama){
  console.log(`Halo, ${nama}! Selamat datang!`)
}

sapaPengguna("Budi");
sapaPengguna("Ani");


---

**Soal 8: Fungsi dengan Nilai Kembali (Return Value)**

*   **Tujuan:** Memahami fungsi yang tidak hanya melakukan aksi, tetapi juga mengembalikan sebuah nilai 
hasil perhitungan atau pemrosesan.
*   **Tugas:** Buat sebuah fungsi JavaScript bernama `hitungLuasPersegiPanjang` yang menerima dua argumen: 
`panjang` dan `lebar`. Fungsi ini harus *mengembalikan* (return) hasil perhitungan luasnya.
    Contoh pemanggilan dan penggunaan:
    ```javascript
    let panjangTanah = 10;
    let lebarTanah = 5;
    let luasTanah = hitungLuasPersegiPanjang(panjangTanah, lebarTanah);
    console.log("Luas tanah adalah:", luasTanah); // Output: Luas tanah adalah: 50

    console.log(hitungLuasPersegiPanjang(8, 3)); // Output: 24
    ```
*   **Tips:** Gunakan keyword `return` di dalam fungsi untuk mengirimkan hasil kembali ke kode yang memanggilnya.

---

**Jawaban**
function hitungLuasPersegiPanjang(panjangTanah, lebarTanah){
  return (panjangTanah * lebarTanah);
}

let panjangTanah = 10;
let lebarTanah = 5;
let luasTanah = hitungLuasPersegiPanjang(panjangTanah, lebarTanah);
console.log("Luas tanah adalah :", luasTanah); 
console.log(hitungLuasPersegiPanjang(8,3));

---

**Soal 9: Pengenalan Array dan Iterasi Array**

*   **Tujuan:** Memahami cara membuat array (daftar nilai) dan cara mengakses setiap elemen di dalamnya menggunakan loop.
*   **Tugas:**
    1.  Buat sebuah array bernama `daftarBuah` yang berisi nama-nama buah: "Apel", "Jeruk", "Mangga", "Pisang".
    2.  Gunakan `loop` (`for` atau `for...of`) untuk mencetak setiap nama buah dalam array ke console, satu per baris.
    Output yang diharapkan:
    ```
    Apel
    Jeruk
    Mangga
    Pisang
    ```
*   **Tips:** Array di JavaScript dibuat dengan kurung siku `[]`. Anda bisa mengakses elemen berdasarkan indeks 
(mulai dari 0) atau menggunakan loop `for...of` yang lebih modern untuk iterasi elemen secara langsung.

---
**Jawaban**

const daftarBuah = ["Apel", "Jeruk", "Mangga", "Pisang"];

for (let i = 0; i < daftarBuah.length; i++){
  console.log(daftarBuah[i]);
}

---

**Soal 10: Fungsi yang Memproses Array**

*   **Tujuan:** Menggabungkan fungsi dan array. Membuat fungsi yang menerima array sebagai 
input dan melakukan sesuatu dengannya.
*   **Tugas:** Buat sebuah fungsi bernama `cetakSemuaElemen` yang menerima satu argumen berupa 
`array`. Fungsi ini harus mencetak semua elemen dalam array tersebut ke console, sama seperti Soal 9.
    Contoh pemanggilan:
    ```javascript
    let angka = [10, 20, 30];
    let nama = ["Adi", "Bima", "Citra"];

    cetakSemuaElemen(angka);
    // Output:
    // 10
    // 20
    // 30

    cetakSemuaElemen(nama);
    // Output:
    // Adi
    // Bima
    // Citra
    ```
*   **Tips:** Ini menggabungkan konsep dari Soal 7 (fungsi) dan Soal 9 (iterasi array).

---
**Jawaban**

function cetakSemuaElemen(array){
  for (let i = 0; i < array.length; i ++){
    console.log(array[i]);
  }
}

let angka = [10, 20, 30];
let nama = ["Adi", "Bima", "Citra"];

cetakSemuaElemen(angka);
cetakSemuaElemen(nama);

---

**Praktik Terbaik yang Perlu Diingat (Best Practices):**

1.  **Nama Variabel dan Fungsi yang Jelas:** Gunakan nama yang deskriptif (misal: `hitungLuas` lebih baik dari `hl`, 
`namaPengguna` lebih baik dari `n`). Gunakan *camelCase* (kata kedua dan seterusnya diawali huruf kapital: 
`namaVariabelContoh`).

2.  **Komentar:** Tambahkan komentar (`//` untuk satu baris, `/* */` untuk banyak baris) untuk menjelaskan 
bagian kode yang mungkin kompleks atau tujuannya tidak langsung jelas.

3.  **Konsistensi Kode:** Jaga gaya penulisan kode Anda konsisten (misal: penempatan kurung kurawal `{ }`, 
penggunaan spasi).

4.  **Gunakan `const` dan `let`:** Gunakan `const` untuk variabel yang nilainya tidak akan berubah setelah 
diinisialisasi. Gunakan `let` untuk variabel yang nilainya mungkin perlu diubah. Hindari `var` sebisa mungkin 
di kode modern.

5.  **Fungsi Fokus:** Usahakan setiap fungsi memiliki satu tanggung jawab utama yang jelas.

---

Baik, mari kita tingkatkan level kesulitannya ke arah yang lebih relevan untuk calon *software developer*. 
Soal-soal berikut akan menyentuh konsep yang lebih dalam seperti struktur data, pemrograman asinkron, 
OOP (Object-Oriented Programming), algoritma dasar, dan praktik pengkodean yang baik.

---

**Seri Latihan JavaScript Tingkat Menengah ke Mahir - Persiapan Software Developer**

Tujuan latihan ini adalah memperdalam pemahaman tentang konsep JavaScript lanjutan, struktur data, 
pola desain umum, penanganan operasi asinkron, dan penulisan kode yang bersih, modular, dan efisien.

---

**Soal 11: Manipulasi Array Tingkat Lanjut (map, filter, reduce)**

*   **Tujuan:** Menguasai *higher-order functions* pada Array untuk pemrosesan data yang efisien dan deklaratif.
*   **Tugas:** Diberikan sebuah array objek yang merepresentasikan daftar produk:
    ```javascript
    const produk = [
      { id: 1, nama: "Laptop Gaming", kategori: "Elektronik", harga: 15000000, stok: 5 },
      { id: 2, nama: "Keyboard Mechanical", kategori: "Aksesoris Komputer", harga: 1200000, stok: 15 },
      { id: 3, nama: "Monitor Ultrawide", kategori: "Elektronik", harga: 8500000, stok: 3 },
      { id: 4, nama: "Mouse Wireless", kategori: "Aksesoris Komputer", harga: 350000, stok: 25 },
      { id: 5, nama: "Smartphone Flagship", kategori: "Elektronik", harga: 12000000, stok: 8 },
    ];
    ```
    Buatlah sebuah fungsi `analisisProduk(dataProduk)` yang:
    1.  Menggunakan `filter` untuk mendapatkan produk dalam kategori "Elektronik".
    2.  Menggunakan `map` pada hasil filter untuk membuat array baru yang hanya berisi nama dan harga 
	produk elektronik tersebut.
    3.  Menggunakan `reduce` pada array produk elektronik (hasil filter langkah 1) untuk menghitung total 
	nilai inventaris (harga * stok) semua produk elektronik.
    4.  Fungsi ini harus mengembalikan sebuah objek yang berisi:
        *   `namaHargaElektronik`: Array hasil langkah 2.
        *   `totalNilaiElektronik`: Angka hasil langkah 3.
*   **Contoh Output (berdasarkan data di atas):**
    ```json
    {
      "namaHargaElektronik": [
        { "nama": "Laptop Gaming", "harga": 15000000 },
        { "nama": "Monitor Ultrawide", "harga": 8500000 },
        { "nama": "Smartphone Flagship", "harga": 12000000 }
      ],
      "totalNilaiElektronik": 197500000 // (15jt*5) + (8.5jt*3) + (12jt*8)
    }
    ```
*   **Tips:** Gabungkan pemanggilan `filter`, `map`, dan `reduce` secara berantai jika memungkinkan 
untuk kode yang lebih ringkas.

---

**Soal 12: Bekerja dengan Objek Kompleks dan Destructuring**

*   **Tujuan:** Memahami cara mengakses dan memanipulasi properti dalam objek bersarang (nested objects) dan menggunakan *destructuring assignment* untuk kode yang lebih bersih.
*   **Tugas:** Diberikan objek konfigurasi berikut:
    ```javascript
    const konfigurasiAplikasi = {
      namaApp: "Aplikasi Super",
      versi: "1.2.0",
      pengaturan: {
        tema: "gelap",
        bahasa: "id",
        notifikasi: {
          email: true,
          push: false,
          levelSuara: 8
        }
      },
      penggunaAktif: {
        id: "usr001",
        nama: "Citra Kirana",
        preferensi: {
          iklan: false,
          newsletter: true
        }
      }
    };
    ```
    Buat sebuah fungsi `infoPenggunaDanNotif(konfig)` yang menerima objek konfigurasi. Fungsi ini harus menggunakan *destructuring assignment* (baik pada parameter fungsi maupun di dalam fungsi) untuk mengekstrak informasi berikut dan mengembalikannya dalam sebuah string deskriptif:
    "Pengguna '[Nama Pengguna]' (ID: [ID Pengguna]) menggunakan tema '[Tema]' dengan notifikasi email [aktif/nonaktif] dan notifikasi push [aktif/nonaktif]."
*   **Contoh Output (berdasarkan data di atas):**
    ```
    "Pengguna 'Citra Kirana' (ID: usr001) menggunakan tema 'gelap' dengan notifikasi email aktif dan notifikasi push nonaktif."
    ```
*   **Tips:** Gunakan destructuring bersarang untuk mengakses properti seperti `nama` dari `penggunaAktif` atau `email` dari `notifikasi`. Gunakan operator ternary (`kondisi ? nilai_jika_true : nilai_jika_false`) untuk mengubah boolean `true`/`false` menjadi string "aktif"/"nonaktif".

---

**Soal 13: Pemrograman Asinkron dengan Promises**

*   **Tujuan:** Memahami konsep dasar operasi asinkron dan cara menanganinya menggunakan Promises.
*   **Tugas:** Buat sebuah fungsi `ambilDataPengguna(userId)` yang *mensimulasikan* pengambilan data pengguna dari API.
    1.  Fungsi ini harus mengembalikan sebuah `Promise`.
    2.  Di dalam Promise, gunakan `setTimeout` untuk menunda eksekusi selama 1 detik (1000 ms) untuk simulasi latensi jaringan.
    3.  Setelah penundaan:
        *   Jika `userId` adalah angka positif, *resolve* Promise dengan objek pengguna (misal: `{ id: userId, nama: "Pengguna " + userId }`).
        *   Jika `userId` bukan angka positif (misal: 0, negatif, atau tipe data lain), *reject* Promise dengan pesan error "ID Pengguna tidak valid".
    4.  Panggil fungsi `ambilDataPengguna` dengan ID yang valid (misal: 123) dan gunakan `.then()` untuk mencetak data pengguna jika berhasil. Gunakan `.catch()` untuk mencetak pesan error jika gagal.
    5.  Panggil lagi fungsi `ambilDataPengguna` dengan ID yang tidak valid (misal: -5) dan tangani hasilnya dengan `.then()` dan `.catch()`.
*   **Tips:** Ingat struktur dasar `new Promise((resolve, reject) => { ... })`.

---

**Soal 14: Pemrograman Asinkron dengan async/await**

*   **Tujuan:** Menggunakan sintaks `async/await` untuk menulis kode asinkron yang terlihat seperti sinkron, membuatnya lebih mudah dibaca.
*   **Tugas:**
    1.  Gunakan kembali fungsi `ambilDataPengguna(userId)` dari Soal 13.
    2.  Buat sebuah fungsi *async* bernama `tampilkanInfoPengguna(userId)`.
    3.  Di dalam `tampilkanInfoPengguna`, gunakan `await` untuk memanggil `ambilDataPengguna(userId)`.
    4.  Gunakan blok `try...catch` untuk menangani potensi error (jika Promise di-reject).
    5.  Jika berhasil (di dalam `try`), cetak data pengguna yang diterima.
    6.  Jika gagal (di dalam `catch`), cetak pesan error yang diterima.
    7.  Panggil `tampilkanInfoPengguna` dengan ID yang valid (misal: 456) dan ID yang tidak valid (misal: 0).
*   **Tips:** Keyword `async` diletakkan sebelum definisi fungsi. Keyword `await` hanya bisa digunakan di dalam fungsi `async`. Blok `try...catch` adalah cara standar menangani error saat menggunakan `async/await`.

---

**Soal 15: Pengenalan Class dan OOP (Object-Oriented Programming)**

*   **Tujuan:** Memahami konsep dasar OOP seperti Class, constructor, properties (properti), dan methods (metode).
*   **Tugas:**
    1.  Buat sebuah `class` bernama `Mobil`.
    2.  Definisikan `constructor` untuk `Mobil` yang menerima `merk`, `warna`, dan `tahunProduksi`. Constructor ini harus menginisialisasi properti `this.merk`, `this.warna`, `this.tahunProduksi`, dan juga properti `this.kecepatan` dengan nilai awal 0.
    3.  Tambahkan sebuah *method* bernama `info()` yang mengembalikan string deskripsi mobil (misal: "Mobil [Merk] warna [Warna] tahun [Tahun Produksi]").
    4.  Tambahkan sebuah *method* bernama `akselerasi(tambahanKecepatan)` yang menambah `this.kecepatan` sebesar `tambahanKecepatan` dan mencetak kecepatan baru ke console (misal: "Kecepatan sekarang: [Kecepatan] km/jam").
    5.  Buat dua *instance* (objek) dari kelas `Mobil` dengan data berbeda.
    6.  Panggil method `info()` dan `akselerasi()` pada kedua instance tersebut.
*   **Tips:** Gunakan keyword `class` dan `constructor`. Method didefinisikan langsung di dalam body class. `this` merujuk pada instance objek yang sedang dibuat atau dimanipulasi.

---

**Soal 16: Inheritance (Pewarisan) dalam OOP**

*   **Tujuan:** Memahami bagaimana membuat subclass yang mewarisi properti dan method dari superclass (kelas induk) dan menambahkan fungsionalitas spesifik.
*   **Tugas:**
    1.  Gunakan `class Mobil` dari Soal 15 sebagai kelas induk.
    2.  Buat `class` baru bernama `Truk` yang *mewarisi* (extends) dari `Mobil`.
    3.  Definisikan `constructor` untuk `Truk` yang menerima `merk`, `warna`, `tahunProduksi`, dan `kapasitasMuatan`. Constructor ini harus memanggil `constructor` kelas induk (`Mobil`) menggunakan `super()` untuk menginisialisasi properti yang diwarisi, dan kemudian menginisialisasi properti spesifik `this.kapasitasMuatan`.
    4.  Tambahkan *method* baru pada `Truk` bernama `angkutBarang(beratBarang)` yang mencetak pesan tentang pengangkutan barang dan kapasitasnya (misal: "Mengangkut barang seberat [beratBarang] kg. Kapasitas maksimal: [kapasitasMuatan] kg.").
    5.  *Override* (timpa) method `info()` di kelas `Truk` untuk menyertakan informasi kapasitas muatan selain informasi dasar mobil. Gunakan `super.info()` di dalam method `info()` Truk untuk memanggil implementasi `info()` dari kelas induk.
    6.  Buat sebuah *instance* dari `Truk`.
    7.  Panggil method `info()`, `akselerasi()`, dan `angkutBarang()` pada instance Truk tersebut.
*   **Tips:** Gunakan keyword `extends` untuk pewarisan dan `super()` untuk memanggil constructor/method kelas induk.

---

**Soal 17: Struktur Data - Map untuk Frekuensi**

*   **Tujuan:** Menggunakan struktur data `Map` untuk kasus penggunaan umum seperti menghitung frekuensi kemunculan item.
*   **Tugas:** Buat sebuah fungsi `hitungFrekuensiKata(kalimat)` yang menerima sebuah string `kalimat`. Fungsi ini harus:
    1.  Mengubah kalimat menjadi huruf kecil semua (`toLowerCase()`).
    2.  Memecah kalimat menjadi array kata-kata (gunakan `split()` dengan spasi atau regex yang lebih canggih untuk menangani tanda baca jika diinginkan).
    3.  Menggunakan `Map` untuk menyimpan frekuensi setiap kata. Key adalah kata, value adalah jumlah kemunculannya.
    4.  Mengembalikan `Map` tersebut.
*   **Contoh Pemanggilan dan Output:**
    ```javascript
    let teks = "Saya suka makan nasi goreng dan nasi uduk suka sekali";
    let frekuensi = hitungFrekuensiKata(teks);
    console.log(frekuensi);
    // Output: Map(7) {
    //   'saya' => 1,
    //   'suka' => 2,
    //   'makan' => 1,
    //   'nasi' => 2,
    //   'goreng' => 1,
    //   'dan' => 1,
    //   'uduk' => 1,
    //   'sekali' => 1 // (Perhatikan: jika split hanya spasi, 'sekali' akan jadi kata sendiri)
    // }
    // (Output Map mungkin sedikit berbeda urutannya)
    ```
*   **Tips:** Iterasi array kata. Untuk setiap kata, periksa apakah sudah ada di `Map`. Jika ya, increment valuenya (`map.set(kata, map.get(kata) + 1)`). Jika tidak, tambahkan ke `Map` dengan value 1 (`map.set(kata, 1)`).

---

**Soal 18: Algoritma Dasar - Pencarian Biner (Binary Search)**

*   **Tujuan:** Mengimplementasikan algoritma pencarian yang efisien pada data yang terurut.
*   **Tugas:** Buat sebuah fungsi `cariAngkaBiner(dataTerurut, target)`:
    1.  Fungsi menerima sebuah `array` angka yang **sudah terurut** naik (`dataTerurut`) dan sebuah angka `target` yang ingin dicari.
    2.  Implementasikan algoritma *binary search* untuk menemukan indeks dari `target` di dalam `dataTerurut`.
    3.  Jika `target` ditemukan, kembalikan indeksnya.
    4.  Jika `target` tidak ditemukan setelah pencarian selesai, kembalikan `-1`.
    5.  **Penting:** Jangan menggunakan method `indexOf()` atau `find()` bawaan Array. Implementasikan logikanya secara manual (menggunakan pointer `kiri`, `kanan`, dan `tengah`).
*   **Contoh Pemanggilan:**
    ```javascript
    let angkaUrut = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91];
    console.log(cariAngkaBiner(angkaUrut, 23));  // Output: 5
    console.log(cariAngkaBiner(angkaUrut, 91));  // Output: 9
    console.log(cariAngkaBiner(angkaUrut, 1));   // Output: -1
    console.log(cariAngkaBiner(angkaUrut, 50));  // Output: -1
    ```
*   **Tips:** Inisialisasi `kiri = 0`, `kanan = dataTerurut.length - 1`. Selama `kiri <= kanan`, hitung `tengah`, bandingkan `dataTerurut[tengah]` dengan `target`, dan perbarui `kiri` atau `kanan` sesuai hasil perbandingan.

---

**Soal 19: Penanganan Error Tingkat Lanjut (Custom Error)**

*   **Tujuan:** Memahami cara membuat dan melemparkan error kustom untuk penanganan kesalahan yang lebih spesifik dan informatif.
*   **Tugas:**
    1.  Buat sebuah *custom error class* bernama `ValidationError` yang mewarisi dari `Error` bawaan JavaScript. Constructor-nya harus menerima pesan error.
    2.  Buat fungsi `validasiInputPengguna(dataPengguna)` yang menerima objek `dataPengguna` (misal: `{ nama: "...", email: "...", usia: ... }`).
    3.  Fungsi ini harus melakukan validasi:
        *   Jika `nama` kosong atau bukan string, lempar (`throw`) `new ValidationError("Nama tidak boleh kosong.")`.
        *   Jika `email` tidak valid (misal, tidak mengandung '@'), lempar `new ValidationError("Format email tidak valid.")`. (Gunakan regex sederhana untuk cek '@').
        *   Jika `usia` bukan angka atau kurang dari 18, lempar `new ValidationError("Usia harus minimal 18 tahun.")`.
    4.  Jika semua validasi lolos, fungsi bisa mengembalikan `true` atau pesan sukses.
    5.  Di luar fungsi, panggil `validasiInputPengguna` dalam blok `try...catch`. Tangkap error spesifik `ValidationError` dan cetak pesannya. Tangkap juga error umum lainnya jika ada.
*   **Tips:** Struktur `class ValidationError extends Error { constructor(message) { super(message); this.name = "ValidationError"; } }`. Di blok `catch`, gunakan `instanceof` untuk memeriksa tipe error (`catch (error) { if (error instanceof ValidationError) { ... } else { ... } }`).

---

**Soal 20: Modul JavaScript (ES Modules)**

*   **Tujuan:** Memahami cara mengorganisir kode ke dalam file-file terpisah (modul) menggunakan sintaks `import` dan `export` standar ES6.
*   **Tugas:**
    1.  Buat file `utils.js`. Di dalamnya, definisikan dan *export* dua fungsi:
        *   `kapitalkanAwalKata(str)`: Mengambil string dan mengembalikan string baru dengan setiap awal kata dikapitalkan (mirip contoh Anda sebelumnya).
        *   `konstantaPajak = 0.11`: Ekspor sebuah konstanta.
    2.  Buat file `main.js`.
    3.  Di `main.js`, *import* fungsi `kapitalkanAwalKata` dan konstanta `konstantaPajak` dari `utils.js`.
    4.  Gunakan fungsi yang diimpor untuk mengubah string "selamat pagi indonesia" menjadi "Selamat Pagi Indonesia" dan cetak hasilnya.
    5.  Cetak nilai `konstantaPajak` yang diimpor.
    6.  **Cara Menjalankan:** Untuk menjalankan kode yang menggunakan ES Modules di Node.js, Anda mungkin perlu:
        *   Menambahkan `"type": "module"` di file `package.json` Anda.
        *   Atau menyimpan file dengan ekstensi `.mjs` (`utils.mjs`, `main.mjs`) dan menjalankannya dengan `node main.mjs`.
        *   Atau menggunakan *bundler* seperti Webpack/Parcel jika ini untuk lingkungan browser.
*   **Tips:** Gunakan `export function namaFungsi() {...}` atau `export const namaKonstanta = ...` di `utils.js`. Gunakan `import { kapitalkanAwalKata, konstantaPajak } from './utils.js';` di `main.js`.

---

**Praktik Terbaik Tambahan untuk Tingkat Mahir:**

1.  **Kode Bersih (Clean Code):** Fokus pada keterbacaan, fungsi/kelas yang kecil dan fokus, hindari duplikasi kode (DRY - Don't Repeat Yourself).
2.  **Immutability:** Sebisa mungkin, hindari memodifikasi data (objek/array) secara langsung. Buat salinan dan modifikasi salinan tersebut, terutama saat bekerja dengan state dalam framework/library.
3.  **Pure Functions:** Jika memungkinkan, buat fungsi yang output-nya hanya bergantung pada input-nya dan tidak memiliki *side effects* (tidak mengubah state di luar fungsi, tidak melakukan I/O).
4.  **Asynchronous Patterns:** Pahami kapan menggunakan `Promise.all`, `Promise.race`, dll.
5.  **Testing:** Mulai pikirkan bagaimana kode Anda bisa diuji (Unit Testing). Fungsi yang murni (pure) lebih mudah diuji.
6.  **Manajemen Ketergantungan (Dependency Management):** Pahami penggunaan `npm` atau `yarn` untuk mengelola library eksternal.
7.  **Version Control (Git):** Ini adalah *skill* wajib bagi developer.

---

