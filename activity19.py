from getpass import getpass
isLogin = False
loginAttempt = 0

s = "Sam02"
d = "samantha070712"

while isLogin == False:
    username = input("Please input your most used username: ")
    password = getpass("Please input your password: ")
    
    if username == s and password == d:
        print("Login Successfully!")
        print("Total Login Attemps!", loginAttempt)
        isLogin = True
    else:
        print("Incorrect Usermake and Password")
        loginAttempt += 1
        isLogin = False
