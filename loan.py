amount = float(input("Enter the loan amount: "))
yr = int(input("Enter the number of years: "))
months = yr * 12
principal = amount / months
rem_bal = amount
interest = 0
payment = 0

for count in range(1, months +1):
    rem_bal -= principal
    interest = rem_bal * 0.00256
    pay = interest + principal
    #print(count, round(pay, 2), round(interest, 2), round(principal, 2), round(rem_bal, 2)) #concatenation
    #string formatting
    print(f"|   {count}\t|\t{round(pay, 2)}\t\t|\t{round(interest, 2)}\t|\t{round(principal, 2)}\t\t|\t{round(rem_bal, 2)}\t\t|")
