# age (integer)
# is_employed (boolean)
# credit_score (integer)
# annual_income (float)
# has_collateral (boolean)
# want_loan (boolean)
# import demo 
# value_collateral
import getpass

want_loan = bool(input("Hello! Would you like to apply for a loan? "))

print("\n----------------------------------------------")
print("            Authentication Required")
print("----------------------------------------------")

Username = "Samkylit24"
Password = "AlamKoNA"

Username = input("Enter Your Username: ")
Password = getpass.getpass("Enter Your Password: ")

if Username == "Samkylit24" and Password == "AlamKoNA":
            print("Authentication Successful!")

else:
            print("Authentication Failed. Please check your username and password.")
            exit()

# This part will ONLY run if authentication succeeds

print("\n----------------------------------------------")
print("            Authentication Passed")
print("----------------------------------------------")

u = input("Enter Your Job Description: ")
i = input("Enter the Name of the Collateral: ")
j = input("Provide a Description of the Collateral: ")
value_collateral = float(input("Enter the Value of the Collateral: "))

print()

if value_collateral >= 13000:
     print("The collateral value is sufficient to meet the requirement.")

else:
     print("The collateral value is insufficient to meet the requirement. Please try again.")

print("\n----------------------------------------------")
print("              FILL OUT THE FORM")
print("----------------------------------------------")

age = int(input("Please Enter Your Age: "))
is_employed = bool(input("Are You Currently Employed? "))
credit_score = float(input("Please Enter Your Credit Score: "))
annual_income = float(input("Please Enter Your Annual Income: "))
has_collateral = bool(input("Do You Have Any Collateral? "))

base_rate = 0.0

if age >= 21 and is_employed == True:
       print("Application Requirements Met!")

#tier1
       if credit_score >= 750:
          print("Credit Score Meets the Qualification Criteria.")
          if annual_income >= 100000:
            base_rate = 4.5
            print("Applicable Interest Rate: ", base_rate)
          else:
            base_rate = 5.0
            print("Applicable Interest Rate: ", base_rate)

#tier2
       elif credit_score >= 600 and credit_score <= 749:
           if has_collateral == True:
              base_rate = 7.0
              print("Applicable Interest Rate: ", base_rate)
           elif annual_income < 400000:
              base_rate = 9.5
              print("Applicable Interest Rate: ", base_rate)
           else:
              base_rate = 8.0
              print("Applicable Interest Rate: ", base_rate)

#tier3
       elif credit_score < 600:
          print("Application Rejected: Credit Score Does Not Meet the Minimum Requirement.")

else:
       print("Application Requirements Not Met.")

print("\n----------------------------------------------")
print("           THANK YOU! ENJOY YOUR LOAN.")
print("----------------------------------------------")

