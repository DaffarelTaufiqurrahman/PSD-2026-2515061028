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
1. Mendefinisikan class SlotState untuk menyimpan status setiap slot pada hash table.
2. Mendefinisikan status EMPTY dengan nilai 0 sebagai penanda slot kosong.
3. Mendefinisikan status OCCUPIED dengan nilai 1 sebagai penanda slot yang berisi data pelanggan.
4. Mendefinisikan status DELETED dengan nilai 2 sebagai penanda slot yang datanya telah dihapus.
5.
6.
7. Mendefinisikan class Entry sebagai tempat penyimpanan data pelanggan pada setiap slot hash table.
8. Mendefinisikan constructor untuk menginisialisasi data awal pada objek Entry.
9. Menginisialisasi atribut key dengan nilai kosong (None).
10. Menginisialisasi atribut value dengan nilai kosong (None).
11. Menginisialisasi status awal slot sebagai EMPTY.
12.
13.
14. Mendefinisikan class HashMapOpenAddressing sebagai class utama pengelola hash table.
15. Mendefinisikan constructor untuk membuat hash table.
16. Menyimpan ukuran hash table ke dalam atribut SIZE.
17. Membuat sejumlah slot kosong sesuai ukuran hash table yang ditentukan.
18.
19. Mendefinisikan fungsi hash_function() untuk menentukan posisi penyimpanan data.
20. Menghasilkan indeks hash menggunakan operasi modulo terhadap ukuran tabel.
21.
22. Mendefinisikan fungsi insert() untuk menambahkan pelanggan ke hash table.
23. Menentukan indeks awal penyimpanan berdasarkan nomor pelanggan.
24. Menginisialisasi variabel untuk menyimpan posisi slot yang pernah dihapus.
25.
26. Melakukan perulangan untuk mencari slot yang dapat digunakan.
27.
28. Menghitung posisi slot menggunakan metode Linear Probing.
29.
30. Memeriksa apakah slot saat ini sudah terisi data pelanggan.
31.
32. Memeriksa apakah nomor pelanggan yang dimasukkan sudah ada di dalam hash table.
33. Memperbarui nama pelanggan jika nomor pelanggan sudah ditemukan.
34. Mengembalikan nilai True sebagai tanda proses berhasil.
35.
36. Memeriksa apakah slot saat ini berstatus DELETED.
37.
38. Memeriksa apakah belum ada slot deleted yang tersimpan sebelumnya.
39. Menyimpan posisi slot deleted pertama yang ditemukan.
40.
41. Menjalankan kondisi ketika slot kosong ditemukan.
42.
43. Memeriksa apakah terdapat slot deleted yang dapat digunakan kembali.
44. Menggunakan slot deleted sebagai lokasi penyimpanan data baru.
45.
46. Menyimpan nomor pelanggan ke dalam slot.
47. Menyimpan nama pelanggan ke dalam slot.
48. Mengubah status slot menjadi OCCUPIED.
49.
50. Mengembalikan nilai True sebagai tanda data berhasil ditambahkan.
51.
52. Mengembalikan nilai False jika proses insert gagal.
53.
54. Mendefinisikan fungsi search() untuk mencari data pelanggan.
55.
56. Menentukan indeks awal pencarian berdasarkan nomor pelanggan.
57.
58. Melakukan perulangan untuk proses pencarian data.
59.
60. Menghitung posisi pencarian menggunakan Linear Probing.
61.
62. Memeriksa apakah slot yang diperiksa masih kosong.
63. Mengembalikan nilai None jika data tidak ditemukan.
64.
65. Memeriksa apakah slot berisi data dan nomor pelanggan sesuai dengan data yang dicari.
66. Membandingkan nomor pelanggan yang dicari dengan data pada slot saat ini.
67.
68. Mengembalikan data pelanggan jika ditemukan.
69.
70. Mengembalikan nilai None apabila pencarian tidak menemukan data.
71.
72. Mendefinisikan fungsi remove_key() untuk menghapus data pelanggan.
73.
74. Melakukan pencarian data pelanggan yang akan dihapus.
75.
76. Memeriksa apakah data pelanggan ditemukan.
77. Mengembalikan nilai False jika data tidak ditemukan.
78.
79. Mengubah status slot menjadi DELETED.
80.
81. Mengembalikan nilai True sebagai tanda penghapusan berhasil.
82.
83. Mendefinisikan fungsi display() untuk menampilkan isi hash table.
84.
85. Menampilkan judul tampilan posisi antrian kasir minimarket.
86.
87. Melakukan perulangan untuk menampilkan seluruh slot hash table.
88.
89. Menampilkan nomor kasir atau indeks slot yang sedang diperiksa.
90.
91. Memeriksa apakah slot berstatus kosong.
92.
93. Menampilkan tulisan "Kosong" jika slot belum berisi pelanggan.
94.
95. Memeriksa apakah slot berstatus DELETED.
96.
97. Menampilkan tulisan "Antrian Dihapus" jika data pelanggan telah dihapus.
98.
99. Menjalankan kondisi jika slot berisi data pelanggan.
100.
101. Menampilkan informasi data pelanggan yang tersimpan pada slot.
102. Menampilkan nomor pelanggan dan nama pelanggan.
103. Menutup perintah output data pelanggan.
104.
105.
106. Mendefinisikan fungsi utama program.
107.
108. Membuat objek hash map bernama kasir.
109.
110. Menambahkan pelanggan nomor 5 dengan nama Andi ke dalam hash table.
111. Menambahkan pelanggan nomor 15 dengan nama Budi ke dalam hash table.
112. Menambahkan pelanggan nomor 25 dengan nama Citra ke dalam hash table.
113. Menambahkan pelanggan nomor 8 dengan nama Dina ke dalam hash table.
114.
115. Menampilkan teks "Data awal".
116. Menampilkan isi hash table setelah data pelanggan dimasukkan.
117.
118. Melakukan pencarian terhadap pelanggan nomor 15.
119.
120. Memeriksa apakah pelanggan nomor 15 berhasil ditemukan.
121.
122. Menampilkan informasi bahwa pelanggan ditemukan.
123. Menampilkan nomor pelanggan yang ditemukan.
124. Menampilkan nama pelanggan yang ditemukan.
125. Menutup perintah output informasi pelanggan.
126.
127. Menjalankan kondisi jika pelanggan tidak ditemukan.
128.
129. Menampilkan pesan bahwa pelanggan tidak ditemukan.
130.
131. Menghapus data pelanggan nomor 15 dari hash table.
132.
133. Menampilkan informasi bahwa pelanggan nomor 15 telah keluar dari antrian.
134.
135. Menampilkan kembali isi hash table setelah penghapusan data.
136.
137. Melakukan pencarian terhadap pelanggan nomor 25.
138.
139. Memeriksa apakah pelanggan nomor 25 masih ditemukan.
140.
141. Menampilkan informasi bahwa pelanggan nomor 25 masih ditemukan.
142. Menampilkan nomor pelanggan yang ditemukan.
143. Menampilkan nama pelanggan yang ditemukan.
144. Menutup perintah output informasi pelanggan.
145.
146. Menjalankan kondisi jika pelanggan nomor 25 tidak ditemukan.
147.
148. Menampilkan pesan bahwa pelanggan tidak ditemukan.
149.
150.
151. Memeriksa apakah file dijalankan sebagai program utama.
152. Menjalankan fungsi main() untuk memulai seluruh proses program.


