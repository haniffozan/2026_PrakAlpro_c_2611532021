menus = ["Nasi Goreng", "Mie Ayam", "Soto"]
number_of_days = 3
sales = []

# Write your code below
# adjusting the sales list
for i in range(3):
    current = []
    for j in range(3):    
        current.append(int(input(f"Day {i + 1}, {menus[j]}: ")))  
    sales.append(current) # TODO

# to find the amount of portions for each of the day and the amount of portion each of the menu
per_day = []
menu_totals = []
for i in range(len(sales)):
    a_day = 0 # temporary variable to store total portion in a day
    menu = 0 # temporary variable to store total portion of each menu
    for j in range(len(sales[0])):
        a_day += sales[i][j]
        menu += sales[j][i]
    per_day.append(a_day)
    menu_totals.append((menus[i], menu))

# output
print("Total per day:")
for i in range(len(per_day)):
    print(f"Day {i + 1}: {per_day[i]}")

print("Total per menu:", menu_totals)

most_total = menu_totals[0][1] # set equal to the integer element of the first touple from the list 
most_menu = menu_totals[0][0] # set equal to the string element of the first touple from the list
for name, total in menu_totals:
    if total > most_total:
        most_total = total
        most_menu = name

print(f"Best seller: {most_menu} ({most_total})")