ulang_2021= int(input("Masukkan jumlah perulangan: "))

jumlah_2021 = 0
for i in range(1, ulang_2021 + 1):
    print(i,end=" ")
    jumlah_2021 = jumlah_2021 + i

    if i < ulang_2021:
        print(" + ", end="")
    else:
        print(" = ", jumlah_2021, end="")
print()
print("jumlah =",jumlah_2021)