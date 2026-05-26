a.	Judul Program: Pendataan Tinggi Badan Mahasiswa Menggunakan Binary Search Tree Dasar

b.	Deskripsi Singkat: 
Program ini dibuat untuk mengelola data tinggi badan mahasiswa menggunakan struktur data Binary Search Tree atau BST. Program dapat digunakan untuk menambahkan data tinggi badan mahasiswa, mencari data tertentu, menampilkan data menggunakan traversal inorder, preorder, dan postorder, mencari nilai minimum dan maksimum, menghitung jumlah mahasiswa, serta menghitung total seluruh tinggi badan mahasiswa yang tersimpan pada tree. Dengan adanya program ini, proses pengelolaan data tinggi badan mahasiswa menjadi lebih terstruktur dan mudah dilakukan.

Algoritma yang diterapkan pada program ini adalah Binary Search Tree (BST), yaitu struktur data berbentuk pohon biner yang memiliki aturan bahwa nilai yang lebih kecil ditempatkan di subtree kiri dan nilai yang lebih besar ditempatkan di subtree kanan. Struktur data BST digunakan karena mampu mempercepat proses pencarian dan pengolahan data dibandingkan pencarian biasa. Selain itu, BST juga mempermudah proses pengurutan data secara otomatis sehingga data tinggi badan mahasiswa dapat ditampilkan secara terurut.

c.	Source Code:


<img width="484" height="911" alt="Screenshot 2026-05-26 063257" src="https://github.com/user-attachments/assets/b3f25f66-f035-4192-beeb-e393caafe9b7" />


<img width="607" height="873" alt="Screenshot 2026-05-26 063330" src="https://github.com/user-attachments/assets/40a3092b-f884-411d-ab80-fce75de5a441" />


<img width="571" height="892" alt="Screenshot 2026-05-26 063356" src="https://github.com/user-attachments/assets/dabb4fcc-62f3-4286-8b63-fab22c1a719b" />


