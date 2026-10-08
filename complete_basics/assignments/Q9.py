# Create a function called `greet` that takes a name and a greeting message as parameters. The greeting message should have a default value of "Hello". The function should print the greeting followed by the name.

# INSTRUCTIONS: Demonstrate how to call the function with and without providing a custom greeting message.


def greet(name, message = "Hello"):
    return f"{message} {name}"

print(greet("Rohit", "Killer"))  #we provided a message
print(greet("Rohit"))   #take the default message "hello"