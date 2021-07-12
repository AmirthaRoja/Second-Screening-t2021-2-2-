enter = "Choose the operation to perform:1.addition,2.subraction,3.multiplication,4.division:"
operator = input("Choose the operation to perform:1.addition,2.subraction,3.multiplication,4.division:")
a = float(input("Enter first operand: "))
b = float(input("Enter second operand: "))

if operator == "addition":
    print(a+b)
elif operator == "subraction":
    print(a-b)
elif operator == "multiplication":
    print(a*b)
elif operator == "addition":
    print(a/b)
else:
    print("Invalid Input")