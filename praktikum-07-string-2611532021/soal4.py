# Name: Muhammad Hanif Fauzan
# NIM: 2611532021
# Question 4

phone = "082611532021"
masked = phone[:4] + "*" * (len(phone) - 7) + phone[-3:]
print(masked)
