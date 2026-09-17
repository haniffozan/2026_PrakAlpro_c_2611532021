# Buat file dengan nama bitwise_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()

print("\n=====================================")
print("3. OPERATOR BITWISE")
print("=====================================")

angka1_2611532021 = int(input("Masukkan angka bitwise-1: "))
angka2_2611532021 = int(input("Masukkan angka bitwise-2: "))

print("\nAngka dalam bentuk desimal dan biner")
print("angka1 =", angka1_2611532021, "| biner =", bin(angka1_2611532021))
print("angka2 =", angka2_2611532021, "| biner =", bin(angka2_2611532021))

# Bitwise AND
hasil1_2611532021 = angka1_2611532021 & angka2_2611532021
print("\nBitwise AND (&)")
print(angka1_2611532021, "&", angka2_2611532021, "=", hasil1_2611532021)
print("Biner hasil =", bin(hasil1_2611532021))
print("Biner hasil (8 bit) =", format(hasil1_2611532021, "08b"))

# Bitwise OR
hasil1_2611532021 = angka1_2611532021 | angka2_2611532021
print("\nBitwise OR (|)")
print(angka1_2611532021, "|", angka2_2611532021, "=", hasil1_2611532021)
print("Biner hasil =", bin(hasil1_2611532021))
print("Biner hasil (8 bit) =", format(hasil1_2611532021, "08b"))

# Bitwise XOR
hasil1_2611532021 = angka1_2611532021 ^ angka2_2611532021
print("\nBitwise XOR (^)")
print(angka1_2611532021, "^", angka2_2611532021, "=", hasil1_2611532021)
print("Biner hasil =", bin(hasil1_2611532021))
print("Biner hasil (8 bit) =", format(hasil1_2611532021, "08b"))

# Bitwise NOT
hasil1_2611532021 = ~angka1_2611532021
print("\nBitwise NOT (-)")
print("~", angka1_2611532021, "=", hasil1_2611532021)
print("Biner hasil =", bin(hasil1_2611532021))
print("Biner hasil (8 bit) =", format(hasil1_2611532021, "08b"))

# Bitwise geser kiri
jumlah_geser_2611532021 = int(input("\nMasukkan jumlah pergeseran bit: "))

hasil1_2611532021 = angka1_2611532021 << jumlah_geser_2611532021
print("\nBitwise geser kiri (<<)")
print(angka1_2611532021, "<<", jumlah_geser_2611532021, "=", hasil1_2611532021)
print("Biner hasil =", bin(hasil1_2611532021))
print("Biner hasil (8 bit) =", format(hasil1_2611532021, "08b"))

# Bitwise geser kanan
hasil1_2611532021 = angka1_2611532021 >> jumlah_geser_2611532021
print("\nBitwise geser kanan (>>)")
print(angka1_2611532021, ">>", jumlah_geser_2611532021, "=", hasil1_2611532021)
print("Biner hasil =", bin(hasil1_2611532021))
print("Biner hasil (8 bit) =", format(hasil1_2611532021, "08b"))