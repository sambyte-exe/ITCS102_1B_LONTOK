print("\n----------------------------------------------")
print("              PACKAGE DETAILS")
print("----------------------------------------------")

sender = input("Please enter your surname: ")
type_of_item = input("Please enter the item name: ")
isFragile = input("Is the item fragile? (True/False): ")
weight = float(input("Please enter the item weight (kg): "))
distance = float(input("Please enter the delivery distance (km): "))
is_express = input("Is this an express shipment? (True/False): ")
is_international = input("Is this an international shipment? (True/False): ")

base_cost = (weight * 2.50) + (distance * 0.15)

if weight <= 1.5 and distance <= 50:
    total = 0.00

elif is_express == "True" and is_international == "True":
    total = (base_cost * 1.40) + 50

elif weight >= 20 or is_express == "True":
    total = (base_cost * 1.20) + 25

elif weight >= 30 or distance >= 1000:
    total = base_cost + 30

else:
    total = base_cost

print("\n==============================================")
print("              SHIPPING RECEIPT")
print("==============================================")
print("Sender Name       :", sender)
print("Item              :", type_of_item)
print("Fragile           :", isFragile)
print("Weight            :", weight, "kg")
print("Distance          :", distance, "km")
print("Express           :", is_express)
print("International     :", is_international)
print("----------------------------------------------")
print("Base Cost         : $", format(base_cost, ".2f"))
print("Total Package Cost: $", format(total, ".2f"))
print("----------------------------------------------")

print("Thank you for your purchase!")
