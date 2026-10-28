rose = int(input("Input size of x: "))

for x in range (rose):
    for y in range (rose):
        if x + y == rose or x == y:
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()