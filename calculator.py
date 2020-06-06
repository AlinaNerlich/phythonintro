number1 = int(input("Enter a number: "))
operation = input("Enter an operation +,-,/ or *: ")
number2 = int(input("Enter a second number: "))

if operation == "+":
    print(number1 + number2)
elif operation == "*":
    print(number1 * number2)
elif operation == "/":
    print(number1 / number2)
elif operation == "-":
    print(number1 - number2)
else:
    print("Your operation is invalid")