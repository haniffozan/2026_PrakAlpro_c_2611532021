# nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# program ini menggunakan fungsi input()
# nilai yang dimasukkan akan dikonversi menjadi tipe data integer
# program operator assignment dalam python

angka1_2611532021 = int(input("Input angka-1: "))
angka2_2611532021 = int(input("Input angka-2: "))

print("\nNilai awal angka1 = ", angka1_2611532021)
print("Nilai angka2 = ", angka2_2611532021)

# assignment biasa
hasil_2611532021 = angka1_2611532021
print("\nAssignment biasa (=)")
print("Hasil = ", hasil_2611532021)

# assignment penambahan
hasil_2611532021 = angka1_2611532021
hasil_2611532021 += angka2_2611532021
print("\nAssignment penambahan (+=)")
print("Hasil = ", hasil_2611532021)

# assignment pengurangan
hasil_2611532021 = angka1_2611532021
hasil_2611532021 -= angka2_2611532021
print("\nAssignment pengurangan (-=)")
print("Hasil = ", hasil_2611532021)

# assignment perkalian
hasil_2611532021 = angka1_2611532021
hasil_2611532021 *= angka2_2611532021
print("\nAssignment perkalian (*=)")
print("Hasil = ", hasil_2611532021)

# assignment pembagian, pembagian bulat, dan sisa bagi
if angka2_2611532021 != 0:
    hasil_2611532021 = angka1_2611532021
    hasil_2611532021 /= angka2_2611532021
    print("\nAssignment pembagian (/=)")
    print("Hasil = ", hasil_2611532021)

    # operator tambahan
    hasil_2611532021 = angka1_2611532021
    hasil_2611532021 //= angka2_2611532021
    print("\nAssignment pembagian bulat (//=)")
    print("Hasil = ", hasil_2611532021)

    hasil_2611532021 = angka1_2611532021
    hasil_2611532021 %= angka2_2611532021
    print("\nAssignment sisa bagi (%=)")
    print("Hasil = ", hasil_2611532021)
else:
    print("\nPembagian tidak dapat dilakukan.")
    print("Angka kedua tidak boleh bernilai 0.")

# operator tambahan: assignment perpangkatan
hasil_2611532021 = angka1_2611532021
hasil_2611532021 **= angka2_2611532021
print("\nAssignment perpangkatan (**=)")
print("Hasil = ", hasil_2611532021)

