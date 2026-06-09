a.	Judul Program: Implementasi Hash Map Open Addressing pada Sistem Antrian Kasir Minimarket Menggunakan Metode Linear Probing


b.	Deskripsi Singkat: 
Program ini dibuat untuk mensimulasikan sistem antrian kasir minimarket menggunakan struktur data Hash Map Open Addressing. Program digunakan untuk mengelola data pelanggan berdasarkan nomor pelanggan dan nama pelanggan yang kemudian disimpan ke dalam hash table. Beberapa fitur yang terdapat pada program ini meliputi proses penambahan data pelanggan, pencarian data pelanggan, penghapusan data pelanggan, serta menampilkan posisi pelanggan pada setiap slot kasir. Dengan adanya program ini, proses pengelolaan data pelanggan dapat dilakukan secara lebih terstruktur dan efisien.
Algoritma yang diterapkan pada program ini adalah Hash Map Open Addressing dengan metode Linear Probing. Metode ini digunakan untuk menangani collision, yaitu kondisi ketika beberapa data memiliki hasil hash yang sama dan menempati indeks yang sama. Saat collision terjadi, sistem akan mencari slot kosong berikutnya secara berurutan hingga menemukan posisi yang tersedia. Selain itu, program juga menerapkan status DELETED pada proses penghapusan data agar pencarian data lain yang mengalami collision tetap dapat dilakukan dengan baik. Dengan penerapan metode ini, proses penyimpanan, pencarian, dan penghapusan data dapat berjalan lebih optimal.


c.	Source Code:


<img width="665" height="875" alt="Screenshot 2026-06-08 223539" src="https://github.com/user-attachments/assets/8f171dcc-d67b-4e1e-9d3e-1f8af028713b" />


<img width="674" height="831" alt="Screenshot 2026-06-08 223600" src="https://github.com/user-attachments/assets/a716aef6-8c1c-4a1c-8f6f-1d120afb09b9" />


 <img width="807" height="830" alt="Screenshot 2026-06-08 223748" src="https://github.com/user-attachments/assets/0ac0015f-d475-4c38-9faa-5a42b441b416" />


 <img width="624" height="803" alt="Screenshot 2026-06-08 223808" src="https://github.com/user-attachments/assets/b2fe0527-3e77-4563-8f99-fbaad60be190" />


 <img width="661" height="253" alt="Screenshot 2026-06-08 223841" src="https://github.com/user-attachments/assets/8ea1d0ea-5c53-4023-977b-88b528cc9e78" />

 
