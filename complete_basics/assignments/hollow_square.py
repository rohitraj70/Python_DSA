def generate_hollow_square(n):
    list = []
    for i in range(n):
        if i == 0:
            print('*'*n)
        elif i <= n-2:
            print('*'+' '*(n-2)+'*')
        elif i == (n-1):
            pass
            print('*' * n)
    return list


print(generate_hollow_square(5))