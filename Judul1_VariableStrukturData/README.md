a.	Judul Program: Program Daftar Kehadiran Siswa Menggunakan List 1 Dimensi

b. Deskripsi Singkat: 
Program ini dibuat menggunakan bahasa Python untuk membantu mencatat kehadiran siswa secara sederhana. Melalui program ini, pengguna dapat melihat daftar siswa yang hadir, menambahkan nama siswa baru, mengetahui jumlah siswa yang hadir, serta keluar dari program setelah selesai digunakan. Dengan adanya program ini, proses pencatatan kehadiran menjadi lebih mudah, cepat, dan teratur.
Struktur data yang digunakan pada program ini adalah list satu dimensi, yaitu kumpulan data yang disimpan dalam satu variabel berbentuk daftar. Setiap nama siswa disimpan sebagai elemen di dalam list. Selain itu, program ini juga menerapkan konsep dasar pemrograman seperti perulangan (`while`), percabangan (`if`, `elif`, `else`), serta fungsi bawaan Python seperti `append()` untuk menambah data dan `len()` untuk menghitung jumlah data.

c. Source Code:
 <img width="491" height="793" alt="Screenshot 2026-04-28 164150" src="https://github.com/user-attachments/assets/19a31de5-5a52-4a3d-a700-8cf7ce2c3496" />

Penjelasan logika berjalannya kode program:
1. Baris ini digunakan untuk membuat fungsi bernama `menu()`. Fungsi ini berisi beberapa perintah `print()` yang nantinya dipanggil untuk menampilkan daftar menu pilihan kepada pengguna.  
2. Baris ini menampilkan tulisan menu nomor 1 yaitu pilihan untuk melihat daftar siswa yang hadir saat ini.  
3. Baris ini menampilkan tulisan menu nomor 2 yaitu pilihan untuk menambahkan nama siswa baru ke dalam daftar hadir.  
4. Baris ini menampilkan tulisan menu nomor 3 yaitu pilihan untuk menghapus nama siswa dari daftar hadir.  
5. Baris ini menampilkan tulisan menu nomor 4 yaitu pilihan untuk melihat jumlah seluruh siswa yang ada di daftar hadir.  
6. Baris ini menampilkan tulisan menu nomor 5 yaitu pilihan untuk keluar dan menghentikan program.  
7.  
8. Baris ini digunakan untuk membuat fungsi utama bernama `main()`. Semua proses utama program dijalankan di dalam fungsi ini.  
9. Baris ini membuat variabel `hadir` dengan tipe data list yang berisi data awal nama siswa yaitu `Lala`, `Altaf`, `Cinta`, dan `Farel`. List ini digunakan untuk menyimpan data kehadiran siswa.  
10. Baris ini membuat variabel `running` bernilai `True`. Variabel ini berfungsi sebagai pengontrol perulangan agar program terus berjalan selama nilainya masih `True`.  
11.  
12. Baris ini menjalankan perulangan `while`. Selama variabel `running` bernilai `True`, maka program akan terus menampilkan menu dan meminta input pengguna.  
13. Baris ini memanggil fungsi `menu()` sehingga daftar pilihan menu ditampilkan setiap kali perulangan berjalan.  
14.  
15. Baris ini menggunakan `try` untuk mencoba menjalankan proses input dari pengguna. Tujuannya agar program dapat menangani kesalahan input tanpa langsung berhenti.  
16. Baris ini meminta pengguna memasukkan nomor pilihan menu. Input yang diterima diubah ke tipe data integer menggunakan `int()`. Nilai input disimpan ke variabel `pilihan`.  
17. Baris ini adalah bagian `except ValueError`, yaitu akan dijalankan jika pengguna memasukkan data selain angka, misalnya huruf atau simbol.  
18. Baris ini menampilkan pesan bahwa input yang dimasukkan salah dan pengguna harus memasukkan angka yang valid.  
19. Baris ini menggunakan `continue` untuk mengulang kembali ke awal perulangan sehingga menu akan ditampilkan lagi tanpa menjalankan baris berikutnya.  
20.  
21. Baris ini memeriksa apakah nilai `pilihan` sama dengan `1`. Jika benar, maka program akan menjalankan perintah untuk menampilkan daftar hadir.  
22. Baris ini menampilkan isi variabel `hadir`, yaitu daftar nama siswa yang sedang tersimpan di dalam list.  
23.  
24. Baris ini memeriksa apakah nilai `pilihan` sama dengan `2`. Jika benar, maka program masuk ke proses penambahan data siswa baru.  
25. Baris ini meminta pengguna memasukkan nama siswa yang ingin ditambahkan ke daftar hadir. Input disimpan ke variabel `nama`.  
26. Baris ini menambahkan isi variabel `nama` ke bagian akhir list `hadir` menggunakan method `append()`.  
27. Baris ini menampilkan pesan bahwa nama siswa berhasil ditambahkan ke dalam daftar hadir.  
28.  
29. Baris ini memeriksa apakah nilai `pilihan` sama dengan `3`. Jika benar, maka program menjalankan proses penghapusan data siswa.  
30. Baris ini meminta pengguna memasukkan nama siswa yang ingin dihapus dari daftar hadir. Input disimpan ke variabel `nama`.  
31. Baris ini mengecek apakah nama yang dimasukkan pengguna terdapat di dalam list `hadir` menggunakan operator `in`.  
32. Jika nama ditemukan, maka baris ini akan menghapus nama tersebut dari list `hadir` menggunakan method `remove()`.  
33. Setelah data berhasil dihapus, baris ini menampilkan pesan bahwa siswa berhasil dihapus dari daftar hadir.  
34. Baris ini adalah bagian `else` dari pengecekan sebelumnya. Bagian ini dijalankan jika nama yang dimasukkan tidak ditemukan di dalam list.  
35. Baris ini menampilkan pesan bahwa nama siswa yang dimasukkan tidak ditemukan sehingga tidak bisa dihapus.  
36.  
37. Baris ini memeriksa apakah nilai `pilihan` sama dengan `4`. Jika benar, maka program akan menampilkan jumlah siswa hadir.  
38. Baris ini menghitung banyaknya data yang ada di dalam list `hadir` menggunakan fungsi `len()`, kemudian hasilnya ditampilkan ke layar.  
39.  
40. Baris ini memeriksa apakah nilai `pilihan` sama dengan `5`. Jika benar, maka program akan keluar.  

