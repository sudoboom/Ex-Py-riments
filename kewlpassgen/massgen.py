import random
import time

# IMPORTANT!
# CHANGE THESE VALUES TO ANY VALUES YOU WANT!
# THIS WILL IMPACT HOW THE PROGRAM RUNS FOR YOU!

characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()" # List of random characters to form password with.
length = 16 # Change the number "16" to desired length.
wait = 0.05 # Change the "0.05" to the amount of time it should wait until generating another password (in seconds). e.g. 0.1 would be 1/10 of a second.

print("\n\n\n\nWelcome to KEWLPASSGEN by Dumprr\n--\nPassword Generator made in Python. It's fully open source.\nIf you want a different result, you can change the \"length\" and \"characters\" variable.")
print("Starting in 1 second...")
time.sleep(1)

pw = ''
print("------------")
print("Generating...")
print("------------")
print("\nPasswords:\n")

while 2 > 1:
    pw = ''
    for x in range(length):
        pw += random.choice(characters)


    print(pw)
    time.sleep(wait)