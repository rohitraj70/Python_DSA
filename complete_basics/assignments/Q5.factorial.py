# Write a Python program to calculate the factorial of a given number using a `for` loop
n = int(input("Enter the number"))
fact = 1
if(n == 0):
    print(1)
    exit()
else:
    for i in range(1 , n+1):
        fact = fact * i
    print(fact)