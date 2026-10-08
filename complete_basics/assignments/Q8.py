# Write a function that takes a list of numbers and returns a new list containing only the even numbers. Use a lambda function within the `filter` function to achieve this.

# INSTRUCTIONS: Provide both the function definition and an example of how to use it with a sample list.


numbers = [1,2,3,4,5,6,7,8,9]  #my test numbers

even_numbers = list(filter(lambda x:x % 2 == 0, numbers))    #used filter and lambda
print(even_numbers)     #printed  [2, 4, 6, 8]
