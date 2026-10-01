# Buat file dengan nama nested_for3_NIM.py
# Buat program untuk perulangan for dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

batas_2021 = int(input("Masukan nilai batas: "))
for i_2021 in range(batas_2021 + 1):
    for j_2021 in range(batas_2021 + 1):
        print(i_2021 + j_2021, end=" ")
    print()  # pindah ke baris berikutnya