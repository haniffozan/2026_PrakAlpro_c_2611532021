tinggi_2021 = int(input("Masukkan tinggi segitiga: "))

for i_2021 in range(1, tinggi_2021 + 1):
    for j_2021 in range(tinggi_2021 - i_2021):
        print(" ", end="")

    for k_2021 in range(i_2021):
        print("* ", end="")

    print()