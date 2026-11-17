isContinue = True

while isContinue == True:
  ans = input("Do you always watch movies in your free time? (yes/no)").lower()
    
  if ans == "yes":
    title = input("What movie did make you want Part 2? ")
    movie.append(title)
    ans = input("Do you want continue my inquiry? (yes/no)").lower()
    if ans == "yes":
      print("Continue!")
      continue
      
  else:
    print(movie)
