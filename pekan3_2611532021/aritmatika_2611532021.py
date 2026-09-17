# buat program untuk operator logika dalam python
# nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# program ini menggunakan fungsi input()
# nilai yang dimasukkan akan dikonversi menjadi tipe data integer

angka1_2021 = int(input("Input angka-1: : "))
angka2_2021 = int(input("Input angka-2: : "))

# penjumlahan
hasil_2021 = angka1_2021 + angka2_2021
print("\nOperator penjumlahan")
print("Hasil = ", hasil_2021)

# pengurangan
hasil_2021 = angka1_2021 - angka2_2021
print("\nOperator pengurangan")
print("Hasil = ", hasil_2021)

# perkalian
hasil_2021 = angka1_2021 * angka2_2021
print("\nOperator perkalian")
print("Hasil = ", hasil_2021) 

# pembagian, pembagian bulat, dan sisa bagi
if angka2_2021 != 0:
    hasil_2021 = angka1_2021 / angka2_2021
    print("\nOperator pembagian")
    print("Hasil = ", hasil_2021)

    hasil_2021 = angka1_2021 // angka2_2021
    print("\nOperator pembagian bulat")
    print("Hasil = ", hasil_2021)

    hasil_2021 = angka1_2021 % angka2_2021
    print("\nOperator sisa bagi")
    print("Hasil = ", hasil_2021)
else:
    print("Angka kedua tidak boleh bernilai 0.")

# pangkat
hasil_2021 = angka1_2021 ** angka2_2021
print("\nOperator pangkat")
print("Hasil = ", hasil_2021)