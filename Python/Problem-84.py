def sol(n):
    count = 0
    for i in range(1, n+1):
        count += i**i
    return int(str(count)[-10:])

print(sol(1000))
