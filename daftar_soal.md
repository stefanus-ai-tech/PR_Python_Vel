


/*
coba buat di javascript pake loop dan hasilnya begini


000000
900000
990000
999000
999900
999990
999999

*/


let jumlah = 7
let output

for (let i = 0; i < jumlah; i++) {
    output = '9'.repeat(i) + '0'.repeat(jumlah-i-1);
    console.log(output);
}

/*

coba buat di javascript pake loop dan hasilnya begini

Bilangan 0 adalah bilangan genap
Bilangan 1 adalah bilangan ganjil
Bilangan 2 adalah bilangan genap
Bilangan 3 adalah bilangan ganjil
Bilangan 4 adalah bilangan genap
Bilangan 5 adalah bilangan ganjil
Bilangan 6 adalah bilangan genap
Bilangan 7 adalah bilangan ganjil
Bilangan 8 adalah bilangan genap
Bilangan 9 adalah bilangan ganjil
*/

for (let i = 0; i < 10; i++) {
    if (i % 2 == 0) {
        console.log('Bilangan ' + i + ' adalah bilangan genap')
    }
    else {
        console.log('Bilangan ' + i + ' adalah bilangan ganjil')
    }
}

/*

coba buat di javascript hasil dengan output begini

Bilangan 0 adalah bilangan genap 
Bilangan 1 adalah bilangan ganjil
Karena ganjil, program berhenti
selesai

*/

let stop = false
let i = 0

while (!stop) {
    if (i % 2 == 0) {
        console.log('Bilangan ' + i + ' adalah bilangan genap')
    }
    else {
        console.log('Bilangan ' + i + ' adalah bilangan ganjil')
        console.log('Karena tedeteksi ganjil, program berhenti')
        stop = true
    }
    i += 1
}
console.log('selesai')


/*

Buat di javascript pake loop dan hasilnya

Januari
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
Februari
1
2
28
Maret
1
29
31 
April
1
2
3
30      
Mei
1
2
31
Juni
1
2
3
30
Juli
1
2
31
Agustus
1
2
3
31
September
1
2
3
30 
Oktober
1
2
3
31
November
1
2
3
30
Desember
1
2
3
31

*/


let month = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]


for (let i = 0; i < month.length; i++) {
    console.log(month[i])
    let maxDays = 31
    if (i === 1) {
        maxDays = 28
        }
    else if ([0, 2, 4, 6, 7, 9, 11].includes(i)) {
        maxDays = 31
    }
    else {
        maxDays = 30
    }
    for (let day = 0; day < maxDays ; day++) {
        console.log(day+1)
    }
}


// 3. Buat fungsi javascript yang akan menerima input berupa angka dan menghasilkan output berupa faktorial dari angka tersebut.

// Contoh:
// faktorial(5) // Output: 120
/*
Soal 3 (Faktorial):
Terapkan rekursi: Definisikan fungsi yang memanggil dirinya sendiri dengan nilai yang lebih kecil hingga mencapai kasus dasar (0! atau 1! adalah 1).
Atau gunakan loop: Iterasi dari 1 hingga n dan kalikan nilai-nilai tersebut untuk mendapatkan faktorial.
*/


function faktorial(n) {
    if (n === 0 || n === 1) return 1;
    return n * faktorial(n - 1);
  }
  
  console.log(faktorial(100));

// 4. Buat fungsi javascript yang menerima input berupa array angka dan mengembalikan array baru yang berisi angka-angka genap saja.

// Contoh:
// hanyaGenap([1, 2, 3, 4, 5]) // Output: [2, 4]
/*
Soal 4 (Hanya Genap):
Gunakan method .filter() pada array: Method ini membuat array baru dengan elemen yang lolos uji kondisi (bilangan genap dalam kasus ini).
Fungsi panah (arrow function): Gunakan sintaks ringkas untuk mendefinisikan fungsi di dalam .filter().
*/


