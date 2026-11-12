# Name: Muhammad Hanif Fauzan
# NIM: 2611532021
# Question 6

first_name = " muhammad"
last_name = "rafi "
full_name = first_name.strip() + " " + last_name.strip()
print(full_name)
print(full_name.title())


full_name = "  Siti Aisyah  "
nim = "2610511023"
clean = full_name.strip().lower()
space = clean.find(" ")

if space == -1:
    username = clean + nim[-3:]
else:
    username = clean[:space] + nim[-3:]
print(username)

# Build the username: first name in lowercase + last 3 digits of the NIM.
# Do not use split().
