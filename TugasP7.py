def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [1]
    barisan = [1, 1]
    for i in range(2, n):
        barisan.append(barisan[i-1] + barisan[i-2])
    return barisan

def m_kali_n(m, n):
    return m * n

def tampilkan_menu():
    print("Nim Genap")
    print("\nmenu pilihan")
    print("1. Barisan Fibonacci")
    print("2. M Kali N")
    print("0. Keluar")

while True:
    tampilkan_menu()
    pilihan = input("Pilih Menu : ")

    if pilihan == "1":
        jumlah = int(input("Masukkan jumlah Suku : "))
        hasil = fibonacci(jumlah)
        print(" ".join(map(str, hasil)))

    elif pilihan == "2":
        m = int(input("Masukkan nilai M : "))
        n = int(input("Masukkan nilai N : "))
        print(f"Hasil M kali N = {m_kali_n(m, n)}")

    elif pilihan == "0":
        print("Keluar dari program.")
        break

    else:
        print("Pilihan tidak valid, silakan coba lagi.")