function hanyaGenap(arr) {
    return arr.filter(num => num % 2 === 0);
  }
  
  console.log(hanyaGenap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]));

// 5. Buat fungsi javascript yang menerima input string dan mengembalikan string baru dengan huruf pertama setiap kata diubah menjadi huruf besar.
// Contoh:
// capitalizeWords("halo dunia") // Output: "Halo Dunia" 
/*
Soal 5 (Capitalize Words):
Gunakan method .split() untuk memisahkan string menjadi array kata berdasarkan spasi.
Gunakan method .map() untuk memproses setiap kata dan mengubah huruf pertama menjadi huruf besar.
Gunakan method .join() untuk menggabungkan kata-kata kembali menjadi string.
*/


function capitalizeWords(str) {
    return str.split(" ").map(word => word[0].toUpperCase() + word.slice(1)).join(" ");
  }
  
  console.log(capitalizeWords("hello world")); // "Hello World"
// 6. Buat program yang menerima input tahun dan menentukan apakah tahun tersebut merupakan tahun kabisat.
/*
Soal 6 (Tahun Kabisat):
Pahami aturan tahun kabisat: Tahun kabisat habis dibagi 4, kecuali tahun yang habis dibagi 100 tetapi tidak habis dibagi 400.
Gunakan operator logika untuk menggabungkan kondisi-kondisi tersebut.
*/


function isKabisat(year) {
    return (year % 4 === 0 && year % 100 !== 0) || year % 400 === 0;
  }
  
  console.log(isKabisat(2020)); // true
  console.log(isKabisat(2021)); // false

// 7. Buat fungsi yang menerima dua string sebagai argumen dan mengembalikan boolean true jika string pertama merupakan anagram dari string kedua, dan false jika bukan.

// Contoh:
// isAnagram("listen", "silent") // Output: true
/*
Soal 7 (Anagram):
Urutkan karakter kedua string: Ubah string menjadi array karakter, urutkan, lalu gabungkan kembali menjadi string.
Bandingkan string yang telah diurutkan: Jika kedua string yang diurutkan sama, mereka adalah anagram.
*/


function isAnagram(str1, str2) {
    const sorted1 = str1.split("").sort().join("");
    const sorted2 = str2.split("").sort().join("");
    return sorted1 === sorted2;
  }
  
  console.log("isAnagram('listen', 'silent')", isAnagram("listen", "silent")); // true
  console.log("isAnagram('hello', 'world')", isAnagram("hello", "world")); // false
// 8. Buat program yang menampilkan bilangan Fibonacci hingga batas tertentu yang ditentukan oleh pengguna.
/*
Soal 8 (Fibonacci):
Gunakan loop atau rekursi: Hitung bilangan Fibonacci berikutnya dengan menjumlahkan dua bilangan sebelumnya hingga mencapai batas yang ditentukan.
*/

function fibonacci(limit) {
    let a = 0, b = 1, c;
    console.log(a);
    console.log(b);
    while (b < limit) {
      c = a + b;
      console.log(c);
      a = b;
      b = c;
    }
  }
  
  console.log(fibonacci(1000));

// 9. Buat fungsi yang menerima array objek siswa (dengan atribut nama dan nilai) dan mengembalikan array objek siswa yang lulus saja (nilai >= 60).
/*
Soal 9 (Siswa Lulus):
Gunakan method .filter() pada array siswa: Periksa atribut nilai setiap siswa dan sertakan siswa dengan nilai >= 60 dalam array baru.
*/


function siswaLulus(siswa) {
    return siswa.filter(s => s.nilai >= 60);
  }

  function siswaLulus(siswa) {
    return siswa.filter(s => s.nilai >= 60);
  }
  
  console.log(siswaLulus([
    { nama: "Budi", nilai: 70 },
    { nama: "Joni", nilai: 50 },
    { nama: "Ani", nilai: 80 },
    { nama: "Siti", nilai: 40 },
    { nama: "Budi", nilai: 90 },
  ]));


