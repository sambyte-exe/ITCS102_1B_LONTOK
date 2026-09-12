sender = input("Please enter your surname: ")
type_of_item = input("Please enter the item name: ")
isFragile = bool(input("Is the item fragile? (True/False): "))
weight = float(input("Please enter the item weight (kg): "))
distance = float(input("Please enter the delivery distance (km): "))
is_express = bool(input("Is this an express shipment? (True/False): "))
is_international = bool(input("Is this an international shipment? (True/False): "))

base_cost = (weight * 2.50) + (distance * 0.15)

if weight >= 1.5 or distance <= 50:  # Shipping is FREE!
    total1 = 0.00
    print("Shipping Fee: FREE")
    print("Total Package Cost: $", total1)

elif is_express is True and is_international is True:  # INTERNATIONAL AND EXPRESS
    total2 = (base_cost * 1.40) + 50
    print("Shipment Type: International Express")
    print("Total Package Cost: $", total2)

elif weight >= 20 or is_express is True:  # EXPRESS / HEAVY ITEM
    total3 = (base_cost * 1.20) + 25
    print("Shipment Type: Heavy/Express")
    print("Total Package Cost: $", total3)

elif weight >= 30 or distance >= 1000:  # OVERSIZED / FAR
    total4 = base_cost + 30
    print("Shipment Type: Oversized/Long-Distance")
    print("Total Package Cost: $", total4)

else:
    print("Shipment Type: Standard")
    print("Total Package Cost: $", base_cost)
