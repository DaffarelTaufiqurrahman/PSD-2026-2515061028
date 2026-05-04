a.	Judul Program: Program Pengurutan Ukuran Baju Menggunakan Metode Bubble Sort

b.	Deskripsi Singkat: 
Program ini dibuat untuk mengurutkan data ukuran baju yang dimasukkan oleh pengguna, yaitu S, M, dan L. Pengguna diminta memasukkan jumlah data, lalu menginput ukuran baju satu per satu. Data tersebut kemudian diproses dan ditampilkan sebelum serta setelah dilakukan pengurutan.
Metode yang digunakan dalam program ini adalah Bubble Sort, yaitu teknik pengurutan dengan cara membandingkan dua data yang bersebelahan, lalu menukarnya jika urutannya belum sesuai. Proses ini dilakukan berulang sampai semua data tersusun dari ukuran paling kecil ke paling besar.

c.	Source Code:
<img width="479" height="839" alt="Screenshot 2026-05-04 232039" src="https://github.com/user-attachments/assets/f62bbea5-c905-454c-9d9b-77fdee53e305" />

Penjelasan logika berjalannya kode program:
1.	def tukar(arr, i, j): digunakan untuk membuat fungsi yang berfungsi menukar dua data dalam array.
2.	temp = arr[i] digunakan untuk menyimpan sementara nilai pada posisi ke-i.
3.	arr[i] = arr[j] digunakan untuk mengganti nilai di posisi ke-i dengan nilai dari posisi ke-j.
4.	arr[j] = temp digunakan untuk mengisi posisi ke-j dengan nilai yang tadi disimpan.
5.	
6.	
7.	def bubble_sort(arr, n): digunakan untuk membuat fungsi pengurutan data dengan metode bubble sort.
8.	for i in range(n - 1): digunakan untuk mengulang proses pengurutan sebanyak n-1 kali.
9.	for j in range(n - i - 1): digunakan untuk membandingkan data yang letaknya bersebelahan.
10.	if arr[j] > arr[j + 1]: digunakan untuk mengecek apakah urutan data masih salah.
11.	tukar(arr, j, j + 1) digunakan untuk menukar posisi data jika urutannya tidak sesuai.
12.	
13.	
14.	def main(): digunakan sebagai fungsi utama tempat program dijalankan.
15.	try: digunakan untuk mencoba menjalankan program dan menghindari error.
16.	n = int(input("Masukkan jumlah baju: ")) digunakan untuk menerima jumlah data dari pengguna.
17.	except ValueError: digunakan untuk menangani kesalahan jika input bukan angka.
18.	print("Input tidak valid!") digunakan untuk menampilkan pesan kesalahan.
19.	return digunakan untuk menghentikan program jika terjadi kesalahan.
20.	
21.	arr = [] digunakan untuk membuat list kosong sebagai tempat menyimpan data.
22.	print("Masukkan ukuran baju (S/M/L):") digunakan untuk memberi petunjuk kepada pengguna.
23.	
24.	konversi = {"S": 1, "M": 2, "L": 3} digunakan untuk mengubah ukuran baju menjadi angka.
25.	balik = {1: "S", 2: "M", 3: "L"} digunakan untuk mengubah angka kembali menjadi ukuran baju.
26.	
27.	for i in range(n): digunakan untuk mengulang input sesuai jumlah data.
28.	while True: digunakan agar input terus diminta sampai benar.
29.	try: digunakan untuk menghindari kesalahan saat input.
30.	ukuran = input().upper() digunakan untuk mengambil input dan mengubahnya menjadi huruf besar.
31.	if ukuran in konversi: digunakan untuk memastikan input sesuai (S, M, atau L).
32.	arr.append(konversi[ukuran]) digunakan untuk menyimpan data ke dalam array.
33.	break digunakan untuk keluar dari perulangan jika input sudah benar.
34.	else: digunakan jika input tidak sesuai.
35.	print("Input tidak valid, masukkan S/M/L!") digunakan untuk memberi tahu bahwa input salah.
36.	except: digunakan untuk menangani kesalahan lain.
37.	print("Input tidak valid!") digunakan untuk menampilkan pesan error umum.
38.	
39.	print("Array sebelum diurutkan:", [balik[x] for x in arr]) digunakan untuk menampilkan data sebelum diurutkan.
40.	
41.	bubble_sort(arr, n) digunakan untuk menjalankan proses pengurutan.
42.	
43.	print("Array setelah diurutkan (Bubble Sort): ", end=" ") digunakan untuk menampilkan hasil setelah diurutkan.
44.	for i in range(n): digunakan untuk menampilkan seluruh data.
45.	print(balik[arr[i]], end=" ") digunakan untuk menampilkan hasil dalam bentuk ukuran baju.
46.	print() digunakan untuk membuat baris baru.
47.	
48.	
49.	if __name__ == "__main__": digunakan untuk memastikan program dijalankan langsung.
50.	main() digunakan untuk menjalankan fungsi utama.

d.	Output Program:
<img width="343" height="161" alt="Screenshot 2026-05-04 233404" src="https://github.com/user-attachments/assets/48cb085f-c932-4e37-b99e-ab6316f10176" />

Penjelasan Output :
Program dimulai dengan meminta pengguna memasukkan jumlah data sebanyak 5, kemudian pengguna menginput ukuran baju secara berurutan yaitu M, L, L, S, dan L. Data yang dimasukkan tersebut disimpan ke dalam array dan diubah ke bentuk angka agar dapat diproses oleh program, dengan ketentuan S = 1, M = 2, dan L = 3. Sebelum proses pengurutan dilakukan, program menampilkan data awal yaitu ['M', 'L', 'L', 'S', 'L'], yang masih sesuai dengan urutan input pengguna. Setelah itu, program menjalankan metode Bubble Sort, yaitu dengan membandingkan data yang posisinya bersebelahan dan menukarnya jika urutannya tidak tepat. Proses ini dilakukan berulang sampai semua data tersusun dengan benar. Hasil akhirnya adalah S M L L L, yang menunjukkan bahwa data telah berhasil diurutkan dari ukuran paling kecil ke paling besar, yaitu S, M, kemudian L.

e. Link YouTube: https://youtu.be/XS1Pj-x2MY8?feature=shared
