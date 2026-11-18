#breakdown fix money value to PH denominations
# 1000, 500, 200, 100, 50, 20, 10, 5, 1

money = 19863

money = eval(input("Enter Money to Deposit ------->"))
print(type(money))
print("========== WELCOME TO THE BANK ==========")
print("Money to Deposit ------>", money, "PHP")

#computation here

wankey = money // 1000
wankey1 = money % 1000

paybhan = wankey1 // 500
paybhan1 = wankey1 % 500

twoh = paybhan1 // 200
twoh1 = paybhan1 % 200

wanwan = twoh1 // 100
wanwan1 = twoh1 % 100

pepti = wanwan1 // 50
peptipepti = wanwan1 % 50

bente = peptipepti // 20
bentebente = peptipepti % 20

ten = bentebente // 10
tenten = bentebente % 10

payb = tenten // 5
payb1 = tenten % 5

wan = payb1 // 1
wan2 = payb1 % 1

print()
print("\t1000 - ", wankey)
print("\t500 -", paybhan)
print("\t200 -", twoh)
print("\t100 -", wanwan)
print("\t50 -", pepti)
print("\t20 -", bente)
print("\t10 -", ten)
print("\t5 -", payb)
print("\t1 -", wan)
