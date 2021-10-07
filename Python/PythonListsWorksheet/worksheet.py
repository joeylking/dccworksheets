# Lists Part 1
# 1. Write a function that has one parameter. When you call the function, you will be passing in a list of strings. 
# a. Print to the console the value at the 0 index of the list
# b. Return the value at the 0 index of the list

numbers = [1,2,3,4,5]

def first_number(list):
    print(list[0])

first_number(numbers)

# 2. Write a function that has one parameter. When you call the function, you will be passing in a list of strings that represent different colors -- create a list and append the following values into the list: “blue”, “red”, “white”, “green”, “yellow”
# a. Prompt the user to enter a color.
# b. Iterate over the list. If the user inputted color matches any of the colors in the list, print to the console “You found my chosen color!”

colors = ["blue", "red", "white", "green", "yellow"]

def guess_color(list):
    guess = input("Guess a color: ")
    for color in list:
        if color == guess:
            print("You found my color!")

guess_color(colors)


# 3. Write a function that has one parameter. When you call the function, you will be passing in a list of numbers.
# a. Iterate over the list and add up all of the numbers inside of it
# b. If the sum of the numbers is even, return string “Even” from the function
# c. If the sum of the numbers is odd, return string “Odd” from the function

def sum_even_odd(list):
    sum_list = sum(list)
    if sum_list%2 ==0:
        print("Even")
    else:
        print("Odd")

sum_even_odd(numbers)

# 4. Write a function that has two parameters. The first parameter will represent a list, the second parameter will represent a number.
# a. The list that is passed in needs to be a list of numbers
# b. Iterate over the list and print to the console each value in the list that is greater than the number parameter

def greater_than(list, num):
    for n in list:
        if n > num:
            print(n)

greater_than(numbers, 3)

# Lists Part 2
# 1. Write a function that has one parameter: a list
# a. The list that is passed in needs to be a list of numbers
# b. Compute the average of the numbers inside the list
# c. Any numbers in the list that are less than the computed average will be appended into a separate list. That list will then be returned from the function.

def under_average(list):
    avg = (sum(list))/(len(list))
    under = []
    for n in list:
        if n < avg:
            under.append(n)
    return under

print(under_average(numbers))

# 2. Write a function that has two parameters: a list, a number
# a. Return the value in the list at the index represented by the number parameter
# b. If there is no value at the specified index, print to the console “No value here!”

def index_at_num(list, num):
    try:
        print(f"Found {list[num]} at index {num}")
        return list[num]
    except:
        print("No value here!")

index_at_num(numbers, 1)
index_at_num(numbers, 6)

def index_at_num2(list, num):
    for n in list:
        if n == num:
            print(f"Found {list[num]} at index {num}")
            return list[num]
    print("No value here!")

index_at_num2(numbers, 1)
index_at_num2(numbers, 6)

# 3. Write a function that has one parameter: a list
# a. The list that is passed in needs to be a list of numbers
# b. Find the most frequent value in the list and return that value

def most_frequent_value(list):
    dict = {}
    for n in list:
        dict[n] = [list.count(n)]
    max_key = max(dict, key=dict.get)
    print(max_key)
    return max_key

new_numbers = [1,2,2,3,3,3,4,4,4,4,4,4,5,6]
most_frequent_value(new_numbers)

# 4. Write a function that has two parameters: a list, a list
# a. Both lists that are passed in should contain the first names of people
# b. Iterate over the lists comparing the values at each index from one list to the other. If there is a matching name in both lists, return that name from the function
# c. For example: [“Nevin”, “David”, “Mike”] and [“Brett”, “Mike”, “Charles]
# i. “Mike” would be returned from the function because it is a match in both lists

def name_match(list1, list2):
    for n in list1:
        for m in list2:
            if m == n:
                print(m)
                return m

# def name_match2(list1, list2):
#     names_dict = {}
#     full_list = list1 + list2
#     for n in full_list:
#         names_dict[n] = [full_list.count(n)]
#     dict2 = dict(filter(lambda elem: elem[0] > 1, names_dict.items()))
#     print(dict2)

names1 = ["Nevin", "David", "Mike"]
names2 = ["Brett", "Mike", "Charles"]

name_match(names1, names2)
# name_match2(names1, names2)