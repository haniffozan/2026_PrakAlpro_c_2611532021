# nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# program ini menggunakan fungsi input()
# program operator logika dalam python

# masukkan nilai boolean
# input tidak pekat terhadap huruf besar dan kecil
a1_2021 = input("Input nilai boolean-1 (True/False): ").strip().lower() == "true"
a2_2021 = input("Input nilai boolean-2 (True/False): ").strip().lower() == "true"

print("\nA1 = ", a1_2021)
print("A2 = ", a2_2021)

# konjungsi: bernilai true jika keduanya true
hasil_2611532021 = a1_2021 and a2_2021
print("\nKonjungsi (AND)")
print("A1 and A2 = ", hasil_2611532021)

# disjungsi: bernilai True jika salah satunya True
hasil_2611532021 = a1_2021 or a2_2021
print("\nDisjungsi (OR)")
print("A1 or A2 = ", hasil_2611532021)

# negasi A1: membalik nilai A1
hasil_2611532021 = not a1_2021
print("\nNegasi A1 (NOT)")
print("not A1 = ", hasil_2611532021)

# negasi a2_2021: membalik nilai a2_2021
hasil_2611532021 = not a2_2021
print("\nNegasi A2 (NOT)")
print("not A2 = ", hasil_2611532021)

# XOR: bernilai True jika kedua nilai berbeda
hasil_2611532021 = a1_2021 != a2_2021
print("\nXOR")
print("A1 XOR A2 = ", hasil_2611532021)