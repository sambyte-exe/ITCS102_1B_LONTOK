def factorial(answer):
    result = 1
    for x in range(answer, 0, -1):
        result *= x
    return result

def salute_me(name):
    salute = 'Hi!' + name
    print(salute)
    
def box(number):
    for x in range(number+1):
        for y in range(number+1):
            if x == 0 or y==0 or x==number or y==number:
                print('*', end=" ")
            else:
                print(' ', end=" ")
        print()
    
print('output', '|', factorial(13) + 5)
print('output', '|', factorial(7) + 35)
print('output', '|', factorial(8))
print('output', '|', factorial(5))
print('output', '|', factorial(21))

salute_me(" Samantha, nice to meet you!")
salute_me(" Kevin, nice to meet you!")
salute_me(" Sakura, nice to meet you!")
salute_me(" Andrei, nice to meet you!")

box(7)
box(12)
box(9)
