# Name: Muhammad Hanif Fauzan
# NIM: 2611532021
# Question 7

name = "muhammad hanif fauzan"
nim = "2611532021"
clean = name.strip().lower()
space = clean.find(" ")

if space == -1:
    username = clean + nim[-3:]
else:
    username = clean[:space] + nim[-3:]

print("=" * 30)
print(f"{'STUDENT CARD': ^30}")
print("=" * 30)
print(f"{"Name": <10}" + f": {name.title()}")
print(f"{"NIM": <10}" + f": {nim}")
print(f"{"Username": <10}" + f": {username}")
print(f"{"Intake": <10}" + f": 20{nim[:2]}")
print("=" * 30)