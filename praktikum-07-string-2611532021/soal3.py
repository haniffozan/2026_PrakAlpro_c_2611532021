# Name: Muhammad Hanif Fauzan
# NIM: 2611532021
# Question 3

# text = "Informatika"
# print(text[10])
# print(text.upper())
# print(text[0:11])

text = "Muhammad Hanif Fauzan"
count = 0
for char in text.lower():
    if char in "aiueo":
        count += 1
print("Vowels:", count)
