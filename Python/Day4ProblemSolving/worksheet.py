import math

# 1. Reverse a string
# a. Write code that takes a string as input and returns the string reversed
# b. i.e. “Hello” will be returned as “olleH”

def reverse_string(string):
    split_str = []
    for char in string:
        split_str.append(char)
    split_str.reverse()
    reverse = ''
    for char in split_str:
        reverse += char
    print(reverse)
    return reverse


reverse_string("Hello")
print( 50 * "-")
# 2. Capitalize letter
# a. Write code that takes a string as input and capitalize the first letter of each word. Words will be separated by only one space. i.e. “hello world” should be outputted as “Hello World”

# def capitalize(str):
#     split_str = str.split()
#     print(split_str)
#     caps = ''
#     for word in split_str:
#         caps += word.caplitalize()
#     print(caps)

# capitalize('hello world')

str_hw = "hello world"
caps = str_hw.title()
print(caps)
print( 50 * "-")
# 3. Compress a string of characters
# a. For example, an input of "aaabbbbbccccaacccbbbaaabbbaaa" would compress to "3a5b4c2a3c3b3a3b3a"

def compress(string):
    compressed_str = ''
    x = 1
    for char in range(len(string)-1):
        if string[char] == string[char + 1]:
            x += 1
        else:
            compressed_str = compressed_str + str(x) + string[char]
            x = 1    
    compressed_str = compressed_str + str(x) + string[char]
    print(compressed_str)
compress("aaabbbbbccccaacccbbbaaabbbaaa")
print( 50 * "-")

# 4. BONUS CHALLENGE: Palindrome
# a. A word, phrase, or sequence that reads the same backward as forward i.e. madam
# b. Write code that takes a user input and checks to see if it is a Palindrome and reports the result

def palindrome_check(string):
    split_str = []
    for char in string:
        split_str.append(char)
    split_str.reverse()
    reverse = ''
    for char in split_str:
        reverse += char
    if reverse == string:
        print("Palindrome!")
    else:
        print("Nope.")
    
palindrome_check("hello")
palindrome_check("madam")
print( 50 * "-")

# 1. Happy Numbers 
# a. https://en.wikipedia.org/wiki/Happy_number 
# b. A happy number is a number defined by the following process: starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1. An example of a happy number is 19 
# c. Write a method that determines if a number is happy or sad 
# convert to string, split into arrays and convert back to ints,

def happy_number(number):
    str_number = str(number)
    nums = []
    for i in str_number:
        nums.append(int(i))
    squared_nums = [num**2 for num in nums]
    total = sum(squared_nums)
    if total > 9:
        happy_number(total)
    elif total == 1:
        print('Happy number!')
    else:
        print('Sad number...')

happy_number(19)
happy_number(13)
happy_number(15)
print( 50 * "-")
# 2. Prime Numbers 
# a. A prime number is a number that is only divisible by one and itself. 
# b. Write a method that prints out all prime numbers between 1 and 100  

def prime_number_check(num1, num2):
    numbers = list(range(num1, num2 +1))
    for number in numbers:
        if number > 1:
            for i in range(2, number):
                if (number % i) == 0:
                    break
            else:
                print(number)

prime_number_check(1, 100)
print( 50 * "-")


# 3. Fibonacci 
# a. A series of numbers in which each number (Fibonacci number) is the sum of the two 
# preceding numbers. The simplest is the series 1, 1, 2, 3, 5, 8, etc. 
# b. Write a method that does the Fibonacci sequence starting at 1 
# c. HARDER VERSION: Write a method that does the Fibonacci sequence starting at a 
# number that a user inputs 

def fibonacci(num1):
    fib_numbers = [num1]
    i = 0
    while len(fib_numbers) < 11:
        if i == 0 and fib_numbers[i] == 1:
            next_number = 1
        elif i == 1 and fib_numbers[i] == 1:
            next_number = 2
        else:
            next_number = fib_numbers[i - 1] + fib_numbers[i]
        fib_numbers.append(next_number)     
        i = i + 1
    print(fib_numbers)
    return fib_numbers


fibonacci(1)
print( 50 * "-")

