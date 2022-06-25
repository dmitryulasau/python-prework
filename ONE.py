# Question 1.
    # Write a function to print "hello_USERNAME!" USERNAME is the input of the 
    # function. The first line of the code has been defined as below. 
    # def hello_name(user_name):
print("\n--- Question 1 ---")
def hello_name(user_name):
    """Prints 'hello_USERNAME!' username."""
    print(f"hello_{user_name.upper()}!")

hello_name('dmitry') # -> hello_DMITRY!

# Question 2.
    # Write a python function, first_odds that prints the odd numbers 
    # from 1-100 and returns nothing def first_odds():
print("\n--- Question 2 ---")
def first_odds():
    """Prints odd numbers from 1 to 100."""
    for number in range(1, 101):
        if number % 2 != 0:
            print(number)

first_odds() # -> 1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43
                # 45 47 49 51 53 55 57 59 61 63 65 67 69 71 73 75 77 79 81 83 
                # 85 87 89 91 93 95 97 99

# Question 3.
    # Please write a Python function, max_num_in_list to return the max number 
    # of a given list. The first line of the code has been defined as below. 
    # def max_num_in_list(a_list):
 # Approach 1.
print("\n--- Question 3 ---")
print("-- Approach 1:")
def max_num_in_list(a_list):
    """Finding MAXIMUM number of a given list."""
    if len(a_list) == 0:
        return "No numbers to check."

    return max(a_list)

print(max_num_in_list([])) # -> No numbers to check.
print(max_num_in_list([1, 6, 8, 19, -2, 0, 14])) # -> 19

 # Approach 2.
print("\n-- Approach 2:")
def max_num_in_list2(a_list):
    """Finding MAXIMUM number of a given list."""
    if len(a_list) == 0:
        return "No numbers to check."

    max_number = a_list[0]
    for number in a_list:
        if number > max_number:
            max_number = number

    return max_number

print(max_num_in_list2([])) # -> No numbers to check.
print(max_num_in_list2([1, 6, 8, 19, -2, 0, 14])) # -> 19

# Question 4.
    # Write a function to return if the given year is a leap year. 
    # A leap year is divisible by 4, but not divisible by 100 
    # unless it is also divisible by 400. The return should be 
    # boolean Type (true/false). def is_leap_year(a_year):
print("\n--- Question 4 ---")
def is_leap_year(a_year):
    """Check if the given year is a leap year."""
    if (a_year % 100 == 0) and (a_year % 400 != 0):
        return False
    elif (a_year % 4 == 0) or (a_year % 400 == 0):
        return True
        
    return False

print(is_leap_year(1600)) # -> True
print(is_leap_year(1900)) # -> False
print(is_leap_year(2000)) # -> True
print(is_leap_year(2020)) # -> True
print(is_leap_year(2021)) # -> False
print(is_leap_year(2022)) # -> False

# Question 5.
    # Write a function to check to see if all numbers in the list are 
    # consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, 
    # but [1,2,4,5] are not consecutive numbers. The return should be 
    # boolean Type. def is_consecutive(a_list):
print("\n--- Question 5 ---")
def is_consecutive(a_list):
    """Check if all numbers in the list are consecutive numbers."""
    # Let's sort the list.
    list_sorted = sorted(a_list)
    # We have a sorted list with a_list(MIN) (start) adn a_list(MAX) (end).

    # Make a new_list with consecutive numbers from a_list(MIN) to 
    # a_list(MAX), to include MAX we need to add + 1 to MAX.
    new_list = list(range(min(a_list), max(a_list) + 1))
    # Compare sorted a_list (list_sorted) with a list of consecutive numbers
    # (new_list)
    return list_sorted == new_list

print(is_consecutive([2,3,4,5,6,7]))
print(is_consecutive([1,2,4,5]))