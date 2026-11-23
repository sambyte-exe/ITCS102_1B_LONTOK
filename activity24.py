while True:
  print("Pleas, select an option:")
  print("1 | Factorial.")
  print("2 | Salute Me.")
  print("3 | Box.")
  print("4 | Exit.")
  choose = int(input("Please, type your option among the list: ")

  if choose == 1:
    print('FACTORIAL')
    number = int(input("Please, enter your chosen number: "))
    print(my_factorial(number))
    continue

  if choose == 2:
    print('SALUTING')
    name = input("Please, enter your name: ")
    salute_me(name)
    continue

  if choose == 3:
    print('BOX')
    number = int(input("Please, enter a box size: "))
    box(number)
    continue

  if choose == 4:
    print('SYSTEM EXIST')
    break
  else:
    print('INVALID CHOICE')
    continue
  
