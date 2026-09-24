# program praktikum minggu 2. 9/10/26.
# program ini mengunakan tipe data boolean untuk menentukan status kelulusan mahasiswa.

# deklarasi variabel dengan tipe data boolean
is_lulus_2021 = True
is_cumlaude_2021 = True

# menggunakan boolean
nilai_2021 = 85
batas_lulus_2021 = 75

# menentukan nilai boolean dari kondisi
status_kelulusan_2021 = nilai_2021 >= batas_lulus_2021 # Hasilnya akan True

# mencetak nilai boolean
print("=== Check Kelulusan ===")
print("Nilai:", nilai_2021)
print("Apakah lulus?:", status_kelulusan_2021)
if is_lulus_2021 and is_cumlaude_2021:
    print("Selamat, Anda lulus dengan peringkat cumlaude!")

