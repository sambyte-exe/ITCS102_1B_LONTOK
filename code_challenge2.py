# PH Denominations: 1000, 500, 200, 100, 50, 20, 10, 5, 1

money = 19863

money = int(input("Enter Money to Deposit -------> "))
print(type(money))
print("=" * 45)
print("          WELCOME TO THE BANK")
print("=" * 45)
print("Money to Deposit ------>", money, "PHP")

# computation here

bills_1000 = money // 1000
remainder_1000 = money % 1000

bills_500 = remainder_1000 // 500
remainder_500 = remainder_1000 % 500

bills_200 = remainder_500 // 200
remainder_200 = remainder_500 % 200

bills_100 = remainder_200 // 100
remainder_100 = remainder_200 % 100

bills_50 = remainder_100 // 50
remainder_50 = remainder_100 % 50

bills_20 = remainder_50 // 20
remainder_20 = remainder_50 % 20

coins_10 = remainder_20 // 10
remainder_10 = remainder_20 % 10

coins_5 = remainder_10 // 5
remainder_5 = remainder_10 % 5

coins_1 = remainder_5 // 1
remainder_1 = remainder_5 % 1

print()
print("=" * 45)
print("          DENOMINATION BREAKDOWN")
print("=" * 45)
print("\tPHP 1000 -", bills_1000)
print("\tPHP 500  -", bills_500)
print("\tPHP 200  -", bills_200)
print("\tPHP 100  -", bills_100)
print("\tPHP 50   -", bills_50)
print("\tPHP 20   -", bills_20)
print("\tPHP 10   -", coins_10)
print("\tPHP 5    -", coins_5)
print("\tPHP 1    -", coins_1)
print("=" * 45)
