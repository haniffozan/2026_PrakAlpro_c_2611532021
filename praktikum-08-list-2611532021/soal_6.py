LAST_DIGIT = 1  # change to the last digit of your NIM
daily_limit = 30000 + LAST_DIGIT * 1000 # hence, it equals to 31000
expenses = []
days = 7
total = 0
highest = 0
over_limit = 0
# Write your code below
for i in range(days):
    expenses.append(int(input(f"Day {i + 1}: ")))
    if i == 0:
        highest = expenses[0]
    current = expenses[i]
    total += current
    if current > highest:
        highest = current
    if current > daily_limit:
        over_limit += 1
    
average = total / days
print("Daily limit:", daily_limit)
print("Total:", total)
print(f"Average: {average:.1f}", )
print("Highest:", highest)
print("Days above limit:", over_limit)
