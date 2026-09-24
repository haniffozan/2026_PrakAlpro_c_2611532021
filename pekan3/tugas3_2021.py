# Tugas 3
# Sistem Simulasi Transaksi dan Validasi Akses Toko


print("=== SISTEM TRANSAKSI TOKO ===")

# ==============================
# INPUT DATA
# ==============================

nama_2021 = input("Masukkan Nama Pelanggan : ")

status_2021 = input(
    "Masukkan Status Pelanggan (member/nonmember) : "
).lower()

total_belanja_2021 = int(
    input("Masukkan Total Belanja : ")
)

jumlah_barang_2021 = int(
    input("Masukkan Jumlah Barang : ")
)

kode_promo_2021 = input(
    "Masukkan Kode Promo : "
).upper()


# ==============================
# DATA TRANSAKSI
# ==============================

print("\n=== DATA TRANSAKSI ===")

print("Nama Pelanggan   :", nama_2021)
print("Status Pelanggan :", status_2021)
print("Total Belanja    : Rp", total_belanja_2021)
print("Jumlah Barang    :", jumlah_barang_2021)
print("Kode Promo       :", kode_promo_2021)


# ==============================
# OPERATOR PERBANDINGAN
# ==============================

min_belanja_2021 = total_belanja_2021 >= 200000

min_barang_2021 = jumlah_barang_2021 >= 3

status_member_2021 = status_2021 == "member"


# ==============================
# OPERATOR KEANGGOTAAN
# ==============================

daftar_promo_2021 = [
    "HEMAT10",
    "HEMAT20",
    "GRATISONGKIR"
]

promo_tersedia_2021 = kode_promo_2021 in daftar_promo_2021


# ==============================
# OPERATOR LOGIKA
# ==============================

diskon_member_2021 = (
    status_member_2021
    and min_belanja_2021
)

mendapatkan_promo_2021 = (
    min_barang_2021
    and promo_tersedia_2021
)


print("\n=== HASIL VALIDASI ===")

print(
    "Belanja >= Rp200000       :",
    min_belanja_2021
)

print(
    "Jumlah Barang >= 3        :",
    min_barang_2021
)

print(
    "Status Member             :",
    status_member_2021
)

print(
    "Kode Promo Tersedia       :",
    promo_tersedia_2021
)

print(
    "Mendapatkan Diskon        :",
    diskon_member_2021
)

print(
    "Mendapatkan Promo         :",
    mendapatkan_promo_2021
)


# ==============================
# OPERATOR ARITMATIKA
# ==============================

if diskon_member_2021:
    diskon_2021 = total_belanja_2021 * 10 / 100
else:
    diskon_2021 = 0

total_pembayaran_2021 = (
    total_belanja_2021 - diskon_2021
)

harga_rata_rata_2021 = (
    total_belanja_2021 / jumlah_barang_2021
)

sisa_pembagian_2021 = (
    total_belanja_2021 % jumlah_barang_2021
)


print("\n=== HASIL PERHITUNGAN ===")

print(
    "Diskon                 : Rp",
    diskon_2021
)

print(
    "Total Pembayaran       : Rp",
    total_pembayaran_2021
)

print(
    "Rata-rata Harga Barang : Rp",
    harga_rata_rata_2021
)

print(
    "Sisa Pembagian         :",
    sisa_pembagian_2021
)


# ==============================
# HAK AKSES
# ==============================

member_access_2021 = (
    status_member_2021
    and min_belanja_2021
)

promo_access_2021 = (
    promo_tersedia_2021
    or mendapatkan_promo_2021
)

free_shipping_access_2021 = (
    kode_promo_2021 == "GRATISONGKIR"
    and not status_member_2021
)


print("\n=== HAK AKSES PELANGGAN ===")

print(
    "Member Access        :",
    member_access_2021
)

print(
    "Promo Access         :",
    promo_access_2021
)

print(
    "Free Shipping Access :",
    free_shipping_access_2021
)


# ==============================
# OPERATOR PENUGASAN
# ==============================

poin_2021 = 0

poin_2021 += 10

print("\n=== OPERATOR PENUGASAN ===")

