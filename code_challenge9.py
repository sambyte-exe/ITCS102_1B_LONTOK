#task2

for x in range (7):
    for y in range (1,14):
        if x + y == 7 or y - x == 7 or x == 6:
            print('*',end='')
        else:
            print(' ',end='')
    print()

print()
print("===============================")
print()

#task3

for x in range (5):
    for y in range (5):
        if x + y == 4 or x == 0 or x == 4:
            print('*',end='')
        else:
            print(' ',end='')
    print()
