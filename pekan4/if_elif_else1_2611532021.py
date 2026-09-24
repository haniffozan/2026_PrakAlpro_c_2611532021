# Buat file dengan nama if_elif_else1_2611532021.py
# Buat program untuk kondisional If
# Nama variabel ditambah 4 digit nim terakhir contoh ipk_1234
# Program ini menggunakan fungsi input()

umur_2021 = int(input("Input umur Anda: "))
sim_2021 = input("Apakah Anda Sudah Punya Sim C: ")[0]

if umur_2021 >= 17 and sim_2021 == 'y': 
    print("Anda sudah dewasa dan boleh bawa motor")
elif umur_2021 >= 17 and sim_2021 != 'y':
    print("Anda sudah dewasa tetapi tidak boleh bawa motor")
elif umur_2021 < 17 and sim_2021 == 'y':
    print("Anda belum cukup umur punya SIM")
else:
    print("Anda belum cukup umur dan tidak boleh bawa motor")
print("Program Selesai")