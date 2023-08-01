print("Coded by Dumprr")
print("\n")
print("Welcome to the spammer.")
print("You get 2 lines to spam")


print(  )
print(  )
print("Enter Spam Message 1: (Type STOP to abort)")
Line1 = input()
if Line1 == "STOP":
  exit("Process Aborted")
print("What is the bottom line you would like to spam?")
Line2 = input()

if Line2 == "STOP":
  exit("Process Aborted")

print("Your spam will look like this: ""\n"+Line1+"\n"+Line2)
print("Is this ok? (y/n)")
YesOrNo = input()

if YesOrNo != "y":
  exit("Process Aborted")

while True:
  print(Line1)
  print(Line2)

