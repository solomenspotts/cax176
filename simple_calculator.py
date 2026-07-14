# Assigning user imput to variables
number_1 = int(input("Enter a number: "))
number_2 = int(input("Enter a another number: "))
operation_choice = input("Choose an operation (+, -, *, /):")

if operation_choice == "+":# Calculates input with addition
    print(f"The total is {number_1 + number_2}.")
elif operation_choice == "-": # Calculates input with subtraction
    print(f"The total is {number_1 - number_2}.")
elif operation_choice == "/":# Calcutates input with division
    print(f"The total is {number_1 / number_2}")
elif operation_choice == "*":# Calculates input with multiplication
    print(f"The total is {number_1 * number_2}")
else:
    print("Invalid operation error.")
