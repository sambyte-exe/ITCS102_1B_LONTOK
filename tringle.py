for x in range(5, 0, -1):
    for y in range(x):
        print("%", end=" ")
    for z in range(1, y):
        print(z, end=" ")
    print()
