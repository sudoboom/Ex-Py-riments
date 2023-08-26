import random
import math # Apparently it's not accessed but I don't care lmao
import time

threeblacklist = [333, 444, 555, 666, 777, 888, 999] # Blacklisted numbers in first 3, e.g. (as A) AAA-BBBBBBB

print("\n\n\n\nWelcome to 95keygen-py by Dumprr\n--\nWindows 95 Key Generator made in Python. It's fully open source.")
print("Starting in 1 second...")
time.sleep(1)

key = ''
print("------------")  # ... terminal filler!
print("Generating...") # ... terminal filler!
print("------------")  # ... terminal filler!

time.sleep(0.5)



def mod3():
    m3i = ''
    for x in range(3): # Repeat 3 times to make the first 3 numbers
        m3i += str(random.randint(0, 9)) # Random 1-9
    if int(m3i) in threeblacklist: # if the number is in the blacklist
        print("mod3 error! retrying")
        mod3(m3i)
    else:
        def mod7(m3i): # Sort all numbers into individual variables.
            m7i1 = str(random.randint(0, 9)) 
            m7i2 = str(random.randint(0, 9)) 
            m7i3 = str(random.randint(0, 9)) 
            m7i4 = str(random.randint(0, 9)) 
            m7i5 = str(random.randint(0, 9)) 
            m7i6 = str(random.randint(0, 9)) 
            m7i7 = str(random.randint(0, 9)) 
            m7i = (m7i1+m7i2+m7i3+m7i4+m7i5+m7i6+m7i7) # Adds all strings of variables together as one string.
            intm7i = (int(m7i1)+int(m7i2)+int(m7i3)+int(m7i4)+int(m7i5)+int(m7i6)+int(m7i7)) # Converts all variables to integers to add mathematically.
            if intm7i % 7 != 0: # Basically just saying, if it is not divisible by 7 then do
                print("mod7 error! retrying")
                mod7(m3i)
            else:
               def finish(m3i, m7i, intm7i):
                 keyweight = intm7i / 7 # "Key Weight", saw it used in MobCat's checker, divides it by 7 to get weight.
                 print()
                 print("Done!")
                 print("Key Weight: " + str(keyweight)) # Prints key weight
                 print(m3i + "-" + m7i) # Prints product key
                 print("\n\nPress enter to leave")
               finish(m3i, m7i, intm7i)
        mod7(m3i) # This is down here because it's in the big if-else statement. There wasn't any other way to do this, atleast from my perspective

print()
mod3() # Starts the operation
input() # I only put this here, because on terminal, python will auto close if there is no waiting or math to be done. Really annoying >:(