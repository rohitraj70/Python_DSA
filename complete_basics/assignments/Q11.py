# Explain the difference between positional arguments and keyword arguments in Python functions. Provide clear examples of each.

#positional arguments
# Arguments are matched based on their position/order.
def greet(name, age):
    print(name, age)

greet("Rohit", 22)



#keyword arguments
# arguments that take inputs in key value pairs 

def greet1(name, age):
    # Arguments are passed using the parameter name.
    print(age, name)
    return 0
print(greet1(age = 3, name="rohit"))