Penjelasan logika berjalannya kode program:
1.	Pada bagian ini dibuat class SlotState untuk menyimpan status slot pada hash table.
2. Status EMPTY digunakan untuk menandai slot yang masih kosong.
3. Status OCCUPIED digunakan untuk menandai slot yang sudah terisi data.
4. Status DELETED digunakan untuk menandai data yang sudah dihapus.
5.
6.
7. Pada bagian ini dibuat class Entry untuk menyimpan data pada setiap slot hash table.
8. Method constructor dibuat untuk menginisialisasi data awal pada class Entry.
9. Variabel key diatur bernilai None sebagai nilai awal.
10. Variabel value diatur bernilai None sebagai nilai awal.
11. Status awal slot diatur menjadi EMPTY atau kosong.
12.
13.
14. Constructor dibuat pada class HashMapOpenAddressing.
15. Parameter size digunakan untuk menentukan ukuran hash table.
16. Nilai ukuran tabel disimpan ke variabel SIZE.
17. Membuat tabel hash berisi slot kosong sebanyak ukuran yang ditentukan.
18.
19. Method hash_function() dibuat untuk menentukan indeks penyimpanan data.
20. Operasi modulo digunakan untuk menghasilkan indeks hash.
21.
22. Method insert() dibuat untuk memasukkan pelanggan ke hash table.
23. Menghitung indeks awal berdasarkan hash function.
24. Variabel first_deleted digunakan untuk menyimpan posisi deleted pertama.
25.
26. Dilakukan perulangan untuk mencari slot kosong atau slot tersedia.
27.
28. Posisi slot dihitung menggunakan linear probing.
29.
30. Mengecek apakah slot sedang terisi data.
31.
32. Mengecek apakah nomor pelanggan sudah ada sebelumnya.
33. Jika key ditemukan, value diperbarui dengan data baru.
34. Mengembalikan nilai True jika update berhasil.
35.
36. Mengecek apakah slot berstatus deleted.
37.
38. Memastikan belum ada slot deleted yang tersimpan sebelumnya.
39. Menyimpan posisi deleted pertama yang ditemukan.
40.
41. Kondisi ini dijalankan ketika slot kosong ditemukan.
42.
43. Mengecek apakah sebelumnya ditemukan slot deleted.
44. Jika ada slot deleted, posisi insert dipindahkan ke slot tersebut.
45.
46. Menyimpan nomor pelanggan ke key slot.
47. Menyimpan nama pelanggan ke value slot.
48. Mengubah status slot menjadi OCCUPIED.
49.
50. Mengembalikan True jika data berhasil dimasukkan.
51.
52. Mengembalikan False jika tabel penuh atau insert gagal.
53.
54. Method search() dibuat untuk mencari pelanggan berdasarkan nomor pelanggan.
55.
56. Menghitung indeks awal menggunakan hash function.
57.
58. Melakukan perulangan untuk proses pencarian.
59.
60. Menghitung posisi menggunakan linear probing.
61.
62. Mengecek apakah slot kosong ditemukan.
63. Jika slot kosong, data dianggap tidak ada.
64.
65. Mengecek apakah slot berisi data dan key sesuai.
66. Membandingkan key tabel dengan nomor pelanggan yang dicari.
67.
68. Mengembalikan data pelanggan jika ditemukan.
69.
70. Mengembalikan None jika data tidak ditemukan.
71.
72. Method remove_key() dibuat untuk menghapus pelanggan.
73.
74. Mencari data pelanggan sebelum proses penghapusan.
75.
76. Mengecek apakah data ditemukan.
77. Mengembalikan False jika data tidak ada.
78.
79. Mengubah status slot menjadi deleted.
80.
81. Mengembalikan True jika penghapusan berhasil.
82.
83. Method display() dibuat untuk menampilkan isi hash table.
84.
85. Menampilkan judul output hash table.
86.
87. Melakukan perulangan untuk menampilkan semua slot.
88.
89. Menampilkan nomor indeks atau nomor kasir.
90.
91. Mengecek apakah slot kosong.
92.
93. Menampilkan tulisan “Kosong”.
94.
95. Mengecek apakah slot deleted.
96.
97. Menampilkan tulisan “Antrian Dihapus”.
98.
99. Kondisi jika slot berisi data pelanggan.
100.
101. Menampilkan output data pelanggan.
102. Menampilkan nomor pelanggan beserta nama pelanggan.
103. Menutup perintah output.
104.
105.
106. Membuat fungsi utama program.
107.
108. Membuat objek hash map bernama kasir.
109.
110. Menambahkan pelanggan nomor 15 dengan nama Budi.
111. Menambahkan pelanggan nomor 25 dengan nama Citra.
112. Menambahkan pelanggan nomor 8 dengan nama Dina.
113. Menambahkan pelanggan nomor 5 dengan nama Andi.
114.
115. Menampilkan teks “Data awal”.
116. Menampilkan isi hash table awal.
117.
118. Melakukan pencarian pelanggan nomor 15.
119.
120. Mengecek apakah pelanggan ditemukan.
121.
122. Menampilkan informasi pelanggan ditemukan.
123. Menampilkan nomor pelanggan yang ditemukan.
124. Menampilkan nama pelanggan yang ditemukan.
125. Menutup output print.
126.
127. Menampilkan pesan jika pelanggan tidak ditemukan.
128.
129. Menghapus pelanggan nomor 15.
130.
131. Menampilkan informasi setelah penghapusan data.
132.
133. Menampilkan isi hash table terbaru.
134.
135. Melakukan pencarian pelanggan nomor 25.
136.
137. Mengecek apakah pelanggan masih ada setelah penghapusan data lain.
138.
139. Menampilkan informasi bahwa pelanggan masih ditemukan.
140.
141. Menampilkan nomor pelanggan.
142. Menampilkan nama pelanggan.
143. Menutup output print.
144. Kondisi jika pelanggan tidak ditemukan.
145.
146. Menampilkan pesan pelanggan tidak ditemukan.
147.
148. Penutup blok kondisi terakhir.
149.
150.
151. Mengecek apakah file dijalankan langsung sebagai program utama.
152. Menjalankan fungsi main().


d.	Output Program:
 

<img width="488" height="651" alt="Screenshot 2026-06-08 223922" src="https://github.com/user-attachments/assets/5d321564-0cee-4553-9741-4f19440b49d5" />


Penjelasan Output :
Output program menunjukkan bagaimana Hash Map Open Addressing dengan metode Linear Probing bekerja dalam mengatur antrian kasir minimarket. Pada awalnya, pelanggan nomor 5 langsung masuk ke Kasir 5, sedangkan pelanggan nomor 15 dan 25 mengalami collision karena memiliki hasil hash yang sama. Untuk mengatasinya, sistem mencari slot kosong berikutnya secara berurutan sehingga pelanggan nomor 15 ditempatkan di Kasir 6 dan pelanggan nomor 25 di Kasir 7. Pelanggan nomor 8 langsung masuk ke Kasir 8 karena slot masih tersedia.
Selanjutnya, program melakukan pencarian pelanggan nomor 15 dan berhasil menemukan data pelanggan dengan nama Budi. Setelah itu, pelanggan nomor 15 dihapus sehingga slotnya berubah menjadi Antrian Dihapus atau DELETED, bukan langsung kosong, agar pencarian data lain tetap berjalan dengan baik. Hal ini terlihat ketika pelanggan nomor 25 masih berhasil ditemukan meskipun sebelumnya terjadi collision dan salah satu data sudah dihapus. Dari hasil tersebut dapat dilihat bahwa metode Linear Probing mampu menangani collision, pencarian, dan penghapusan data dengan baik.


e.	Link YouTube: 
