for x in range(5, 0, -1):
    for y in range(x):
        print("-", end=" ")
    for z in range(1, 7 - x):
        print(z, end=" ")
    for i in range(x - 7, -1):
        print(i, end=" ")
    for o in range(x):
        print("-", end=" ")
    print()
