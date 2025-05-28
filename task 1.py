def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

print("Welcome to the Python Calculator!")

while True:
    try:
        
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        
        print("Choose operation: +, -, *, /")
        op = input("Enter operation: ")

        
        if op == '+':
            result = add(num1, num2)
        elif op == '-':
            result = subtract(num1, num2)
        elif op == '*':
            result = multiply(num1, num2)
        elif op == '/':
            result = divide(num1, num2)
        else:
            print("Invalid operation. Please choose +, -, *, or /.")
            continue

        print(f"The result of {num1} {op} {num2} = {result:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

    
    again = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
    if again != 'yes':
        print("Thank you for using the calculator!")
        break
