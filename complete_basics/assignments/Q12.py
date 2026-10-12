# Write a recursive function to calculate the factorial of a given non-negative integer.

def factorial(n):
    fact = n
    # if n == 0:
    if n == 1:
        return fact
    elif n > 0:
        fact = fact * factorial(n-1)
        return fact

a = factorial(4)
print(a)