# 1. Given a list of integers, return indices of the two numbers such that they add up to a specific target. You may assume that each input would have exactly one solution, and you may not use the same element twice.
# a. Use Case:i. Given numbers in a list: [5, 17, 77, 50] ii. Target: 55

def two_sum(numbers, target):
    nums = {} # create hash
    for number in numbers:
        print(number)
        num_to_find = target - number
        print(num_to_find)
        if num_to_find in nums: #check if num_to_find is in hash
            print(f"{numbers.index(number)}, {nums[num_to_find]}")
        else:
            nums[number] = numbers.index(number)
            print(nums)

two_sum([5, 17, 77, 50], 55)
print( 50 * "-")

# 2. Given a list of integers, return a bool that represents whether or not all integers in the list can form a sequence of incrementing integers
# a. Use case: i. {5, 7, 3, 8, 6}  false (no 4 to complete the sequence) ii. {17, 15, 20, 19, 21, 16, 18}  true

def is_incrementing_sequence(list):
    list.sort()
    for i in range(len(list) - 1):
        if list[i] == list[i + 1] - 1:
            continue
        else:
            return False
    return True

print(is_incrementing_sequence([17, 15, 20, 19, 21, 16, 18]))
print(is_incrementing_sequence([5, 7, 3, 8, 6]))
print( 50 * "-")

# 3. Create a function that takes a list of positive and negative numbers. Return a list where the first element is the count of the positive numbers and the second element is the sum of negative numbers. 
# a. Use case: [7, 9, -3, -32, 107, -1, 36, 95, -14, -99, 21]

def positive_count_negative_sum(numbers):
    numbers.sort()
    positive_numbers = []
    negative_numbers = []
    for number in numbers:
        if number > 0:
            positive_numbers.append(number)
        else:
            negative_numbers.append(number)
    negative_sum = sum(negative_numbers)
    positive_count = len(positive_numbers)
    return [positive_count, negative_sum]

print(positive_count_negative_sum([7, 9, -3, -32, 107, -1, 36, 95, -14, -99, 21]))
print( 50 * "-")

# 4. Create a function that accepts a string of space separated numbers and returns the highest and lowest number as a string
# a. Use case: “3 9 0 1 4 8 10 2”  “0 10”
def max_min(numbers_string):
    no_spaces = numbers_string.replace(" ", "")
    numbers_list = list(no_spaces) 
    max_min_string = f"{max(numbers_list)} {min(numbers_list)}"
    return max_min_string
    
print(max_min("3 9 0 1 4 8 10 2"))
print( 50 * "-")

# TODO: 5. Create a function that accepts a string, check if it’s a valid email address and returns either true or false depending on the valuation. Think about what is necessary to have a valid email address.
# a. Use case: i. “mike1@gmail.com”  true ii. “gmail.com”  false

print( 50 * "-")
# 6. Create a function that takes in a string and replaces each letter with its appropriate position in the alphabet and returns the string
# a. Use case: i. “abc”  “1 2 3” ii. “coding is fun”  “3 15 4 9 14 7 9 19 6 21 14”

def letters_to_numbers(letters):
    lower = letters.lower()
    no_spaces = lower.replace(" ", "")
    numbers = ""
    for letter in no_spaces:
       numbers += str(ord(letter) - 96) + " "
    return numbers

print(letters_to_numbers("coding is fun"))
print(letters_to_numbers("Coding is Fun"))
print( 50 * "-")
# TODO: 7. A briefcase has a four-digit rolling-lock. Each digit is a number from 0-9 that can be rolled either forwards or backwards. Write a function that returns the smallest number of turns it takes to transform the lock from current combination to the target combination. One turn is equivalent to rolling a number forwards or backwards by one. 
# a. Use case: i. Current lock: 3893 ii. Target lock: 5296

print( 50 * "-")

# 8. Given a number, return the reciprocal of the reverse of the original number, as a double. NOTE: python does not have doubles
# a. Use case: If given 17, return 0.01408 (1/71)

def reverse_reciprocal(number):
    reverse_number = int(str(number)[::-1])
    return (1/reverse_number)

print(reverse_reciprocal(17))
print( 50 * "-")