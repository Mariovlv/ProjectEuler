def sol(n):
    count = 0
    max_ = 1
    max_relative = 0
    for i in range(2, n):
        max_relative = 0
        dinamyc = i
        while dinamyc > 1:
            print(dinamyc)
            if dinamyc % 2 == 0:
                count += 1
                dinamyc = dinamyc/2
            else:
                dinamyc = (dinamyc*3)+1
                count += 1

        max_relative = count
        if max_relative > max_:
            max_ = max_relative
        else:
            count = 0
    return max_

print(sol(1000000))
