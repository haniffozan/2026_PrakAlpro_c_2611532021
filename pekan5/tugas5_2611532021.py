# program ini mencetak gambar jam pasir
# program ini lumayan ribet sehingga diperlukan beberapa fungsi custom

def main():
    # judul dan mengambil input user
    print("=== PROGRAM JAM PASIR KRISTAL PALINDROMIK (PEKAN 5) ===")
    n_2021 = int(input("Masukkan skala jam pasir: "))
    
    bingkai(n_2021) # lihat deklarasinya
    fase1_2021(n_2021) # lihat deklarasinya
    fase2_2021(n_2021) # lihat deklarasinya
    fase3_2021(n_2021) # lihat deklarasinya
    bingkai(n_2021) # lihat deklarasinya


# membuat bingkai jam pasir
def bingkai(n_2021):
    print("#", end="")
    for i_2021 in range (4 * n_2021 + 5):
        print("=", end="")
    print("#")


# fase 1 yang bagian jam pasir atas sebelum singularitas
def fase1_2021(n_2021):
    n_dinamis_2021 = n_2021 # variabel ini berperan sebagai acuan program untuk mencetak angka-angka

    
    # cetak seluruh baris untk bagian jam pertama alias untuk fase 1
    for i_2021 in range(n_2021):

        # garis tegak pembatas kiri dan 1 spasi padding
        print("|", end=" ")

        # spasi penyeimbang kiri sebanyak 2 * baris
        for j_2021 in range(2 * (i_2021)):
            print(" ", end="")

        # print angka dari n sampai 1    
        for j_2021 in range(n_dinamis_2021, 0, -1):
            print(f"{j_2021} ", end="")

        # poros kristal tengah karakter "<*>"
        print("<*>", end=" ")

        # print angka dari 1 sampai n
        for j_2021 in range(1, n_dinamis_2021 + 1):
            print(f"{j_2021} ", end="")

        # spasi penyeimbang kanan sebanyak 2 * baris
        for j_2021 in range(2 * (i_2021)):
            print(" ", end="")

        # garis tegak pembatas kanan
        print("|")    
        
        n_dinamis_2021 -= 1 # variabel ini berkurang 1 tiap baris
        

# fase 2 / singularitas yang mencetak "<*>" tunggal
def fase2_2021(n_2021):

    # garis tegak pembatas kiri dan 1 spasi padding
    print("|", end=" ")

    # spasi-spasi penyeimbang kiri sebanyak N
    for i_2021 in range(n_2021 * 2):
        print(" ", end="")

    # kristal tunggal
    print("<*>", end="")

    # spasi-spasi penyeimbang kanan sebanyak N
    for i_2021 in range(n_2021 * 2):
        print(" ", end="")

    # garis tegak pembatas kanan dan 1 spasi padding
    print(" ", end="|")
    print() # masuk baris baru


# fase 3 yang mencetak bagian setengah bawah jam pasir
def fase3_2021(n_2021):
    n_dinamis_2021 = 1 # variabel ini berperan sebagai acuan program untuk mencetak angka-angka
    
    # cetak seluruh baris untk bagian jam ketiga alias untuk fase 3
    for i_2021 in range(1, n_2021 + 1):

        # garis tegak pembatas kiri dan 1 spasi padding
        print("|", end=" ")

        # spasi penyeimbang kiri sebanyak 2 * (N - baris)
        for j_2021 in range(2 * (n_2021 - i_2021)):
            print(" ", end="")

        # print angka dari n sampai 1    
        for j_2021 in range(n_dinamis_2021, 0, -1):
            print(f"{j_2021} ", end="")

        # poros kristal tengah karakter "<*>"
        print("<*>", end=" ")

        # print angka dari 1 sampai n
        for j_2021 in range(1, n_dinamis_2021 + 1):
            print(f"{j_2021} ", end="")

        # spasi penyeimbang kanan sebanyak 2 * (N - baris)
        for j_2021 in range(2 * (n_2021 - i_2021)):
            print(" ", end="")

        # garis tegak pembatas kanan
        print("|")    
        
        n_dinamis_2021 += 1 # variabel ini berkurang 1 tiap baris

if __name__ == "__main__":
    main()