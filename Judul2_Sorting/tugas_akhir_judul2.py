def tukar(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def bubble_sort(arr, n):
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                tukar(arr, j, j + 1)


def main():
    try:
        n = int(input("Masukkan jumlah baju: "))
    except ValueError:
        print("Input tidak valid!")
        return

    arr = []
    print("Masukkan ukuran baju (S/M/L):")

    konversi = {"S": 1, "M": 2, "L": 3}
    balik = {1: "S", 2: "M", 3: "L"}

    for i in range(n):
        while True:
            try:
                ukuran = input().upper()
                if ukuran in konversi:
                    arr.append(konversi[ukuran])
                    break
                else:
                    print("Input tidak valid, masukkan S/M/L!")
            except:
                print("Input tidak valid!")

    print("Array sebelum diurutkan:", [balik[x] for x in arr])

    bubble_sort(arr, n)

    print("Array setelah diurutkan (Bubble Sort): ", end=" ")
    for i in range(n):
        print(balik[arr[i]], end=" ")
    print()


if __name__ == "__main__":
    main()
