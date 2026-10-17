print("Welcome to the Simple Calculator!")
print("1. ADDITION")
print("2. SUBTRACTION")
print("3. MULTIPLICATION") 
print("4. DIVISION")
print("5. EXIT")
choice = input("Enter your choice (1-5): ")

if choice == '1':
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 + num2
    print(f"The result of addition is: {result}")

elif choice == '2':
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 - num2
    print(f"The result of subtraction is: {result}")

elif choice == '3':
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 * num2
    print(f"The result of multiplication is: {result}")

elif choice == '4':
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if num2 != 0:
        result = num1 / num2
        print(f"The result of division is: {result}")
    else:
        print("Error: Division by zero is not allowed.")

elif choice == '5':
    print("Exiting the program.")
else:
    print("Invalid choice. Please enter a number between 1 and 5.")
    