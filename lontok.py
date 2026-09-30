age = int(input("Please enter your age: "))
rev = float(input("Please enter your revenue: "))
cc = int(input("Please enter your credit card number:"))
years_worked = int(input("Please enter the number of years you have worked:"))
has_defaults = input("Please enter your dafault history: ")
collateral = input("Please enter the name of the collateral: ")
c_value = float(input("Please enter the value of the collateral: "))

max_limit = 0
base_fee = 0.0
#baseline
if age >= 21 and years_worked >= 2 and has_defaults == False:
    print("Baseline Requirements Met!")
    max_limit = rev * 3
    base_fee = 0.0
    if cc >= 700:
        print("High Credit Score of 720!")
        if rev >= 50000:
            base_fee = max_limit * 0.015
            print("Base fee rate is ",base_fee)
        else:
            base_fee = max_limit * 0.025
            print("Base fee rate is ",base_fee)

        if c_value >= max_loan:
            print("Collateral", collateral, "--Accepted!")
        else:
            print("Collateral Not Accepeted!")

        surcharge = max_loan * base_fee
        if c_value % 500 != 0:
            surcharge += 250

    elif cc <= 620 and cc < 720:
        max_loan = rev * 1.5
        print("Max Loan is Set To",max_loan)
        if years_worked >= 5:
            max_loan = rev * 0.02
            print("Base fee rate is ",base_fee)
        else:
            base_fee = max_loan * 0.035
            print("Base fee rate is ",base_fee)
    elif cc < 620:
        print("Credir Score Too Low To Apply for Loan!")
    else:
        print("The Requirement is Not Met!")

else:
    print("Rejected: High Risk Application!")
