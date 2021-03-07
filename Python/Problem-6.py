def sol(n):
    sum_=((n*(n+1))/2)**2
    for i in range(1, n+1):
        sum_-=i*i
    return sum_

print(sol(100))