<img width="526" height="284" alt="Screenshot 2026-05-26 063428" src="https://github.com/user-attachments/assets/a722437a-f3b9-4cf4-9c32-a342e49b8796" />

 
Penjelasan logika berjalannya kode program:
1.	Mendefinisikan class Node sebagai struktur dasar untuk menyimpan data tinggi badan mahasiswa pada Binary Search Tree. 
2.	Mendefinisikan constructor untuk menginisialisasi isi node saat objek dibuat. 
3.	Menyimpan nilai tinggi badan mahasiswa ke dalam atribut tinggi sebagai data utama node. 
4.	Menginisialisasi child kiri dengan nilai kosong (None) yang nantinya digunakan untuk menyimpan data lebih kecil dari root. 
5.	Menginisialisasi child kanan dengan nilai kosong (None) yang nantinya digunakan untuk menyimpan data lebih besar dari root. 
6.	
7.	
8.	Mendefinisikan class BSTTinggiMahasiswa sebagai class utama untuk mengatur seluruh proses Binary Search Tree. 
9.	Mendefinisikan constructor untuk class BST. 
10.	Menginisialisasi root BST dengan nilai kosong (None) karena tree belum memiliki data. 
11.	
12.	Mendefinisikan fungsi insert_node untuk menambahkan node baru ke dalam BST sesuai aturan Binary Search Tree. 
13.	Mengecek apakah posisi root masih kosong atau belum memiliki node. 
14.	Membuat node baru berisi data tinggi badan jika posisi root kosong. 
15.	
16.	Mengecek apakah nilai tinggi badan lebih kecil dibandingkan root saat ini. 
17.	Memasukkan data ke subtree kiri secara rekursif karena nilainya lebih kecil dari root. 
18.	
19.	Mengecek apakah nilai tinggi badan lebih besar dibandingkan root saat ini. 
20.	Memasukkan data ke subtree kanan secara rekursif karena nilainya lebih besar dari root. 
21.	
22.	Mengembalikan root setelah proses penambahan node selesai dilakukan. 
23.	
24.	Mendefinisikan fungsi insert sebagai fungsi utama untuk proses penambahan data tinggi badan. 
25.	Memanggil fungsi insert_node untuk memasukkan data ke dalam BST mulai dari root. 
26.	
27.	Mendefinisikan fungsi search_node untuk mencari data tinggi badan tertentu pada BST. 
28.	Mengecek apakah node yang sedang diperiksa kosong. 
29.	Mengembalikan nilai False sebagai tanda bahwa data tidak ditemukan di BST. 
30.	
31.	Mengecek apakah data pada root sama dengan data yang sedang dicari. 
32.	Mengembalikan nilai True sebagai tanda bahwa data berhasil ditemukan. 
33.	
34.	Mengecek apakah data yang dicari lebih kecil dari nilai root saat ini. 
35.	Melanjutkan pencarian ke subtree kiri secara rekursif karena nilainya lebih kecil. 
36.	
37.	Melanjutkan pencarian ke subtree kanan secara rekursif karena nilainya lebih besar. 
38.	
39.	Mendefinisikan fungsi search sebagai fungsi pencarian utama yang dipanggil pada menu program. 
40.	Memanggil fungsi search_node dari root BST untuk memulai proses pencarian data. 
41.	
42.	Mendefinisikan fungsi traversal inorder untuk menampilkan data secara terurut dari kecil ke besar. 
43.	Mengecek apakah node yang sedang diperiksa kosong. 
44.	Menghentikan traversal apabila node kosong agar tidak terjadi error. 
45.	
46.	Menjalankan traversal pada subtree kiri terlebih dahulu untuk mengambil nilai terkecil lebih dulu. 
47.	Menampilkan data tinggi badan yang berada pada root saat traversal berlangsung. 
48.	Menjalankan traversal pada subtree kanan setelah subtree kiri selesai diproses. 
49.	
50.	Mendefinisikan fungsi traversal preorder untuk menampilkan root terlebih dahulu sebelum subtree lain. 
51.	Mengecek apakah node yang sedang diperiksa kosong. 
52.	Menghentikan traversal apabila node kosong. 
53.	
54.	Menampilkan data root terlebih dahulu pada traversal preorder. 
55.	Menjalankan traversal pada subtree kiri setelah root ditampilkan. 
56.	Menjalankan traversal pada subtree kanan setelah subtree kiri selesai. 
57.	
58.	Mendefinisikan fungsi traversal postorder untuk menampilkan root paling akhir. 
59.	Mengecek apakah node yang sedang diperiksa kosong. 
60.	Menghentikan traversal apabila node kosong. 
61.	
62.	Menjalankan traversal pada subtree kiri terlebih dahulu. 
63.	Menjalankan traversal pada subtree kanan setelah subtree kiri selesai diproses. 
64.	Menampilkan data root paling akhir setelah subtree kiri dan kanan selesai. 
65.	
66.	Mendefinisikan fungsi find_min untuk mencari nilai tinggi badan paling kecil pada BST. 
67.	Mengecek apakah BST kosong atau belum memiliki data. 
68.	Mengembalikan nilai -1 apabila BST kosong. 
69.	
70.	Menyimpan posisi root ke variabel current untuk proses pencarian minimum. 
71.	
72.	Melakukan perulangan selama node masih memiliki child kiri. 
73.	Menggeser posisi current terus ke kiri karena nilai minimum berada di sisi paling kiri BST. 
74.	
75.	Mengembalikan nilai tinggi badan terkecil yang ditemukan pada BST. 
76.	
77.	Mendefinisikan fungsi find_max untuk mencari nilai tinggi badan paling besar pada BST. 
78.	Mengecek apakah BST kosong atau belum memiliki data. 
79.	Mengembalikan nilai -1 apabila BST kosong. 
80.	
81.	Menyimpan posisi root ke variabel current untuk proses pencarian maksimum. 
82.	
83.	Melakukan perulangan selama node masih memiliki child kanan. 
84.	Menggeser posisi current terus ke kanan karena nilai maksimum berada di sisi paling kanan BST. 
85.	
86.	Mengembalikan nilai tinggi badan terbesar yang ditemukan pada BST. 
87.	
88.	Mendefinisikan fungsi count_nodes untuk menghitung jumlah seluruh node pada BST. 
89.	Mengecek apakah node yang sedang diperiksa kosong. 
90.	Mengembalikan nilai 0 apabila node kosong. 
91.	
92.	Menghitung total seluruh node pada subtree kiri dan subtree kanan kemudian ditambah root. 
93.	
94.	Mendefinisikan fungsi sum_nodes untuk menghitung total seluruh tinggi badan mahasiswa. 
95.	Mengecek apakah node yang sedang diperiksa kosong. 
96.	Mengembalikan nilai 0 apabila node kosong. 
97.	
98.	Menjumlahkan seluruh nilai node pada subtree kiri, subtree kanan, dan root BST. 
99.	
100.	
101.	Mendefinisikan fungsi main sebagai pusat jalannya program BST. 
102.	Membuat objek BST bernama bst dari class BSTTinggiMahasiswa. 
103.	Menginisialisasi variabel pilih dengan nilai awal 0 untuk menyimpan pilihan menu. 
104.	
105.	Menjalankan perulangan menu selama pengguna belum memilih menu keluar. 
106.	Menampilkan judul program BST Tinggi Badan Mahasiswa. 
107.	Menampilkan menu untuk menambah data tinggi badan mahasiswa. 
108.	Menampilkan menu untuk mencari data tinggi badan mahasiswa. 
109.	Menampilkan menu traversal inorder. 
110.	Menampilkan menu traversal preorder. 
111.	Menampilkan menu traversal postorder. 
112.	Menampilkan menu untuk mencari tinggi badan minimum. 
113.	Menampilkan menu untuk mencari tinggi badan maksimum. 
114.	Menampilkan menu untuk menghitung jumlah mahasiswa yang tersimpan pada BST. 
115.	Menampilkan menu untuk menghitung total seluruh tinggi badan mahasiswa. 
116.	Menampilkan menu keluar program. 
117.	
118.	Membuat blok try untuk menangani kemungkinan kesalahan input pengguna. 
119.	Meminta pengguna memasukkan pilihan menu program. 
120.	Menangani error apabila input yang dimasukkan bukan angka. 
121.	Menampilkan pesan bahwa input yang diberikan tidak valid. 
122.	Mengulang kembali ke menu utama apabila terjadi error input. 
123.	
124.	Mengecek apakah pengguna memilih menu tambah data tinggi badan. 
125.	Membuat blok try untuk menangani kesalahan input data tinggi badan. 
126.	Meminta pengguna memasukkan data tinggi badan mahasiswa dalam satuan cm. 
127.	Memasukkan data tinggi badan ke dalam BST menggunakan fungsi insert. 
128.	Menampilkan pesan bahwa data tinggi badan berhasil ditambahkan ke BST. 
129.	Menangani error apabila input bukan angka. 
130.	Menampilkan pesan bahwa input tidak valid. 
131.	
132.	Mengecek apakah pengguna memilih menu pencarian data tinggi badan. 
133.	Membuat blok try untuk menangani kesalahan input pencarian data. 
134.	Meminta pengguna memasukkan data tinggi badan yang ingin dicari. 
135.	
136.	Mengecek apakah data tinggi badan terdapat di dalam BST menggunakan fungsi search. 
137.	Menampilkan pesan bahwa data tinggi badan ditemukan pada BST. 
138.	Menjalankan kondisi apabila data tidak ditemukan pada BST. 
139.	Menampilkan pesan bahwa data tinggi badan tidak ditemukan. 
140.	
141.	Menangani error apabila input pencarian bukan angka. 
142.	Menampilkan pesan bahwa input tidak valid. 
143.	
144.	Mengecek apakah pengguna memilih menu traversal inorder. 
145.	Menampilkan teks “Inorder” sebelum traversal dijalankan. 
146.	Menjalankan traversal inorder mulai dari root BST. 
147.	Membuat pindah baris setelah traversal selesai ditampilkan. 
148.	
149.	Mengecek apakah pengguna memilih menu traversal preorder. 
150.	Menampilkan teks “Preorder” sebelum traversal dijalankan. 
151.	Menjalankan traversal preorder mulai dari root BST. 
152.	Membuat pindah baris setelah traversal selesai ditampilkan. 
153.	
154.	Mengecek apakah pengguna memilih menu traversal postorder. 
155.	Menampilkan teks “Postorder” sebelum traversal dijalankan. 
156.	Menjalankan traversal postorder mulai dari root BST. 
157.	Membuat pindah baris setelah traversal selesai ditampilkan. 
158.	
159.	Mengecek apakah pengguna memilih menu mencari tinggi minimum. 
160.	Menampilkan nilai tinggi badan paling kecil yang terdapat pada BST. 
161.	
162.	Mengecek apakah pengguna memilih menu mencari tinggi maksimum. 
163.	Menampilkan nilai tinggi badan paling besar yang terdapat pada BST. 
164.	
165.	Mengecek apakah pengguna memilih menu menghitung jumlah mahasiswa. 
166.	Menampilkan jumlah seluruh node atau jumlah mahasiswa yang tersimpan pada BST. 
167.	
168.	Mengecek apakah pengguna memilih menu menghitung total tinggi badan. 
169.	Menampilkan hasil penjumlahan seluruh data tinggi badan mahasiswa pada BST. 
170.	
171.	Mengecek apakah pengguna memilih menu keluar program. 
172.	Menampilkan pesan bahwa program telah selesai dijalankan. 
173.	
174.	Menjalankan kondisi apabila pengguna memasukkan pilihan menu yang tidak tersedia. 
175.	Menampilkan pesan bahwa pilihan menu tidak valid. 
176.	
177.	
178.	Mengecek apakah file dijalankan langsung sebagai program utama Python. 
179.	Menjalankan fungsi main() untuk memulai keseluruhan program BST Tinggi Badan Mahasiswa. 

