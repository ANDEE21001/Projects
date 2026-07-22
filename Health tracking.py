def log_physical_activities():
    #Function to log or view physical activities.
    #Prompts the user with choices and performs actions based on the input.
    while True:
        # Display user menu options
        print("1. Log physical activities")
        print("2. View physical activities")

        ob = "logs.txt"  # File used to store activity logs
        t = read_storage(ob)  # Retrieve the current data from storage

        try:
            # Get the user's choice and handle it
            choice = int(input("Enter your choice: "))
            if choice == 1:
                # Log new activities and update the file
                noa(t)
                create_storage(ob, t)
            if choice == 2:
                # Display the logged activities
                read_log(t)
                break  # Exit the loop after viewing logs
        except ValueError:
            # Handle invalid input that isn't an integer
            print("Please enter a number only within this range")


def noa(t):
    #Function to log physical activities into the dictionary.
    try:
        # Prompt the user for the number of activities and ensure it's an integer
        number_of_actvities = int(input("Enter the number of physical activities done: "))
    except ValueError:
        # Handle invalid input for the number of activities inputted
        print("Please enter an integer")
        return

    # Loop through the number of activities provided
    for i in range(int(number_of_actvities)):
        while True:
            # Get the name of the activity from the user
            activity = input("Enter the name of the activity: ")
            if not activity or activity.isdigit():
                # Validate that the activity name is not empty or purely numeric
                print("Please enter a valid activity name")
                continue
            try:
                # Get the total number of times the activity was done
                sets = int(input("Enter overall amount of times done: "))
                if sets <= 0:
                    # Ensure the number of sets is a positive integer
                    print("Please enter a positive integer")
                    continue
            except ValueError:
                # Handle invalid input for sets
                print("Please enter a positive integer")
                continue

            # Add the activity and its sets to the dictionary
            t[activity] = sets
            print("Activities have been successfully logged")
            break


def track_nutrition():
    #Function to track the nutrition details of users.
    while True:
        # Display the menu options
        print("1. Input daily meals")
        print("2. View nutrition")

        try:
            # Get the user's choice and validate it as an integer
            option = int(input("Enter your choice: "))

            if option == 1:
                # Open file in append mode to store meal details
                ob = open("TN.txt", "a")

                # Dictionary to store user meals inputs
                TN = {
                    "Breakfast": "",
                    "Lunch": "",
                    "Dinner": "",
                }

                # Collect user inputs for each meal
                choice1 = input("What have you had for breakfast today: ")
                choice2 = input("What have you had for lunch today: ")
                choice3 = input("What have you had for dinner today: ")

                # Assign user inputs to key/value pairs in the dictionary
                TN["Breakfast"] = choice1
                TN["Lunch"] = choice2
                TN["Dinner"] = choice3

                # Write the meal input to TN.txt file
                ob.write(f"{list(TN.values())}\n")
                ob.close()

            if option == 2:
                # Open TN.txt in read mode to display meal details
                ob = open("TN.txt", "r")
                print(f"{ob.read()}")
                ob.close()

                # Open Calorie.txt in read mode to display nutritional info
                ob = open("Calorie.txt", "r")
                print(f"{ob.read()}")
                ob.close()

                # Exit the loop after viewing nutrition data
                break

        except ValueError:
            # Handle invalid input
            print("Please enter a number only within this range")


