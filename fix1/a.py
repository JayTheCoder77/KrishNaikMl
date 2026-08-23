# buggy_script.py

def calculate_average(numbers):
    total = 0
    for num in numbers:
        total += num
    
    # BUG 1: Potential ZeroDivisionError if the list is empty
    # BUG 2: Using the wrong variable name (count instead of len)
    average = total / count
    return average

my_list = [10, 20, 30, 40]

# BUG 3: SyntaxError/TypeError due to missing comma and bad indentation below
result = calculate_average(my_list)
print("The average is: " + result
