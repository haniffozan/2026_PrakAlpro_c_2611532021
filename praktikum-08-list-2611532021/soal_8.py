number_of_rows = 4
seats_per_row = 5

# Write your code below
# seats list adjustment
seats = [["."] * seats_per_row]
for i in range(number_of_rows - 1):
    seats.append(["."] * seats_per_row)

# non list variables
stop = 1
seats_taken = 0

# run the folowing as long as the user hasn't type 0
while True:

    # print the seats
    for i in range(len(seats)):
        print(f"Row {i + 1}:", end=" ")
        for j in range(len(seats[0])):
            print(seats[i][j], end=" ")
        print()
    stop = int(input("Row (0 to stop): "))
    if stop == 0: # stops the program when the user enters "0"
            break
    row = stop - 1
    seat = (int(input("Seat: ")) - 1)

    # decide what would the program must print and modify the seats list at a certain condition
    if row < 0 or number_of_rows <= row or seat < 0 or seats_per_row <= seat:
        print("Invalid seat.")
    elif seats[row][seat] == "X":
        print("Seat already taken.")
    else:
        seats[row][seat] = "X"
        seats_taken += 1
        print("Seat booked.")


# print the total seats taken in the end
print("Seats taken:", seats_taken)
