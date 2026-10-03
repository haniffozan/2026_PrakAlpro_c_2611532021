# Buat file dengan nama nested_for4_NIM.py
# Buat program untuk perulangan for dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

tinggi_2021 = int(input("Masukkan tinggi pola (bilangan genap, misal 10): "))

if tinggi_2021 % 2 != 0:
    print("Tinggi harus bilangan genap!")
else:
    a_2021 = tinggi_2021
    c_2021 = a_2021
    lebar_2021 = (2 * tinggi_2021) - 2

    for i_2021 in range(1, tinggi_2021 + 1):
        b_2021 = c_2021 + 1

        for j_2021 in range(1, lebar_2021 + 1):

            # Baris atas dan bawah
            if i_2021 == 1 or i_2021 == tinggi_2021:
                if j_2021 == 1 or j_2021 == lebar_2021:
                    print("#", end="")
                else:
                    print("=", end="")

            # Baris isi
            else:
                if j_2021 == 1 or j_2021 == lebar_2021:
                    print("|", end="")
                else:
                    if j_2021 == c_2021:
                        print("<", end="")
                    elif j_2021 == b_2021:
                        print(">", end="")
                    elif j_2021 == (lebar_2021 - c_2021):
                        print("<", end="")
                    elif j_2021 == (lebar_2021 - c_2021 + 1):
                        print(">", end="")
                    elif j_2021 > b_2021 and j_2021 < (lebar_2021 - c_2021):
                        print(".", end="")
                    else:
                        print(" ", end="")

        print()

        # Logika asli java
        a_2021 -= 2

        if a_2021 <= 0:
            c_2021 = (-a_2021 + 2)
        else:
            c_2021 = a_2021