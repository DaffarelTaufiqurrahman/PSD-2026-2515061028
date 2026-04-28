def menu():
    print("1. Tampilkan daftar hadir")
    print("2. Tambah siswa hadir")
    print("3. Hapus siswa")
    print("4. Jumlah siswa hadir")
    print("5. Keluar")

def main():
    hadir = ["Lala", "Altaf", "Cinta", "Farel"]
    running = True

    while running:
        menu()

        try:
            pilihan = int(input("Pilihan: "))
        except ValueError:
            print("Masukkan angka yang valid!")
            continue

        if pilihan == 1:
            print("Daftar hadir:", hadir)

        elif pilihan == 2:
            nama = input("Masukkan nama siswa: ")
            hadir.append(nama)
            print("Siswa berhasil ditambahkan.")

        elif pilihan == 3:
            nama = input("Masukkan nama siswa yang dihapus: ")
            if nama in hadir:
                hadir.remove(nama)
                print("Siswa berhasil dihapus.")
            else:
                print("Nama tidak ditemukan.")

        elif pilihan == 4:
            print("Jumlah siswa hadir:", len(hadir))

        elif pilihan == 5:
            running = False
            print("Program selesai.")

        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
