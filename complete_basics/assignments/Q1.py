# Write a Python function that takes a list of numbers and returns a new list containing only the unique elements, using sets.

def unique_elements(list):
    sett = set()
    sett.update(list)
    return sett

numbers = [1,3,3,3,4,3,2,3,2]
print(unique_elements(numbers))