import random

# age = 36
# print(f"I am {age} years old")

# first_name = input('What is your first name? ')
# last_name = input('What is your last name? ')

# full_name = first_name + ' ' + last_name

# print(f"My first name is {first_name} and my last name is {last_name}, which means my full name is {full_name}")

# temp_f = 80.0
# temp_c = (temp_f - 32) * 5/9

# print(f"{temp_f} degrees Fahrenheit is {temp_c} degrees Celsius")

# legal_driving_age_usa = 16
# user_age = int(input('What is your age? '))
# if user_age >= legal_driving_age_usa:
#     print("You are legally able to drive.")
# else: print("You are not old enough to drive yet.")


# random_number = random.randint(0,10)
# print(random_number)
# if random_number <= 2:
#     print("0 or 1 or 2")
# elif random_number > 2 and random_number < 6:
#     print("3 or 4 or 5")
# elif random_number > 5 and random_number < 9:
#     print("6 or 7 or 8")
# elif random_number >= 9:
#     print("9 or 10")

team_name = input("What is the name of your favorite NFL team? ")
if team_name == "Bears":
    print("Quarterback much?")
elif team_name == "Vikings":
    print("Loud noises!")
elif team_name == "Lions":
    print("LOL! They bad!")
elif team_name == "Packers":
    print("Best team in the world! Actually, the universe!")
else:
    print("Pick a different team")
