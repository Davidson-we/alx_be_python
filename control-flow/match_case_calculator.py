#Ask the user to enter two numbers
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

#Ask the user to enter an operator
operation = input("Choose the operation (+, -, *, /):")

#A helper function to clean numbers like 50.0 to 50
def clean_number(n):
    if n == int(n):
        return int(n)
    return n

#Use match case to perform the operation
match operation:
    case "+":
        result = num1 + num2
        print(f"The result is {result}")
    case "-":
        result = num1 - num2
        print(f"The result is {result}")
    case "*":
        result = num1 * num2
        print(f"The result is {result}")
    case "/":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"The result is {result}")
    case _:
        print("Invalid operation.")