d.	Output Program:


<img width="328" height="902" alt="Screenshot 2026-05-26 065556" src="https://github.com/user-attachments/assets/1b68d8ab-2648-4d57-8948-905187ab35ba" />


<img width="256" height="837" alt="Screenshot 2026-05-26 065616" src="https://github.com/user-attachments/assets/e51223d2-f086-4d3d-b7b0-9b05d86cd58f" />


<img width="282" height="850" alt="Screenshot 2026-05-26 065632" src="https://github.com/user-attachments/assets/a48d3645-2f8f-4c83-8e5b-84984825a2c0" />


Penjelasan Output :
Saat program dijalankan, program akan menampilkan menu utama BST Tinggi Badan Mahasiswa yang berisi beberapa pilihan menu seperti tambah data, cari data, traversal, mencari nilai minimum dan maksimum, menghitung jumlah mahasiswa, menghitung total tinggi badan, dan keluar program.

Pada menu Tambah Tinggi Badan, pengguna memasukkan data tinggi badan 177 cm, 173 cm, dan 180 cm. Program kemudian menampilkan pesan bahwa data berhasil ditambahkan ke dalam BST. Hal ini menunjukkan proses insert berjalan dengan baik.

Pada menu Cari Tinggi Badan, pengguna mencari data 177 dan program menampilkan pesan “Data tinggi badan ditemukan”. Output tersebut menunjukkan bahwa proses pencarian data pada BST berhasil dilakukan.

Pada menu Inorder, program menampilkan output 173 177 180. Hasil ini menunjukkan traversal inorder berhasil menampilkan data secara urut dari kecil ke besar.

Pada menu Preorder, program menampilkan output 177 173 180. Output tersebut menunjukkan bahwa root ditampilkan terlebih dahulu sebelum subtree kiri dan kanan.

Pada menu Postorder, program menampilkan output 173 180 177. Hasil ini menunjukkan bahwa traversal postorder menampilkan root paling akhir.

Pada menu Tinggi Minimum, program menampilkan output 173 cm yang menunjukkan nilai terkecil pada BST.
Pada menu Tinggi Maksimum, program menampilkan output 180 cm yang menunjukkan nilai terbesar pada BST.

Pada menu Jumlah Mahasiswa, program menampilkan output 3 yang berarti terdapat tiga data mahasiswa yang tersimpan pada BST.

Pada menu Total Tinggi, program menampilkan output 530 cm yang merupakan hasil penjumlahan seluruh data tinggi badan mahasiswa.

Pada menu Keluar, program menampilkan pesan “Program selesai.” yang menunjukkan bahwa program berhasil dihentikan tanpa error.


e.	Link YouTube: 
