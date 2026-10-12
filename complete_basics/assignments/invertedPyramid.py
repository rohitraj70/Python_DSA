n = 5
k = 0 
for i in range(1, n+1):
    print(('*' * ((2*n-1) - k)).center(2*n-1))
    k+=2