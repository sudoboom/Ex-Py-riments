import math
print("Welcome to \n FORMULATOR!\n")
print("Type one of the following numbers:\n1. Pythagorean Theorum Solver\n2. Reverse Pythagorean Theorum\n3. Area of a Circle\n4. Cirumference of a Circle (USING RADIUS)\n5. Circumference of a Circle (USING DIAMETER)")
Option = input("Type:")
OptionInt = int(Option)

if OptionInt <= 5:
    if OptionInt == 1:
        Var1 = int(input("Value of A?: "))
        Var2 = int(input("Value of B?: "))
        FinalAnswer = str(Var1**2 + Var2**2)
        FinalAnswerWithSqrt = str(math.sqrt(int(FinalAnswer)))
        print("\nFinal Answer:\nC: "+FinalAnswer+"\nC (Square Rooted): "+FinalAnswerWithSqrt)
        input("type any to leave")
        exit
    if OptionInt == 2:
        Var1 = int(input("Value of C? (Hypotenuse):"))
        Var2 = int(input("Value of B? (Any Side):"))
        FinalAnswer = str(Var1**2 - Var2**2)
        FinalAnswerWithSqrt = str(math.sqrt(int(FinalAnswer)))
        print("\nFinal Answer:\nA: "+FinalAnswer+"\nA (Square Rooted): "+FinalAnswerWithSqrt)
        input("type any to leave")
        exit
else:
   exit
