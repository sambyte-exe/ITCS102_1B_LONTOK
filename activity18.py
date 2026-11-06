#boolean variable
run = True

while run == True:
    ask = input("Do you wish to continue this program (yes / no): ")
    
    if ask.lower () == "yes":
        print("You may continue!")
        continue
    else:
        print("You may stopped now!")
        break
