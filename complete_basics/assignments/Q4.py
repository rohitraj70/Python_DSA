# Explain the difference between `break`, `continue`, and `pass` statements in Python loops. Provide code examples to illustrate their usage.

#pass
for i in range(10):
    pass
#here the pass will tell interpreter to ignore the current block , we will update it in future

for i in range(10):
    if (i == 2):
        break  
    print(i)
#brak will directly terminate the loop pre maturely 



for i in range(10):
    if (i == 3):
        continue
    print(i)
#here continue will skip the current iternation



