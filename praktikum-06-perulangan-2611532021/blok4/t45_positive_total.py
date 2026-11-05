number = int(input("Enter a number: "))
total = 0
while number >= 0:
    if number == 0:
        number = int(input("Enter a number: "))
        continue
    if number < 0:
        break
    total += number
    print("Positive number:", number)
    number = int(input("Enter a number: "))

print("Total:", total)