# ===== VARIABEL GLOBAL =====
nama_2021 = "..."
kelamin_2021 = '-'
umur_2021 = 0
skor_2021 = 0.0
batas_minimum_2021 = 75.0
lulus_2021 = False
token_2021 = 6767 + 3j
alamat_2021 = """
Perumahan Taman Mangunsarkoro,
Jl. KIS Mangunsarkoro,
Kec. Padang Timur
Kota padang """


# fungsi utama
def main():
    print("=== SISTEM REGISTRASI PRAKTIKAN ALPRO 2026 ===")
    bagian1()
    print("\n=== DATA PRAKTIKAN & HASIL PEMERIKASAAN ===")
    bagian2()
    print("\n=== STATUS KELULUSAN PRAKTIKUM ===")
    bagian3()

# fungsi ini mengambil seluruh data dari user
def bagian1():
    # menggunakan perintah 'global' karena fungsi ini memanipulasi variabel-variabel global
    global nama_2021
    global kelamin_2021
    global umur_2021
    global skor_2021
    nama_2021 = input("Masukkan Nama Mahasiswa     : ")
    kelamin_2021 = input("Masukkan Jenis Kelamin (L/P): ")
    umur_2021 = int(input("Masukkan Umur               : "))
    skor_2021 = float(input("Masukkan Skor Tes Awal      : "))


# fungsi ini memprint seluruh variabel global (kecuali variabel 'lulus_2021') dengan cara tertentu
def bagian2():
    print("Nama Mahasiswa :", nama_2021, "| Tipe: ", type(nama_2021))
    print("Jenis Kelamin  :", kelamin_2021, "| Tipe: ", type(kelamin_2021))
    print("Alamat Domisili:", alamat_2021, "| Tipe: ", type(alamat_2021))
    print("Umur           :", umur_2021, "tahun | Tipe: ", type(umur_2021))
    print("Skor Tes Awal  :", skor_2021, "| Tipe: ", type(skor_2021))
    print("ID Token Sinyal:", token_2021, "| Tipe: ", type(token_2021))


# fungsi ini mengerjakan bagian terakhir dari kode ini yang memerlukan variabel global 'lulus_2021'
# variabel itu sengaja dipisah dari variabel lain karena cara menentukan nilainya yang unik
# dari variabel lain
def bagian3():
    # menggunakan perintah 'global' karena 'lulus_2021' adalah variabel global
    global lulus_2021
    print("Batas Minimum Nilai:",batas_minimum_2021)
    lulus_2021 = skor_2021 >= batas_minimum_2021
    print("Apakah Dinyatakan Lulus?:", lulus_2021, "| Tipe: ", type(lulus_2021)) 

    
# menjalankan seluruh kode
main()