# Buat File dengan nama multi_if1_nim.py
# Buat program untuk kondisional If
# Nama variabel ditambah 4 digit nim terakhir contoh ipk_1234
# Program ini menggunakan fungsi input()

umur_2021 = int(input("Input umur Anda: "))
sim_2021 = input("Apakah Anda Sudah Punya SIM C (y/t): ")[0]

if umur_2021 >= 17 and sim_2021 == 'y': 
    print("Anda sudah dewasa dan boleh bawa motor")

if umur_2021 >= 17 and sim_2021 != 'y':
    print("Anda sudah dewasa tetapi tidak boleh bawa motor")

if umur_2021 < 17 and sim_2021 == 'y':
    print("Anda belum cukup umur punya SIM")

if umur_2021 < 17 and sim_2021 != 'y':
    print("Anda belum cukup umur bawa motor")