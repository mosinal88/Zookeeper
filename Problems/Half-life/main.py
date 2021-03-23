atom_one = int(input())
atom_two = int(input())
if atom_one >= 2 or atom_one <= 1000000:
    i = 0
    while atom_one >= atom_two:
        atom_one /= 2
        i += 1
    print(i * 12)
