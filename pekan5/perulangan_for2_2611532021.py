# program ini menggunakan fungsi input()

ulang_2021 = int(input("Masukkan jumlah perulangan: "))

print("Perulangan ke-0 sampai ke-",ulang_2021-1)
for i in range(ulang_2021):
    print(i, end="")
print()
print("Perulangan ke-1 sampai ke-",ulang_2021)
for i in range (1,ulang_2021 + 1):
    print(i, end=" ")