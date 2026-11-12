# Name: Muhammad Hanif Fauzan
# NIM: 2611532021
# Bonus question  

sentence = input("Enter a sentence: ").lower()
if sentence == sentence[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")