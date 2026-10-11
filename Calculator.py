print("Welcome to your Calculator!!!!!")

print ("Please select an operation you would like to perform: ")
print ("1. Addition")
print ("2.Subtraction")
print ("3.Multiplication")
print("4.Division")
print ("5. Exit")
usr_input = int(input("Enter your choice: "))

if usr_input not in [1, 2, 3, 4, 5]:
    print("Invalid input. Please select a valid operation.")
    exit()


while True:
    try:

        num1 =float(input ("Please enter the first number: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue
    try:
        num2 = float(input("Please enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    if usr_input ==1:
        print (num1, "+", num2, "=", num1 + num2)
        exit()
    elif usr_input ==2:
        print (num1, "-", num2, "=", num1 - num2)
        exit()
    elif usr_input ==3:
        print (num1, "*", num2, "=", num1 * num2)
        exit()
    elif usr_input ==4:
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            print (num1, "/", num2, "=", num1 / num2)
            exit()
    elif usr_input ==5:
        print("Exiting the calculator. Goodbye!")
        exit()

    else:
        print("Invalid input. Please select a valid operation.")
