correct_pin = "1234" # k
MAX_ATTEMPTS = 3 # h
attempt = 1 # b    
pin = input("Enter PIN: ") # e

while pin != correct_pin and attempt < MAX_ATTEMPTS: # c    
    print("Incorrect PIN.") # i
    attempt += 1 # g
    pin = input("Enter PIN: ") # e

if pin == correct_pin: # j
    print("Access granted") # d

else: # f
    print("Account locked") # a

    




 
 