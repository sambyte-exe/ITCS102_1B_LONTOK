#Create a python program that would capture age group

name = input("Please input your name ----> ")
age = int(input("Please input your age ----> "))

if age >= 0 and  age <= 5:
          print("This age is not allowed in this program! GET OUT, INFANT!")

elif age >= 10 and age <= 13:
          print("This age is not allowed in this program! GET OUT, KID!")

elif age >= 13 and age <= 17:
          print("This age is not allowed in this program! GET OUT, TEENAGER!")

elif age >= 18  and age <= 28:
          print("This age is allowed in this program! ENJOY, ADULT!")