def calorie_intake():
    #Function to track and manage calorie intake and calories burned.
    CI = {}  # Dictionary to store calorie data

    while True:
        # Display the user menu for calorie intakes
        print("1. View amount of calorie intake:")
        print("2. Input amount of calories taken")
        print("3. Input amount of calories burned")

        try:
            # Get the user's choice and validate it as an integer
            choice = int(input("Enter your choice: "))

            if choice == 2:
                # Open Calorie.txt in append mode to add calorie intake data
                ob = open("Calorie.txt", "a")

                # Dictionary to store calorie intake for meals
                CI = {
                    "Calorie for breakfast": "",
                    "Calorie for lunch": "",
                    "Calorie for dinner": ""
                }

                # Collect calorie for each meal
                option1 = input("How many calories for breakfast today: ")
                option2 = input("How many calories for lunch today: ")
                option3 = input("How many calories for dinner today: ")

                # Assign calorie data to dictionary keys
                CI["Calorie for breakfast"] = option1
                CI["Calorie for lunch"] = option2
                CI["Calorie for dinner"] = option3

                # Calculate total calorie intake
                option4 = int(option1) + int(option2) + int(option3)
                CI["Total calorie"] = option4

                # Save the total calorie intake to the file
                ob.write(f"{'Total calorie intake':{option4}}\n")
                print("Successful")
                ob.close()

            if choice == 1:
                # Open Calorie.txt in read mode to display stored calorie information
                ob = open("Calorie.txt", "r")
                print(f"{ob.read()}\n")
                ob.close()

            if choice == 3:
                # Open Calorie.txt in read+write mode to update calories burned
                ob = open("Calorie.txt", "r+")
                option5 = int(input("How many calories have you burned: "))
                CI["Calories Burned"] = option5

                # Save the burned calorie information to the file
                ob.write(f"Calories Burned:{option5}\n")
                ob.close()
                print("Successfully updated calories burned.")

            # Exit the loop after processing a valid choice
            break

        except ValueError:
            # Handle invalid input for menu options
            print("Please enter a number only within this range")


def display_calories_burned():
    #Function to display the total calories burned from the log file.
    try:
        # Open the calorie log file in read mode
        with open("Calorie.txt", "r") as file:
            calories_burned = None  # Initialize the variable to store calories burned

            # Read the file line by line and search for "Calories Burned"
            for line in file:
                if "Calories Burned" in line:
                    # Split the line into key and value, then store the calorie value
                    key, value = line.strip().split(":")
                    calories_burned = int(value)
                    break

            # Display the calories burned if found, otherwise notify the user
            if calories_burned is not None:
                print(f"Total calories burned: {calories_burned}")
            else:
                print("No record of calories burned found in the log.")
    except FileNotFoundError:
        # Handle the case where the file does not exist
        print("Calorie log file not found. Please log some data first.")


def summary2():
    #Function to display the users activities done.
    # Open the "logs.txt" file in read mode
    ob = open("logs.txt", "r")

    # Print the contents of the file
    print(f"{ob.read()}")


def View_progress_towards_goals():
    #Function to manage and view progress towards fitness goals.
    VPTG = {}  # Dictionary to store fitness goals temporarily

    while True:
        # Display the menu options for fitness goals
        print("1. Create new fitness goal")
        print("2. Update current fitness goal")
        print("3. View current fitness goal")

        try:
            # Get the user's choice and validate it as an integer
            choice = int(input("Enter your choice: "))

            if choice == 1:
                # Open fitness.txt in append mode to add a new goal
                ob = open("fitness.txt", "a")
                option = input("Enter exercise: ")  # Name of the exercise
                option1 = int(input("Enter amount to be done: "))  # Target amount
                VPTG[option] = option1

                # Write the new goal to the file
                ob.write(f"{option}:{option1}\n")
                ob.close()

            elif choice == 2:
                # Open fitness.txt in read/write mode to update it
                ob = open("fitness.txt", "r+")
                option = input("Enter exercise to update: ")  # Exercise name to update

                # Check if the exercise exists in the dictionary
                if option in VPTG:
                    option2 = int(input("Enter amount done: "))  # Progress made
                    VPTG[option] -= option2  # Update the remaining goal
                    ob.seek(0)  # Move file pointer to the beginning

                    # Write the updated data to the file
                    ob.write(f"{VPTG}\n")
                    ob.truncate()  # Remove remaining file content
                    ob.close()
                    print("Successfully updated")

            elif choice == 3:
                # Open fitness.txt in read mode to view current
                ob = open("fitness.txt", "r")
                print(ob.read())  # Display the file contents
                ob.close()

            # Exit the loop after processing a valid choice
            break

        except ValueError:
            # Handle invalid input for menu options
            print("Please enter a number only within this range")


