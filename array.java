public class array {
    public static void main(String[] args) {
        String[] lantaiz = {
            "Lantai 1",
            "Lantai 2"
        };
        String[][] ruanganz = {
            {"1","2","3","4","5"}
        };
        String[][][] barangz = {
            { // dimensi 1
                {"Hihi", "hoho", "wgwg", "wqwq", "b1", "sksks"}, // dimensi 2
                {"wqwq", "b1", "sksks"} // didalem yang 3 biji adalah dimensi 3
            },
            { // dimensi 1
                {"hoii","yeye","anjai"}, // dimensi 2
                {"popo","pip","assembly"} // didalem yang 3 biji adalah dimensi 3
            }
        };
        System.out.println(anjai[0][0][1]);
                    // dimensi   1  2  3


        // for (int lantai = 0; lantai < daftarBarang.length; lantai++) {
        //     for (int ruangan = 0; ruangan < daftarBarang[i].length; ruangan++) {
        //         for (int barang = 0; barang < daftarBarang[i][j].length; barang++) {
        //             System.out.println(daftarBarang[lantai][ruangan][barang]);
        //         }
        //     }
        // }
                    
    }
}