print(
    "Poin setelah += 10 :",
    poin_2021
)

poin_2021 -= 2

print(
    "Poin setelah -= 2  :",
    poin_2021
)

poin_2021 *= 2

print(
    "Poin setelah *= 2  :",
    poin_2021
)

poin_2021 /= 2

print(
    "Poin setelah /= 2  :",
    poin_2021
)


# ==============================
# OPERATOR IDENTITAS
# ==============================

objek_a_2021 = ["HEMAT10"]

objek_b_2021 = ["HEMAT10"]

print("\n=== OPERATOR IDENTITAS ===")

print(
    "objek_a == objek_b     :",
    objek_a_2021 == objek_b_2021
)

print(
    "objek_a is objek_b     :",
    objek_a_2021 is objek_b_2021
)

print(
    "objek_a is not objek_b :",
    objek_a_2021 is not objek_b_2021
)


# ==============================
# OPERATOR BITWISE
# ==============================

print("\n=== OPERASI BITWISE ===")

# Nilai bit
bit_member_2021 = 0b0001
bit_belanja_2021 = 0b0010
bit_barang_2021 = 0b0100
bit_promo_2021 = 0b1000


# OR (|)
kode_status_2021 = 0

if status_member_2021:
    kode_status_2021 |= bit_member_2021

if min_belanja_2021:
    kode_status_2021 |= bit_belanja_2021

if min_barang_2021:
    kode_status_2021 |= bit_barang_2021

if promo_tersedia_2021:
    kode_status_2021 |= bit_promo_2021


print("\n=== KODE STATUS TRANSAKSI ===")

print("0001 | 0010 | 0100 | 1000")

print(
    "Kode Biner   :",
    format(kode_status_2021, "04b")
)

print(
    "Kode Desimal :",
    kode_status_2021
)


# AND (&)
cek_member_2021 = (
    kode_status_2021 & bit_member_2021
)

cek_promo_2021 = (
    kode_status_2021 & bit_promo_2021
)


print("\n=== PEMERIKSAAN STATUS ===")

print("\nCek Member")

print(
    format(kode_status_2021, "04b"),
    "&",
    format(bit_member_2021, "04b")
)

print(
    "Hasil Biner   :",
    format(cek_member_2021, "04b")
)

print(
    "Hasil Desimal :",
    cek_member_2021
)


print("\nCek Promo")

print(
    format(kode_status_2021, "04b"),
    "&",
    format(bit_promo_2021, "04b")
)

print(
    "Hasil Biner   :",
    format(cek_promo_2021, "04b")
)

print(
    "Hasil Desimal :",
    cek_promo_2021
)


# XOR (^)

kode_referensi_2021 = 0b1011

hasil_xor_2021 = (
    kode_status_2021 ^ kode_referensi_2021
)


print("\n=== PERBANDINGAN STATUS ===")

print(
    "Kode Transaksi :",
    format(kode_status_2021, "04b")
)

print(
    "Kode Referensi :",
    format(kode_referensi_2021, "04b")
)

print(
    format(kode_status_2021, "04b"),
    "^",
    format(kode_referensi_2021, "04b")
)

print(
    "Hasil Biner   :",
    format(hasil_xor_2021, "04b")
)

print(
    "Hasil Desimal :",
    hasil_xor_2021
)


# SHIFT

hasil_shift_2021 = kode_status_2021 << 1

print("\n=== SHIFT ===")

print(
    format(kode_status_2021, "04b"),
    "<< 1"
)

print(
    "Hasil Biner   :",
    format(hasil_shift_2021, "b")
)

print(
    "Hasil Desimal :",
    hasil_shift_2021
)


# ==============================
# HASIL OPERATOR
# ==============================

print("\n=== HASIL OPERATOR ===")

print("Operator Aritmatika   : digunakan")
print("Operator Perbandingan : digunakan")
print("Operator Logika       : digunakan")
print("Operator Penugasan    : digunakan")
print("Operator Keanggotaan  : digunakan")
print("Operator Identitas    : digunakan")
print("Operator Bitwise      : digunakan")


print("\n=== SELESAI ===")