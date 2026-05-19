a.	Judul Program: Sistem Tiket Bioskop Menggunakan Stack Linked List


b.	Deskripsi Singkat: 
Program ini dibuat untuk mensimulasikan sistem pengelolaan tiket bioskop menggunakan struktur data stack linked list. Pada program ini, pengguna dapat menambahkan tiket film, mencetak tiket, melihat tiket teratas, menampilkan seluruh tiket, serta menghitung jumlah tiket yang tersimpan. Data tiket yang terakhir dimasukkan akan berada di posisi paling atas dan diproses lebih dahulu.

Algoritma yang diterapkan pada program ini adalah struktur data Stack dengan metode Linked List. Konsep stack menggunakan prinsip LIFO (Last In First Out), yaitu data terakhir yang masuk akan menjadi data pertama yang keluar. Linked list digunakan agar penyimpanan data menjadi lebih fleksibel karena setiap data disimpan dalam node yang saling terhubung.


c.	Source Code:
 <img width="463" height="890" alt="Screenshot 2026-05-19 061945" src="https://github.com/user-attachments/assets/19002220-e1ae-42f2-8f80-df45e5d7b440" />
<img width="341" height="761" alt="Screenshot 2026-05-19 062022" src="https://github.com/user-attachments/assets/333fc745-85c9-48ac-a412-57ddac760dec" />


 
Penjelasan logika berjalannya kode program:
1.	Pada baris ini dibuat class Node untuk menyimpan data tiket. 
2.	Method __init__ dibuat untuk membuat data awal pada class Node.
3.	Baris ini digunakan untuk menyimpan data tiket ke dalam variabel data. 
4.	next diatur bernilai None karena node belum terhubung dengan node lain. 
5.	
6.	
7.	Pada baris ini dibuat class StackLinkedList untuk menerapkan struktur data stack menggunakan linked list. 
8.	Constructor dibuat pada class StackLinkedList. 
9.	Baris ini digunakan untuk menginisialisasi top_ptr sebagai penunjuk elemen paling atas pada stack. 
10.	
11.	Method is_empty() dibuat untuk mengecek apakah stack kosong atau tidak. 
12.	Method ini akan mengembalikan nilai True jika top_ptr bernilai None. 
13.	
14.	
15.	Pada baris ini dibuat method push() untuk menambahkan tiket ke dalam stack. 
16.	Node baru dibuat berdasarkan data tiket yang dimasukkan. 
17.	Node baru dihubungkan ke node teratas sebelumnya. 
18.	top_ptr dipindahkan ke node baru agar node tersebut menjadi elemen paling atas. 
19.	Baris ini menampilkan pesan bahwa tiket berhasil ditambahkan. 
20.	
21.	
22.	Method pop() dibuat untuk mencetak sekaligus menghapus tiket paling atas. 
23.	Pada bagian ini dilakukan pengecekan apakah stack kosong. 
24.	Jika stack kosong maka program akan menampilkan pesan tidak ada tiket. 
25.	Program dihentikan sementara karena tidak ada data yang bisa diproses. 
26.	
27.	Node paling atas disimpan ke dalam variabel sementara bernama temp. 
28.	Baris ini digunakan untuk menampilkan tiket yang berhasil dicetak. 
29.	top_ptr dipindahkan ke node berikutnya setelah tiket dihapus. 
30.	
31.	
32.	Method peek() dibuat untuk melihat tiket paling atas tanpa menghapusnya. 
33.	Pada bagian ini dilakukan pengecekan apakah stack kosong. 
34.	Jika kosong maka program menampilkan pesan tidak ada tiket. 
35.	Program dihentikan karena tidak ada data yang dapat ditampilkan. 
36.	
37.	Baris ini digunakan untuk menampilkan tiket yang berada di posisi teratas. 
38.	
39.	
40.	Method display() dibuat untuk menampilkan seluruh tiket dalam stack. 
41.	Pada bagian ini dilakukan pengecekan apakah stack kosong. 
42.	Jika kosong maka program menampilkan pesan tidak ada tiket. 
43.	Program dihentikan karena tidak ada data yang bisa ditampilkan. 
44.	
45.	Baris ini digunakan untuk menampilkan judul daftar tiket bioskop. 
46.	Node teratas disimpan ke variabel current untuk proses traversal. 
47.	Variabel nomor dibuat untuk memberikan nomor urut pada daftar tiket. 
48.	
49.	Perulangan dilakukan selama current masih memiliki data. 
50.	Baris ini menampilkan nomor urut dan nama tiket. 
51.	current dipindahkan ke node berikutnya. 
52.	Nilai nomor ditambah satu setiap perulangan. 
53.	
54.	
55.	Method count() dibuat untuk menghitung jumlah tiket yang ada pada stack. 
56.	Variabel jumlah dibuat dengan nilai awal 0. 
57.	Node teratas disimpan ke variabel current. 
58.	
59.	Perulangan dilakukan selama node masih tersedia. 
60.	Nilai jumlah akan bertambah satu setiap ada node. 
61.	current dipindahkan ke node berikutnya. 
62.	
63.	Baris ini digunakan untuk menampilkan total jumlah tiket. 
64.	
65.	
66.	Fungsi utama main() dibuat untuk menjalankan program. 
67.	Pada baris ini dibuat objek tiket dari class StackLinkedList. 
68.	Variabel pilih dibuat dengan nilai awal 0. 
69.	
70.	Perulangan akan terus berjalan selama pengguna belum memilih menu keluar. 
71.	Baris ini menampilkan judul menu program sistem tiket bioskop. 
72.	Program menampilkan menu tambah tiket. 
73.	Program menampilkan menu cetak tiket. 
74.	Program menampilkan menu melihat tiket teratas. 
75.	Program menampilkan menu menampilkan semua tiket. 
76.	Program menampilkan menu menghitung jumlah tiket. 
77.	Program menampilkan menu keluar. 
78.	
79.	try digunakan untuk menangani kemungkinan error pada input. 
80.	Program meminta pengguna memasukkan pilihan menu. 
81.	Bagian ini dijalankan jika pengguna memasukkan input yang salah. 
82.	Program menampilkan pesan bahwa input harus berupa angka. 
83.	Perulangan diulang kembali ke awal menu. 
84.	
85.	Pada bagian ini dilakukan pengecekan apakah pengguna memilih menu 1. 
86.	Program meminta pengguna memasukkan nama film. 
87.	Data film dimasukkan ke stack menggunakan method push(). 
88.	
89.	Dilakukan pengecekan apakah pengguna memilih menu 2. 
90.	Program menjalankan method pop() untuk mencetak tiket. 
91.	
92.	Dilakukan pengecekan apakah pengguna memilih menu 3. 
93.	Program menjalankan method peek() untuk melihat tiket teratas. 
94.	
95.	Dilakukan pengecekan apakah pengguna memilih menu 4. 
96.	Program menjalankan method display() untuk menampilkan semua tiket. 
97.	
98.	Dilakukan pengecekan apakah pengguna memilih menu 5. 
99.	Program menjalankan method count() untuk menghitung jumlah tiket. 
100.	
101.	Dilakukan pengecekan apakah pengguna memilih menu 6. 
102.	Program menampilkan pesan bahwa program selesai dijalankan. 
103.	
104.	Bagian ini dijalankan jika menu yang dipilih tidak tersedia. 
105.	Program menampilkan pesan bahwa menu tidak valid. 
106.	
107.	
108.	Baris ini digunakan untuk memastikan program dijalankan dari file utama. 
109.	Fungsi main() dijalankan agar program dapat dieksekusi. 


