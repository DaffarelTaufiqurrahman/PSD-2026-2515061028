a.	Judul Program: Program Pencarian Produk Minimarket Menggunakan Sequential Searching

b.	Deskripsi Singkat: 
Program ini saya buat untuk melakukan pencarian produk minimarket menggunakan metode Sequential Search. Pada program ini, pengguna dapat memasukkan nama produk yang ingin dicari, kemudian program akan mencari data tersebut secara berurutan mulai dari data pertama sampai data terakhir. Setelah proses pencarian selesai, program akan menampilkan apakah produk ditemukan atau tidak beserta jumlah kemunculannya pada data. Metode Sequential Search yang digunakan pada program ini bekerja dengan cara memeriksa setiap data satu per satu hingga data yang dicari ditemukan. Metode ini cocok digunakan pada data yang belum terurut dan jumlah datanya tidak terlalu banyak.

c.	Source Code:
 <img width="649" height="893" alt="Screenshot 2026-05-11 222317" src="https://github.com/user-attachments/assets/a82109fa-14e7-4fac-8c56-442ed60d4649" />

Penjelasan logika berjalannya kode program:
1.	def sequential_search(data, n, target): digunakan untuk membuat fungsi pencarian data secara berurutan pada list produk.
2.	i = 0 digunakan untuk menentukan posisi awal pencarian dimulai dari indeks pertama.
3.	counter = 0 digunakan untuk menghitung jumlah data yang ditemukan.
4.	
5.	while i < n: digunakan untuk melakukan perulangan selama indeks masih kurang dari jumlah data.
6.	if data[i] == target: digunakan untuk mengecek apakah data saat ini sama dengan data yang dicari.
7.	counter += 1 digunakan untuk menambah jumlah data yang ditemukan.
8.	i += 1 digunakan untuk berpindah ke data berikutnya.
9.	
10.	return counter digunakan untuk mengembalikan jumlah data yang ditemukan ke program utama.
11.	
12.	
13.	def main(): digunakan untuk membuat fungsi utama program.
14.	data = [ digunakan untuk membuat list data produk minimarket.
15.	"Air Mineral", digunakan untuk menambahkan data produk Air Mineral ke dalam list.
16.	"Teh", digunakan untuk menambahkan data produk Teh ke dalam list.
17.	"Kopi", digunakan untuk menambahkan data produk Kopi ke dalam list.
18.	"Susu Putih", digunakan untuk menambahkan data produk Susu Putih ke dalam list.
19.	"Susu Cokelat", digunakan untuk menambahkan data produk Susu Cokelat ke dalam list.
20.	"Jus" digunakan untuk menambahkan data produk Jus ke dalam list.
21.	] digunakan untuk menutup list data produk.
22.	
23.	n = len(data) digunakan untuk menghitung jumlah seluruh data pada list.
24.	
25.	print("Daftar Produk Minimarket:") digunakan untuk menampilkan judul daftar produk.
26.	print(data) digunakan untuk menampilkan seluruh data produk yang tersimpan pada list.
27.	
28.	while True: digunakan untuk melakukan perulangan sampai input yang dimasukkan valid.
29.	target = input("\nMasukkan nama produk yang ingin dicari: ") digunakan untuk menerima input nama produk dari pengguna.
30.	
31.	if target.strip() == "": digunakan untuk mengecek apakah input kosong.
32.	print("Input tidak valid, silakan masukkan nama produk!") digunakan untuk menampilkan pesan kesalahan jika input kosong.
33.	else: digunakan untuk menjalankan kondisi jika input sudah benar.
34.	break digunakan untuk menghentikan perulangan input.
35.	
36.	counter = sequential_search(data, n, target) digunakan untuk memanggil fungsi pencarian sequential search.
37.	
38.	if counter > 0: digunakan untuk mengecek apakah data ditemukan.
39.	print(f"Produk '{target}' ditemukan sebanyak {counter} kali.") digunakan untuk menampilkan pesan bahwa produk ditemukan.
40.	else: digunakan untuk menjalankan kondisi jika produk tidak ditemukan.
41.	print(f"Produk '{target}' tidak ditemukan.") digunakan untuk menampilkan pesan bahwa produk tidak ada pada data.
42.	
43.	
44.	if __name__ == "__main__": digunakan untuk memastikan program dijalankan langsung dari file utama.
45.	main() digunakan untuk menjalankan fungsi utama program.

d.	Output Program:
 <img width="555" height="126" alt="Screenshot 2026-05-11 222704" src="https://github.com/user-attachments/assets/d6874cef-2aac-4ebd-823d-b33830acc39e" />
 
Penjelasan Output :
Berdasarkan hasil output program, proses pencarian data berhasil dijalankan menggunakan metode Sequential Search. Pertama, program menampilkan daftar produk minimarket yang tersedia, yaitu Air Mineral, Teh, Kopi, Susu Putih, Susu Cokelat, dan Jus. Setelah itu, pengguna diminta memasukkan nama produk yang ingin dicari. Pada contoh output, saya memasukkan produk “Susu Cokelat”. Program kemudian melakukan pencarian secara berurutan mulai dari data pertama hingga data terakhir sampai produk ditemukan. Karena produk “Susu Cokelat” terdapat satu kali pada list, maka program menampilkan pesan bahwa produk tersebut ditemukan sebanyak 1 kali. Dari hasil tersebut dapat diketahui bahwa metode Sequential Search bekerja dengan cara mengecek data satu per satu secara berurutan hingga data yang dicari berhasil ditemukan.

e. Link YouTube: https://youtu.be/r0ZMJ5GKLxE?si=Ndvbog6iWbPszM0q
