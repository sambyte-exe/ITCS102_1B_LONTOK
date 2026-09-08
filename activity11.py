#import demo 
import getpass

Username = "sambyte07"
Password = "Miracle_Domain24"

s = input("Input USERNAME ----> ")
u = getpass.getpass("Input PASSWORD  ----> ")

if s == Username and u == Password:
           print("Login Successfully!")

else: 
           print("Access Denied!")