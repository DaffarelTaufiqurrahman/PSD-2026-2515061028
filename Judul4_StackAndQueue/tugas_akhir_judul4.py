class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class StackLinkedList:
    def __init__(self):
        self.top_ptr = None

    def is_empty(self):
        return self.top_ptr is None

    
    def push(self, tiket):
        new_node = Node(tiket)
        new_node.next = self.top_ptr
        self.top_ptr = new_node
        print(f"Tiket film '{tiket}' berhasil ditambahkan")

    
    def pop(self):
        if self.is_empty():
            print("Tidak ada tiket")
            return

        temp = self.top_ptr
        print(f"Tiket film '{temp.data}' berhasil dicetak")
        self.top_ptr = self.top_ptr.next

   
    def peek(self):
        if self.is_empty():
            print("Tidak ada tiket")
            return

        print(f"Tiket teratas: {self.top_ptr.data}")

    
    def display(self):
        if self.is_empty():
            print("Tidak ada tiket")
            return

        print("\nDaftar tiket bioskop:")
        current = self.top_ptr
        nomor = 1

        while current is not None:
            print(f"{nomor}. {current.data}")
            current = current.next
            nomor += 1

    
    def count(self):
        jumlah = 0
        current = self.top_ptr

        while current is not None:
            jumlah += 1
            current = current.next

        print(f"Jumlah tiket: {jumlah}")


def main():
    tiket = StackLinkedList()
    pilih = 0

    while pilih != 6:
        print("\n=== SISTEM TIKET BIOSKOP ===")
        print("1. Tambah Tiket")
        print("2. Cetak Tiket")
        print("3. Lihat Tiket Teratas")
        print("4. Tampilkan Semua Tiket")
        print("5. Hitung Jumlah Tiket")
        print("6. Keluar")

        try:
            pilih = int(input("Pilih menu: "))
        except ValueError:
            print("Input harus angka!")
            continue

        if pilih == 1:
            film = input("Masukkan nama film: ")
            tiket.push(film)

        elif pilih == 2:
            tiket.pop()

        elif pilih == 3:
            tiket.peek()

        elif pilih == 4:
            tiket.display()

        elif pilih == 5:
            tiket.count()

        elif pilih == 6:
            print("Program selesai.")

        else:
            print("Menu tidak valid!")


if __name__ == "__main__":
    main()
