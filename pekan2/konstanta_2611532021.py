# program praktikum minggu 2. 9/10/26.
# program ini menggunakan konstanta untuk menghitung luas lingkaran.

from typing import Final
PI: Final = 3.14
print("pi: %f" % (PI))
jari_2021 = float(input("Masukkan nilai jari-jari: "))
luas_2021 = PI * jari_2021 * jari_2021
print("Luas lingkaran dengan jari-jari %.2f adalah: %.2f" % (jari_2021, luas_2021))
