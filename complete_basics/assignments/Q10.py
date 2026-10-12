# Write a lambda function that takes two numbers as input and returns their product. Use this lambda function with the `map` function to calculate the product of corresponding elements in two lists.

# INSTRUCTIONS: Provide example lists and demonstrate how to use the lambda function with `map`.

product = lambda x, y: x*y
print(product(2,4))

#here we have 2 lists 
lst1 = [2,3,4,5,6,7,8]
lst2 = [1,3,4,3,3,2,4]
#used this map and lambda fun to multiply both the lists
lists_product = list(map(lambda x, y: x*y, lst1, lst2))
print(lists_product)