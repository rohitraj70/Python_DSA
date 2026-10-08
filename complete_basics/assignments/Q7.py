# Write a Python program that simulates a simple login system. Ask the user for a username and password. If the username is "admin" and the password is "password", print "Login successful". Otherwise, print "Login failed".


user = "admin"
password = "password"

inUser = input("Enter your username: \n")
inPass = input("Enter your password: \n")

if(user == inUser and inPass == password):
    print("Login successful")
else:
    print("Login failed")