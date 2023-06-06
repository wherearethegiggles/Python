def divide_numbers():
    try:
        dividend = int(input("Enter the dividend: "))
        divisor = int(input("Enter the divisor: "))

        result = dividend / divisor
        print("Result:", result)

    except ValueError:
        print("Invalid input. Please enter valid integers.")

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

    finally:
        print("Finally block executed.")

        # Custom exception raising example
        if divisor == 0:
            raise Exception("Custom Exception: Cannot divide by zero.")

try:
    divide_numbers()
except Exception as e:
    print(str(e))