def submain():
    #Function to provide the main menu for the fitness tracking system.
    while True:
        # Display the menu options
        print("1. Log physical activities")
        print("2. Track nutrition")
        print("3. Calorie intake")
        print("4. View progress towards fitness goals")
        print("5. Fitness summary")
        print("6. Personalised fitness goal")
        print("7. Sign Out")

        try:
            # Get user's choice and validate as an integer
            choice1 = int(input("Enter your choice: "))

            if choice1 == 1:
                # Navigate to log physical activities
                log_physical_activities()
            elif choice1 == 2:
                # Navigate to track nutrition
                track_nutrition()
            elif choice1 == 3:
                # Navigate to calorie intake
                calorie_intake()
            elif choice1 == 4:
                # Navigate to view progress towards fitness goals
                View_progress_towards_goals()
            elif choice1 == 5:
                # Display fitness summary: calories burned, logs, and progress
                display_calories_burned()
                summary2()
                progress()
            elif choice1 == 6:
                # Navigate to personalised fitness goal
                personalised_fitness_goal()
            elif choice1 == 7:
                # Exit the menu
                break
            else:
                # Handle invalid menu choice
                print("Invalid choice, please choose between 1 and 7.")
        except ValueError:
            # Handle non-integer input
            print("Invalid input. Please enter a number between 1 and 7.")


def personalised_fitness_goal():
    #Function to create and view personalised fitness goals.
    PA = {}  # Dictionary to store planned activities and their quantities
    PC = {}  # Dictionary to store calorie goals
    MEAL = {}  # Dictionary to store meal plans

    while True:
        # Open the file to append new goals or view existing ones
        ob = open("personalised_fitness_goal.txt", "a")
        print("1. Create personalised fitness goal")
        print("2. View personalised fitness goal")

        try:
            # Prompt the user for their choice
            choice1 = int(input("Enter your choice: "))

            if choice1 == 1:
                # Input planned activities
                times = int(input("How many activities do you plan on doing? "))
                for i in range(times):
                    plan_activity = input("Which activity do you plan on doing: ")
                    plan_quantity_activity = input("Amount to be done: ")
                    PA[plan_activity] = plan_quantity_activity

                # Input calorie goal
                plan_calories = int(input("How many calories do you plan on burning? "))
                PC["Calories to be burned"] = plan_calories

                # Write activities and calorie goals to the file
                ob.write("Activities:\n")
                for plan_activity, plan_quantity_activity in PA.items():
                    ob.write(f"{plan_activity}: {plan_quantity_activity}\n")
                ob.write(f"Calories to be burned: {plan_calories}\n")

                # Prompt for diet plan
                print("Do you want to plan a diet?")
                choice = input("Input choice (y/n): ")
                if choice == "y":
                    # Input diet plan details
                    meal = input("What would you like to eat for breakfast: ")
                    meal1 = input("What would you like to eat for lunch: ")
                    meal2 = input("What would you like to eat for dinner: ")
                    MEAL["Breakfast"] = meal
                    MEAL["Lunch"] = meal1
                    MEAL["Dinner"] = meal2

                    # Write diet plan to the file
                    ob.write("Diet plan:\n")
                    ob.write(f"Breakfast: {meal}\n")
                    ob.write(f"Lunch: {meal1}\n")
                    ob.write(f"Dinner: {meal2}\n")
                    print("Successfully planned a diet")
                ob.close()

            elif choice1 == 2:
                # Open the file in read mode to view personalised fitness goals
                ob = open("personalised_fitness_goal.txt", "r")
                print("Personalised fitness goal:")
                print(ob.read())
                ob.close()

            # Exit the menu after processing the choice
            break

        except ValueError:
            # Handle invalid input for menu options or numeric entries
            print("Please enter a number only within this range")


def progress():
    #Function to display the user's fitness progress.
    # Open the "fitness.txt" file in read mode
    ob = open("fitness.txt", "r")

    # Print the contents of the file to display fitness progress
    print(ob.read())

    # Close the file after reading
    ob.close()
