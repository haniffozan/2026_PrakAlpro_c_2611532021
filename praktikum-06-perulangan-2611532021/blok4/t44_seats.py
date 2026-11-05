# saya tidak paham apa maksud perintah "baca blocked_seat" yang ada di halaman 7 nomor 4.4 
# dari modul. Apakah itu maksudnya sebuah contoh kode

break_seat = int(input("Break seat: "))

for row in range(1, 4):
    print("Row", row, end=": ")
    for seat in range(1, 6):
        if seat == break_seat:
            break
        print(seat, end=" ")
    print()