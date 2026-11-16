#PART 1. EVERY LIST METHOD IS A JEEPNEY MOMENT

passengers = ["Ana", "Ben", "Carla"]
passengers.append("Dan")
passengers.insert(0, "Lola")
passengers.remove("Ben")
x = passengers.pop()
y = passengers.pop(0)
len(passengers)
passengers.reverse()

#PART 2. THE INTERACTIVE JEEPNEY

route = ["Terminal", "Perez Park", "Pacific Mall"]
passengers = []
SEATS = 6
FARE = 13
total = 0

while True:
  print()
  print("Sakay:", passengers)
  print(len(passengers), "of", SEATS, "seats")
  print("1 Sakay")
  print("2 Priority Seat")
  print("3 Para po!")
  print("4 Baba sa pinto")
  print("5 Baba sa harap")
  print("6 Seat check")
  print("7 Balikan")
  print("8 Exit")
  choice = input("Choice: ")

  if choice == "1":
    if len(passengers) == SEATS:
      print("Puno na!")
    else:
      name = input("Name: ")
      passengers.append(name)
      total = total + FARE
      print(name, "Boarded at the Back.")

  elif choice == "2":
    if len(passengers) == SEATS:
      print("Puno na, Kasi!")
    else:
      name = input("Name: ")
      passengers.insert(0, name)
      total = total + FARE
      print(name, "Took the Priority Seat.")

  elif choice == "3":
    name = input("Who is getting off? ")
    if name in passengers:
      passengers.remove(name)
      print(name, "got off, Ingat!")
    else:
      print(name, "is not on this Jeep!")

  elif choice == "4":
    if len(passengers) == 0:
      print("The Jeep is Empty!")
    else:
      left = passengers,pop(0)
      print(left, "got off at the door")

  elif choice == "5":
    if len(passengers) == 0:
      print("The Jeep is Empty!")
    else:
      front = passengers.pop(0)
      print(front, "got off at the front")

  elif choice == "6":
    for i in range(len(passengers)):
      print("Seat", i + 1, passengers[i])

  elif choice == "7":
    route.reverse()
    print("Route: ", route)

  elif choice == "8":
    print("Total Fare Today: ", total)
    break

  else:
    print("Invalid Choice! Come Again.")
  
