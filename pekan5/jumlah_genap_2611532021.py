# Buat file dengan nama jumlah_genap_NIM.py
# Buat program untuk perulangan for dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

ulang_2021 = int(input("Masukan nilai batas: "))

jumlah_2021 = 0
for i_2021 in range(1, ulang_2021 + 1):
    if i_2021 % 2 == 0:
        print(i_2021, end=" ")
        jumlah_2021 = jumlah_2021 + i_2021

        if i_2021 < ulang_2021:
            print(" + ", end="")
        else:
            print(" = ", jumlah_2021, end="")
print()
print("Jumlah =", jumlah_2021)