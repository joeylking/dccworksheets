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

# 3. Compress a string of characters
# a. For example, an input of "aaabbbbbccccaacccbbbaaabbbaaa" would compress to "3a5b4c2a3c3b3a3b3a"

def compress(string):
    compressed_str = ''
    x = 1
    for char in range(len(string)-1):
        if string[char] == string[char + 1]:
            x += 1
        else:
            # compressed_str = str(x) + compressed_str + string[char]
            compressed_str = compressed_str + str(x) + string[char]
            x = 1    
    # compressed_str = str(x)  + compressed_str + string[char+1]
            # compressed_str = str(x) + compressed_str + string[char]
    compressed_str = compressed_str + str(x) + string[char]
    print(compressed_str)
compress("aaabbbbbccccaacccbbbaaabbbaaa")

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
# 2. Prime Numbers 
# a. A prime number is a number that is only divisible by one and itself. 
# b. Write a method that prints out all prime numbers between 1 and 100  



# 3. Fibonacci 
# a. A series of numbers in which each number (Fibonacci number) is the sum of the two 
# preceding numbers. The simplest is the series 1, 1, 2, 3, 5, 8, etc. 
# b. Write a method that does the Fibonacci sequence starting at 1 
# c. HARDER VERSION: Write a method that does the Fibonacci sequence starting at a 
# number that a user inputs 