def read_log(t):
    #Function to display logged physical activities and their corresponding sets.
    # Loop through the dictionary and print each activity with its corresponding sets
    for activity, sets in t.items():
        print(f"{activity} - {sets}")


def signup(h):
    #Function to handle user signup by adding a new username and password.
    while True:
        # Prompt user for a username
        username = input("Username: ")
        if username in h:
            # Notify user if the username is already taken
            print("This username is already taken")
            continue
        # Prompt user for a password
        password = input("Password: ")

        # Add the username and password to the dictionary
        h[username] = password
        break
def read_h(fp):
    #Function to read user credentials from a file and store them in a dictionary.
    h = {}  # Initialize an empty dictionary to store credentials
    try:
        # Open the file in read mode
        with open(fp, mode='r') as file:
            # Read the file line by line
            for line in file:
                if ":" in line:
                    # Split the line into username and password at the colon
                    username, password = line.strip().split(":")
                    # Add the username and password to the dictionary
                    h[username] = password
    except FileNotFoundError:
        # Handle the case where the file does not exist
        pass  # Gracefully continue without raising an error
    return h

def store_user(fp, h):
    #Function to store user credentials into a file.
    # Open the specified file in write mode
    with open(fp, mode='w') as file:
        # Write each username-password pair to the file
        for username, password in h.items():
            file.write(f"{username}:{password}\n")
def create_storage(ob, t):
    #Function to store physical activity logs into a file.
    # Open the specified file in write mode
    with open(ob, mode='w') as file:
        # Write each activity and its corresponding sets to the file
        for activity, sets in t.items():
            file.write(f"{activity}:{sets}\n")

def read_storage(ob):
    #Function to read stored activity logs from a file into a dictionary.
    t = {}  # Initialize an empty dictionary to store activity logs
    try:
        # Open the specified file in read mode
        with open(ob, mode='r') as file:
            # Read the file line by line
            for line in file:
                if ":" in line:
                    # Split the line into activity and sets at the colon
                    activity, sets = line.strip().split(":")
                    # Add the activity and sets (as an integer) to the dictionary
                    t[activity] = int(sets)
    except FileNotFoundError:
        # Handle the case where the file does not exist
        pass  # Gracefully continue without raising an error
    return t


def login(h):
    #Function to handle user login by verifying their username and password.
    while True:
        # Prompt the user to enter their username
        username = input("Enter your username: ")
        if username not in h:
            # Notify the user if the username is invalid
            print("Invalid username")
            continue

        # Prompt the user to enter their password
        password = input("Enter your password: ")
        if password != h[username]:
            # Notify the user if the password is incorrect
            print("Wrong password, try again")
            continue

        # Update the password in the dictionary (if needed)
        h[username] = password
        break


def main():
    #Main function for the health and fitness tracking system.
    # Define the file path for storing user credentials
    fp = "H and T.txt"

    # Load existing user credentials from the file
    h = read_h(fp)

    while True:
        # Display the main menu options
        print("Health and fitness tracking system")
        print("1. Sign up")
        print("2. Login with existing username and password")
        print("3. Exit")

        try:
            # Prompt the user for their choice and validate it as an integer
            choice = int(input("Enter your choice: "))

            if choice == 1:
                # Sign up a new user
                signup(h)
                store_user(fp, h)  # Save the updated credentials
                submain()  # Navigate to the main system after signing up

            elif choice == 2:
                # Login with an existing account
                login(h)
                submain()  # Navigate to the main system after logging in

            elif choice == 3:
                # Exit the program
                print("Goodbye")
                exit()

            elif choice > 3 or choice <= 0:
                # Handle input that's outside the valid range
                print("Invalid. Input is out of range")

        except ValueError:
            # Handle invalid (non-integer) input
            print("Invalid input. Please enter a number.")


# Ensure the program starts by calling main when executed
if __name__ == '__main__':
    main()