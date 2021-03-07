def sol(n):
    count = 0
    for i in range(n):
        if (i % 3 == 0) or (i % 5 == 0):
            count += i
           
    return count

print(sol(10))
