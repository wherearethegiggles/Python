def perform_arithmetic_operations():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Addition
    addition = num1 + num2
    print("Addition:", addition)

    # Subtraction
    subtraction = num1 - num2
    print("Subtraction:", subtraction)

    # Multiplication
    multiplication = num1 * num2
    print("Multiplication:", multiplication)

    # Division
    if num2 != 0:
        division = num1 / num2
        print("Division:", division)
    else:
        print("Cannot divide by zero.")


# Call the function
perform_arithmetic_operations()