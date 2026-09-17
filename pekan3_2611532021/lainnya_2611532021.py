# nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# program ini menggunakan fungsi input()
# program operator keanggotaan dan identitas

print("========================================")
print("1. OPERATOR KEANGGOTAAN")
print("========================================")

# input beberapa data yang dipisahkan dengan koma
input_data_2611532021 = input("Masukkan beberapa angka, pisahkan dengan koma: ")

# mengibah nilai input menjadi list integer
data_2611532021 = [int(angka.strip()) for angka in input_data_2611532021.split(",")]

nilai_dicari_2611532021 = int(input("Masukkan nilai yang ingin dicari: "))

# operator in
hasil_2611532021 = nilai_dicari_2611532021 in data_2611532021
print("\nOperator keanggotaan IN")
print(nilai_dicari_2611532021, "in", data_2611532021, "=", hasil_2611532021)

# operator not in
hasil_2611532021 = nilai_dicari_2611532021 not in data_2611532021
print("\nOperator keanggotaan NOT IN")
print(nilai_dicari_2611532021, "not in", data_2611532021, "=", hasil_2611532021)

print("\n=========================================")
print("2. OPERATOR IDENTITAS")
print("=========================================")
# TODO: pahami baris-baris berikut ini
# objek1 menggunakan list dari input pengguna
objek1_2611532021 = data_2611532021

# objek2 merujuk pada objek yang sama dengan objek1
objek2_2611532021 = objek1_2611532021

# objek3 memiliki isi sama, tetapi merupakan objek yang baru
objek3_2611532021 = data_2611532021.copy()

print("Objek1 = ", objek1_2611532021)
print("Objek2 = ", objek2_2611532021)
print("Objek3 = ", objek3_2611532021)

# operator is
hasil_2611532021 = objek1_2611532021 is objek2_2611532021
print("\nOperator identitas IS")
print("Objek1 is Objek2 =", hasil_2611532021)

# operator is not
hasil_2611532021 = objek1_2611532021 is not objek3_2611532021
print("\nOperator identitas IS NOT")
print("Objek1 is not Objek3 =", hasil_2611532021)

# membandingkan identitas dan nilai
print("\nPerbandingan identitas dan nilai")
print("Objek1 is Objek3 =", objek1_2611532021 is objek3_2611532021)
print("Objek1 == Objek3 =", objek1_2611532021 == objek3_2611532021)