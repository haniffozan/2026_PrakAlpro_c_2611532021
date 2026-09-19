# tugas 3
# variabel global
# program ini menggunakan dictionary untuk menggabungkan variabel-variabel yang banyak

def main():
    data_2021 = {}
    mulai(data_2021)
    data_transaksi(data_2021)
    hasil_validasi(data_2021)
    hasil_perhitungan(data_2021)
    hak_akses(data_2021)
    operasi_bitwise(data_2021)
    pemeriksaan_status(data_2021)
    cek_promo(data_2021)
    perbandingan_status(data_2021)
    shift(data_2021)
    print("=== SELESAI ===")


def mulai(data):
    print("=== SISTEM TRANSAKSI TOKO ===")
    data["nama"] = input("Masukkan Nama pelanggan:")

main()