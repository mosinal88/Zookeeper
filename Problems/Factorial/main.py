n = int(input())
if n >= 1 or n <= 100:
    i = 0
    a = 1
    while i < n:
        a *= i + 1
        i += 1
    print(a)
