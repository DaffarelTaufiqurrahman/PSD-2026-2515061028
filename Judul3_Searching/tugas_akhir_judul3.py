def sequential_search(data, n, target):
    i = 0
    counter = 0

    while i < n:
        if data[i] == target:
            counter += 1
        i += 1

    return counter


def main():
    data = [
        "Air Mineral",
        "Teh",
        "Kopi",
        "Susu Putih",
        "Susu Cokelat",
        "Jus"
    ]

    n = len(data)

    print("Daftar Produk Minimarket:")
    print(data)

    while True:
        target = input("\nMasukkan nama produk yang ingin dicari: ")

        if target.strip() == "":
            print("Input tidak valid, silakan masukkan nama produk!")
        else:
            break

    counter = sequential_search(data, n, target)

    if counter > 0:
        print(f"Produk '{target}' ditemukan sebanyak {counter} kali.")
    else:
        print(f"Produk '{target}' tidak ditemukan.")


if __name__ == "__main__":
    main()
