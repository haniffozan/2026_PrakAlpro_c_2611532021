PASS_SCORE = 65
sorry = 0
total = 0
for number in range(4):
    score = int(input("Enter the score: "))
    if score < 0:
        print("Invalid score!")
    if score < 10:
        score = 0
        continue
    total += score
    sorry += 1
while sorry > 0:
    break
average = round(total/sorry, 2)
print("Total score: ", total)
print("Average score: ", average)
