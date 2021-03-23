n = int(input())
if n >= 1 or n <= 200:
    i = 0
    while i < n:
        if i % 2 == 0 and i != 0:
            print(i)
        i += 1
