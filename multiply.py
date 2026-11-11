rose = int(input("Enter Number of Columns: "))

for x in range(1, 11):
    for y in range(1, rose+1):
        print(x," x ", y,"=", x*y, end= "\t\t")
    print()
