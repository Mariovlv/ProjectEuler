def sol(n):
    n1, n2 = 0, 1
    count = 0
    while n2 < n:
        n1, n2 = n2, n1 + n2
        if n2 % 2 == 0:
            count += n2
    return count

print(sol(4000000))
