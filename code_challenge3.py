sender = input("Please enter your surname: ")
type_of_item = input("Please enter the item name: ")
isFragile = bool(input("Is the item fragile? (True/False): "))
weight = float(input("Please enter the item weight (kg): "))
distance = float(input("Please enter the delivery distance (km): "))
is_express = bool(input("Is this an express shipment? (True/False): "))
is_international = bool(input("Is this an international shipment? (True/False): "))


base_cost = (weight * 2.50) + (distance * 0.15)

if weight >= 1.5 or distance <= 50: #Shipping is FREE!
      total1 = 0.00
        print("The Shipping of Item is FREE, The Cost of Package: $", total1)

elif is_express is True and is_international is True : #INTERNATIONAL AND EXPRESS 
      total2 = (base cost * 1.40) + 50
        print("The Item is both International & Express, The Cost of Package: $", total2)

elif weight >= 20 or is_express is True: #EXPRESS / HEAVY ITEM
      total3 = (base cost * 1.20) + 25
        print("The Iten is Heavy and Express, The Cost of Package: $",total3)

elif weight >= 30 or distance >= 1000: #OVERSIZED / FAR
      total4 = base cost + 30
        print("The Iten is Oversized and Far, The Cost of Package: $",total4)

else:
        print("The Item Regular Rate:$", base_cost)
       
