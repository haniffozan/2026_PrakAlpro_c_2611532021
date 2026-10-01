# buat file dengan nama nested_for1_NIM.py
# buat program untuk perulangan for dalam python
# nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# program ini menggunakan fungsi input()

batas_2021 = int(input("Masukkan nilai batas : "))
for line_2021 in range(1, batas_2021 + 1):
    for j_2021 in range(1,(-1 * line_2021 + batas_2021) + 1):
        print(".",end="")
    print(line_2021)