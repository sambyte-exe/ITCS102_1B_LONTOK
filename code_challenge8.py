flowers = int(input("Enter the number of flowers: "))

for s in range(0, flowers):
    for s in range(0, flowers - i - 1):
        print(" ", end="")
    for s in range(0, i + 1):
        print("* ", end="")
    print()

for l in range(0, flowers - 1):
    for l in range(0, i + 1):
        print(" ", end="")
    for l in range(0, flowers - i - 1):
        print("* ", end="")
    print()