# For Loops 1
for number in range(5):
    print("Hello")

# For Loops 2
for number in range(11):
    print(number)

# For Loops 3
for n in range(10, -1, -1):
    print(n)

# For Loops 4
i = int(input('How many times should this print? '))
for n in range(i):
    print('devCodeCamp')

# For Loops 5
for n in "packers":
    print(n)

# For Loops 6
for n in range(101):
    if n%3 == 0 and n%5 == 0:
        print('fizzbuzz')
    elif n%3 == 0:
        print('fizz')
    elif n%5 == 0:
        print('buzz')

# While Loops 1
i = 1
while i < 6:
    print ("Hello")
    i += 1

# While Loops 2
password = ""
while password != "password":
    password = input("What is the password? ")
print("User validated")