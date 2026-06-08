class SlotState:
    EMPTY = 0
    OCCUPIED = 1
    DELETED = 2


class Entry:
    def __init__(self):
        self.key = None
        self.value = None
        self.state = SlotState.EMPTY


class HashMapOpenAddressing:
    def __init__(self, size=10):
        self.SIZE = size
        self.table = [Entry() for _ in range(self.SIZE)]

    def hash_function(self, key):
        return (key % self.SIZE + self.SIZE) % self.SIZE

    def insert(self, nomor_pelanggan, nama):
        idx = self.hash_function(nomor_pelanggan)
        first_deleted = -1

        for step in range(self.SIZE):

            i = (idx + step) % self.SIZE

            if self.table[i].state == SlotState.OCCUPIED:

                if self.table[i].key == nomor_pelanggan:
                    self.table[i].value = nama
                    return True

            elif self.table[i].state == SlotState.DELETED:

                if first_deleted == -1:
                    first_deleted = i

            else:

                if first_deleted != -1:
                    i = first_deleted

                self.table[i].key = nomor_pelanggan
                self.table[i].value = nama
                self.table[i].state = SlotState.OCCUPIED

                return True

        return False

    def search(self, nomor_pelanggan):

        idx = self.hash_function(nomor_pelanggan)

        for step in range(self.SIZE):

            i = (idx + step) % self.SIZE

            if self.table[i].state == SlotState.EMPTY:
                return None

            if (self.table[i].state == SlotState.OCCUPIED and
                    self.table[i].key == nomor_pelanggan):

                return self.table[i]

        return None

    def remove_key(self, nomor_pelanggan):

        entry = self.search(nomor_pelanggan)

        if entry is None:
            return False

        entry.state = SlotState.DELETED

        return True

    def display(self):

        print("\n=== Posisi Antrian Kasir Minimarket ===")

        for i in range(self.SIZE):

            print(f"Kasir {i}: ", end="")

            if self.table[i].state == SlotState.EMPTY:

                print("Kosong")

            elif self.table[i].state == SlotState.DELETED:

                print("Antrian Dihapus")

            else:

                print(
                    f"Pelanggan {self.table[i].key} ({self.table[i].value})"
                )


def main():

    kasir = HashMapOpenAddressing()

    kasir.insert(5, "Andi")
    kasir.insert(15, "Budi")
    kasir.insert(25, "Citra")
    kasir.insert(8, "Dina")

    print("Data awal:")
    kasir.display()

    hasil = kasir.search(15)

    if hasil is not None:

        print(
            f"\nPelanggan nomor {hasil.key} ditemukan "
            f"dengan nama {hasil.value}"
        )

    else:

        print("\nPelanggan tidak ditemukan")

    kasir.remove_key(15)

    print("\nSetelah pelanggan nomor 15 keluar:")

    kasir.display()

    hasil = kasir.search(25)

    if hasil is not None:

        print(
            f"\nPelanggan nomor {hasil.key} masih ditemukan "
            f"dengan nama {hasil.value}"
        )

    else:

        print("\nPelanggan tidak ditemukan")


if __name__ == "__main__":
    main()
