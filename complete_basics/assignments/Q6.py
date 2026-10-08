# Create a program that prints the multiplication table (from 1 to 10) of a number entered by the user using nested loops.
n = int(input("Enter a number"))
for i in range(1):
    for j in range(1, 11):
        print(f"{n} x {j} = {n * j}")
