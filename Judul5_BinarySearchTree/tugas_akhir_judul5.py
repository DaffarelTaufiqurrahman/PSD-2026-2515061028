class Node:
    def __init__(self, tinggi):
        self.tinggi = tinggi
        self.left = None
        self.right = None


class BSTTinggiMahasiswa:
    def __init__(self):
        self.root = None

    def insert_node(self, root, tinggi):
        if root is None:
            return Node(tinggi)

        if tinggi < root.tinggi:
            root.left = self.insert_node(root.left, tinggi)

        elif tinggi > root.tinggi:
            root.right = self.insert_node(root.right, tinggi)

        return root

    def insert(self, tinggi):
        self.root = self.insert_node(self.root, tinggi)

    def search_node(self, root, tinggi):
        if root is None:
            return False

        if root.tinggi == tinggi:
            return True

        if tinggi < root.tinggi:
            return self.search_node(root.left, tinggi)

        return self.search_node(root.right, tinggi)

    def search(self, tinggi):
        return self.search_node(self.root, tinggi)

    def inorder(self, root):
        if root is None:
            return

        self.inorder(root.left)
        print(root.tinggi, end=" ")
        self.inorder(root.right)

    def preorder(self, root):
        if root is None:
            return

        print(root.tinggi, end=" ")
        self.preorder(root.left)
        self.preorder(root.right)

    def postorder(self, root):
        if root is None:
            return

        self.postorder(root.left)
        self.postorder(root.right)
        print(root.tinggi, end=" ")

    def find_min(self, root):
        if root is None:
            return -1

        current = root

        while current.left is not None:
            current = current.left

        return current.tinggi

    def find_max(self, root):
        if root is None:
            return -1

        current = root

        while current.right is not None:
            current = current.right

        return current.tinggi

    def count_nodes(self, root):
        if root is None:
            return 0

        return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)

    def sum_nodes(self, root):
        if root is None:
            return 0

        return root.tinggi + self.sum_nodes(root.left) + self.sum_nodes(root.right)


def main():
    bst = BSTTinggiMahasiswa()
    pilih = 0

    while pilih != 10:
        print("\n=== BST Tinggi Badan Mahasiswa ===")
        print("1. Tambah Tinggi Badan")
        print("2. Cari Tinggi Badan")
        print("3. Inorder")
        print("4. Preorder")
        print("5. Postorder")
        print("6. Tinggi Minimum")
        print("7. Tinggi Maksimum")
        print("8. Jumlah Mahasiswa")
        print("9. Total Tinggi")
        print("10. Keluar")

        try:
            pilih = int(input("Pilih menu: "))
        except ValueError:
            print("Input tidak valid!")
            continue

        if pilih == 1:
            try:
                tinggi = int(input("Masukkan tinggi badan mahasiswa (cm): "))
                bst.insert(tinggi)
                print(f"Tinggi badan {tinggi} cm berhasil ditambahkan")
            except ValueError:
                print("Input tidak valid!")

        elif pilih == 2:
            try:
                tinggi = int(input("Cari tinggi badan: "))

                if bst.search(tinggi):
                    print("Data tinggi badan ditemukan")
                else:
                    print("Data tinggi badan tidak ditemukan")

            except ValueError:
                print("Input tidak valid!")

        elif pilih == 3:
            print("Inorder: ", end="")
            bst.inorder(bst.root)
            print()

        elif pilih == 4:
            print("Preorder: ", end="")
            bst.preorder(bst.root)
            print()

        elif pilih == 5:
            print("Postorder: ", end="")
            bst.postorder(bst.root)
            print()

        elif pilih == 6:
            print(f"Tinggi minimum: {bst.find_min(bst.root)} cm")

        elif pilih == 7:
            print(f"Tinggi maksimum: {bst.find_max(bst.root)} cm")

        elif pilih == 8:
            print(f"Jumlah mahasiswa: {bst.count_nodes(bst.root)}")

        elif pilih == 9:
            print(f"Total tinggi badan: {bst.sum_nodes(bst.root)} cm")

        elif pilih == 10:
            print("Program selesai.")

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()