41. Baris ini mengubah nilai variabel `running` menjadi `False` sehingga perulangan `while` berhenti dan program selesai dijalankan.  
42. Baris ini menampilkan pesan bahwa program telah selesai dijalankan.  
43.  
44. Baris ini adalah bagian `else` terakhir yang dijalankan jika pengguna memasukkan angka selain 1, 2, 3, 4, atau 5.  
45. Baris ini menampilkan pesan bahwa pilihan menu yang dimasukkan tidak tersedia atau tidak valid.  
46.  
47. Baris ini digunakan untuk mengecek apakah file Python dijalankan secara langsung, bukan diimpor dari file lain.  
48. Jika kondisi pada baris 47 benar, maka fungsi `main()` dipanggil sehingga seluruh program mulai dijalankan.  

d. Output Program:
<img width="455" height="814" alt="Screenshot 2026-04-28 165548" src="https://github.com/user-attachments/assets/a32280b7-459f-48d4-8ff0-ba6771fe9537" />

Penjelasan Output :
Berdasarkan hasil output yang ditampilkan, program dapat berjalan dengan baik sesuai fungsi yang telah dirancang. Program menampilkan menu utama yang terdiri dari lima pilihan, yaitu menampilkan daftar hadir, menambah siswa hadir, menghapus siswa, melihat jumlah siswa hadir, dan keluar dari program. Setelah pengguna memilih salah satu menu, program akan memproses perintah tersebut kemudian kembali menampilkan menu utama.

Pada saat pengguna memilih menu 1, program menampilkan daftar hadir awal yaitu ['Lala', 'Altaf', 'Cinta', 'Farel']. Hal ini menunjukkan bahwa data awal yang tersimpan pada list berhasil dibaca dan ditampilkan dengan benar.

Pada saat pengguna memilih menu 2, pengguna memasukkan nama siswa baru yaitu Raina. Setelah itu program menampilkan pesan "Siswa berhasil ditambahkan." yang menandakan data baru berhasil dimasukkan ke dalam list melalui fungsi `append()`.

Pada saat pengguna memilih menu 3, pengguna memasukkan nama siswa Cinta untuk dihapus dari daftar hadir. Program kemudian menampilkan pesan "Siswa berhasil dihapus." yang berarti nama tersebut ditemukan di dalam list dan berhasil dihapus menggunakan fungsi `remove()`.

Pada saat pengguna memilih menu 4, program menampilkan jumlah siswa hadir sebanyak 4 orang. Jumlah tersebut sudah sesuai, karena data awal berjumlah 4 siswa, kemudian ditambah 1 siswa menjadi 5 siswa, lalu dikurangi 1 siswa sehingga tersisa 4 siswa.

Pada saat pengguna memilih menu 5, program menampilkan pesan "Program selesai." yang berarti program berhenti dan keluar dengan normal tanpa terjadi kesalahan.

Secara keseluruhan, hasil output membuktikan bahwa seluruh fitur program, seperti menampilkan data, menambah data, menghapus data, menghitung jumlah data, serta keluar dari program, telah berjalan dengan baik sesuai yang diharapkan.

e. Link YouTube: https://www.youtube.com/watch?feature=shared&v=xteuBq-BzIw
