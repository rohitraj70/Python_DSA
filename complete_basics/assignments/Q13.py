# Design a function that takes a variable number of positional arguments and returns their sum. Use *args to achieve this.

# INSTRUCTIONS: Provide example usage with different numbers of arguments.

def add(*args):
    sum = 0
    lst = []
    lst = args
    for i in lst:
        sum = sum + i
    return sum

print(add(1,2,3,4))
print(add(4,2,5))