d.	Output Program:
 

<img width="488" height="651" alt="Screenshot 2026-06-08 223922" src="https://github.com/user-attachments/assets/5d321564-0cee-4553-9741-4f19440b49d5" />


Penjelasan Output :
Output program menunjukkan bagaimana Hash Map Open Addressing dengan metode Linear Probing bekerja dalam mengatur antrian kasir minimarket. Pada awalnya, pelanggan nomor 5 langsung masuk ke Kasir 5, sedangkan pelanggan nomor 15 dan 25 mengalami collision karena memiliki hasil hash yang sama. Untuk mengatasinya, sistem mencari slot kosong berikutnya secara berurutan sehingga pelanggan nomor 15 ditempatkan di Kasir 6 dan pelanggan nomor 25 di Kasir 7. Pelanggan nomor 8 langsung masuk ke Kasir 8 karena slot masih tersedia.
Selanjutnya, program melakukan pencarian pelanggan nomor 15 dan berhasil menemukan data pelanggan dengan nama Budi. Setelah itu, pelanggan nomor 15 dihapus sehingga slotnya berubah menjadi Antrian Dihapus atau DELETED, bukan langsung kosong, agar pencarian data lain tetap berjalan dengan baik. Hal ini terlihat ketika pelanggan nomor 25 masih berhasil ditemukan meskipun sebelumnya terjadi collision dan salah satu data sudah dihapus. Dari hasil tersebut dapat dilihat bahwa metode Linear Probing mampu menangani collision, pencarian, dan penghapusan data dengan baik.


e.	Link YouTube: https://youtu.be/pzEzzvG_IcU?si=WEgxfOGuCnJUH0a5
