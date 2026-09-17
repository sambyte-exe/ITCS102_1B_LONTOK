# age (integer)
# is_employed (boolean)
# credit_score (integer)
# annual_income (float)
# has_collateral (boolean)


age = int(input("Please Enter Your Age: "))
is_employed = bool(input("Are you currently employed? (True/False): "))
credit_score = eval(input("Please Enter Your Credit Score: "))
annual_income = eval(input("Please Enter Your Annual Income: "))
has_collateral = bool(input("Do you have any collateral? (True/False) "))

base_rate = 0.0

if age >= 21 and is_employed == True:
       print("Requirements Meet!")

#tier1
       if credit_score >= 750:
          print("Credit Score is Qualified!")
          if annual_income >= 100000:
            base_rate = 4.5
            print("Interest Rate: ", base_rate)
          else:
            base_rate = 5.0
            print("Interest Rate: ", base_rate)

#tier2
       elif credit_score >= 600 and credit_score <= 749:
           if has_collateral == True:
              base_rate = 7.0
              print("Interest Rate: ", base_rate)
           elif annual_income < 400000:
              base_rate = 9.5
              print("Interest Rate: ", base_rate)
           else:
              base_rate = 8.0
              print("Interest Rate: ", base_rate)

#tier3
       elif credit_score < 600:
          print("Rejected: Credit Score Too Low!")

else:
       print("Requirement Failed")

    

