# KAMI KELAS PRAKTIKUM C TIDAK MENDAPATKAN KETENTUAN YANG BERKAITAN DENGAN "score_recap.py"
# OLEH KARENA ITU KODE INI BANYAK SALAHNYA
PASS_SCORE = 65
counter = 0
total = 0
amount = int(input("How many scores? "))
for number in range(amount):
    score = int(input("Enter the score: "))
    if score < 0 or score > 100:
        print("Invalid score!")
        continue
    total += score
    counter += 1
while score > 0:
    break
    
average = round(total/counter, 2)
print("Total score: ", total)
print("Average score: ", average)
