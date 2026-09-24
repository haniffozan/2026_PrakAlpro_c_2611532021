# Buat file dengan nama multi_if2_2611532021.py
# Buat program untuk kondisional If
# Nama variabel ditambah 4 digit nim terakhir contoh ipk_1234
# Program ini menggunakan fungsi input()
# Program Menghitung Diskon belanja

# Input dari user
total_belanja_2021 = float(input("Input Total Belanja (Rp): "))

# Input status member (mengecek apakah user mengetik 'y' atau 'ya')
input_member_2021 = input("Apakah Anda Member? (y/t): ").strip().lower()
is_member_2021 = input_member_2021 in ["y", "ya"]

# Input status kode promo (mengecek apakah user mengetik 'y' atau 'ya')
input_promo_2021 = input("Apakah Kode Promo valid? (y/t): ").strip().lower()
kode_promo_valid_2021 = input_promo_2021 in ["y", "ya"]

total_diskon_persen_2021 = 0

# MULTI-IF terpisah Setiap kondisi diperiksa secara independen
# Diskon bisa ditumpuk jika memenuhi beberapa syarat sekaligus

if total_belanja_2021 > 1000000:
    total_diskon_persen_2021 += 10  # Diskon belanja besar

if is_member_2021:
    total_diskon_persen_2021 += 5  # Diskon member

if kode_promo_valid_2021:
    total_diskon_persen_2021 += 15  # Diskon voucher

# Menghitung nominal diskon dan total bayar
nominal_diskon_2021 = total_belanja_2021 * (total_diskon_persen_2021 / 100) 
total_bayar_2021 = total_belanja_2021 - nominal_diskon_2021

# Output hasil
print("\n--- Rincian Pembayaran ---")
print(f"Total Diskon : {total_diskon_persen_2021}% (Rp {nominal_diskon_2021:,.0f})")
print(f"Total Bayar   : Rp {total_bayar_2021:,.0f}")

print(f"Total Diskon yang anda dapatkan : {total_diskon_persen_2021}%")
# Output: Total diskon yang anda dapatkan : 30% jika belanja > 1 juta, member, dan kode promo valid