d.	Output Program:
 <img width="305" height="811" alt="Screenshot 2026-05-19 062151" src="https://github.com/user-attachments/assets/33809fe5-8985-431a-a759-99e55af1c0c9" />
<img width="332" height="292" alt="Screenshot 2026-05-19 062234" src="https://github.com/user-attachments/assets/e757f8cd-fab3-417b-b643-77e70b88f556" />

 
Penjelasan Output :
Output program tersebut menunjukkan proses kerja sistem tiket bioskop yang menggunakan struktur data stack linked list. Saat program dijalankan, muncul beberapa menu seperti tambah tiket, cetak tiket, lihat tiket teratas, tampilkan semua tiket, hitung jumlah tiket, dan keluar. Pada percobaan ini dipilih menu 1 untuk menambahkan tiket film “DILAN”. Setelah nama film dimasukkan, program menampilkan pesan bahwa tiket film “DILAN” berhasil ditambahkan ke dalam stack. Setelah itu, menu 1 dipilih kembali untuk menambahkan tiket film “MARIPOSA”, lalu program kembali menampilkan pesan bahwa tiket berhasil ditambahkan.

Selanjutnya dipilih menu 3 untuk melihat tiket teratas. Output menunjukkan bahwa tiket teratas adalah “MARIPOSA”. Hal ini terjadi karena stack menggunakan konsep LIFO (Last In First Out), yaitu data yang terakhir masuk akan berada di posisi paling atas dan diproses lebih dahulu.

Kemudian dipilih menu 4 untuk menampilkan seluruh tiket yang ada pada stack. Output menampilkan daftar tiket dengan urutan “MARIPOSA” di posisi pertama dan “DILAN” di posisi kedua. Urutan tersebut menunjukkan bahwa tiket terakhir yang dimasukkan berada di atas tiket sebelumnya.

Setelah itu dipilih menu 5 untuk menghitung jumlah tiket yang tersimpan di dalam stack. Program menampilkan output “Jumlah tiket: 2”, yang berarti terdapat dua data tiket yang berhasil disimpan. Dari output tersebut dapat dilihat bahwa program stack linked list berhasil menjalankan fungsi push, peek, display, dan count sesuai konsep stack.


e. Link YouTube: https://youtu.be/cdUan2AmvEU?si=cuNf0R6g3af7jnvW
