# age (integer)
# is_employed (boolean)
# credit_score (integer)
# annual_income (float)
# has_collateral (boolean)

age = int(input("Please Enter Your Age ---> "))
is_employed = bool(input("Are you currently employed? ---> "))
credit_score = eval(input("What is your credit score history? ---> "))
annual_income = eval(input("How much is your annual income? ---> "))
has_collateral = bool(input("Do you have any collateral? ---> "))

base_rate = 0.0
if age >= 21 and is_employed == True:
       print("You Meet the Requirements")

#tier1
       if credit_score >= 750:
          print("Your Credit Score is Qualified!")
          if annual_income >= 100000:
            print("You have a high annyal income!")
            base_rate = 4.5
            print("Your Interest Rate is", base_rate)
          else:
            base_rate = 5.0
            print("Your Interest Rate is", base_rate)

#tier2
       elif credit_score >= 600 and credit_score <= 749:
          if has_collateral == True:
              base_rate = 7.0
              print("Your Interest Rate is", base_rate)
          elif annual_income < 400000:
              base_rate = 9.5
              print("Your Interest Rate is", base_rate)
          else:
              base_rate = 8.0
              print("Your Interest Rate is", base_rate)

#tier3
       elif credit_score < 600:
          print("Rejected: Credit Score Too Low!")

else:
       print("Baseline Requirement Failed

    

