'''
Purpose: Learning basic features of Python
Author: Carter Blackie
'''

#Task 1: Printing

print(f'The book title is "Learn Python in 21 days".')
print(f"What's mine is mine, and whats yours is mine.")
print(f'''You have enemies? Good. That means you've stood up for something, sometime in your life" Winston Churchill''')
print("""Three things cannot be long hidden:
      the sun, 
      the moon,
      and the truth""")


#Task 2: User Input

food = input("Enter your favorite food: ")
movie = input("Enter your favorite TV show: ")

print(f'I like to eat {food} while watching {movie}')

#Task 3: Converts inches to meters

#CONSTANT
INCH_CONVERSION = 0.254

inch = float(input("Enter the amount of inches: "))
meters = inch * INCH_CONVERSION

print(f'{inch} inche(s) is equal to {meters} meter(s)')

#Task 4: Calculate the cost of pizza and how many are ordered

cost = float(input("Please enter the cost of 1 pizza: $"))
amount = int(input("Please enter the amount of pizzas: "))

total = cost * amount 
print(f'{amount} pizza(s) will cost you ${total} at ${cost} per pizza')

#Task 5: Calculates balance using principles, interests, time and interest compound

principal = float(input("Principal: $"))
interest = float(input("Interest (decimal): "))
years = int(input("Number of years: "))
compound = int(input("Number of times interest compounded per year: "))

balance = principal*(1 + (interest/compound)**(interest * years))
print(f'Balance: ${balance:f}')
