'''
Purpose: Learning basic features of Python
Author: Carter Blackie
'''

#Task 1: Printing
def task1():
    print(f'The book title is "Learn Python in 21 days".')
    print(f"What's mine is mine, and whats yours is mine.")
    print(f'''You have enemies? Good. That means you've stood up for something, sometime in your life" Winston Churchill''')
    print("""Three things cannot be long hidden:
        the sun, 
        the moon,
        and the truth""")


#Task 2: User Input
def task2():
    food = input("Enter your favorite food: ")
    movie = input("Enter your favorite TV show: ")

    print(f'I like to eat {food} while watching {movie}')

#Task 3: Converts inches to meters
def task3():
    #CONSTANT
    INCH_CONVERSION = 0.254

    inch = float(input("Enter the amount of inches: "))
    meters = inch * INCH_CONVERSION

    print(f'{inch} inche(s) is equal to {meters} meter(s)')

#Task 4: Calculate the cost of pizza and how many are ordered
def task4():
    cost = float(input("Please enter the cost of 1 pizza: $"))
    amount = int(input("Please enter the amount of pizzas: "))

    total = cost * amount 
    print(f'{amount} pizza(s) will cost you ${total} at ${cost} per pizza')

#Task 5: Calculates balance using principles, interests, time and interest compound
def task5():
    principal = float(input("Principal: $"))
    interest = float(input("Interest (decimal): "))
    years = int(input("Number of years: "))
    compound = int(input("Number of times interest compounded per year: "))

    balance = principal*(1 + (interest/compound)**(interest * years))
    print(f'Balance: ${balance:f}')

#Menu for the system 
def menu():
    print("[1] Task 1")
    print("[2] Task 2")
    print("[3] Task 3")
    print("[4] Task 4")
    print("[5] Task 5")
    print("[6] Exit the program!")

#Main loop 
option = 0 

while option != 6:
    menu()
    option = int(input("Enter your option: "))

    if option == 1:
        #Option 1 Stuff
        task1()
    elif option == 2: 
        #Option 2 stuff
        task2()
    elif option == 3: 
        #Option 2 stuff
        task3()
    elif option == 4: 
        #Option 2 stuff
        task4()
    elif option == 5: 
        #Option 2 stuff
        task5()
    elif option == 6: 
        #Option 2 stuff
        print("Exiting the program!")
        break
    else: 
        print("Invalid option.")

