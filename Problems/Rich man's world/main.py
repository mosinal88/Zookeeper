deposit = int(input())
i = 0
while deposit <= 700000:
    deposit = deposit / 100 * 7.1 + deposit
    i += 1
print(i)
