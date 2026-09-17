# nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# program ini menggunakan fungsi input()
# program operator logika dalam python

# masukkan nilai boolean
# input tidak pekat terhadap huruf besar dan kecil
a1 = input("Input nilai boolean-1 (True/False): ").strip().lower() == "true"
a2 = input("Input nilai boolean-2 (True/False): ").strip().lower() == "true"

print("\nA1 = ", a1)
print("A2 = ", a2)

# konjungsi: bernilai true jika keduanya true
hasil_2611532021 = a1 and a2
print("\nKonjungsi (AND)")
print("A1 and A2 = ", hasil_2611532021)

# disjungsi: bernilai True jika salah satunya True
hasil_2611532021 = a1 or a2
print("\nDisjungsi (OR)")
print("A1 or A2 = ", hasil_2611532021)

# negasi A1: membalik nilai A1
hasil_2611532021 = not a1
print("\nNegasi A1 (NOT)")
print("not A1 = ", hasil_2611532021)

# negasi A2: membalik nilai A2
hasil_2611532021 = not a2
print("\nNegasi A2 (NOT)")
print("not A2 = ", hasil_2611532021)

# XOR: bernilai True jika kedua nilai berbeda
hasil_2611532021 = a1 != a2
print("\nXOR")
print("A1 XOR A2 = ", hasil_2611532021)