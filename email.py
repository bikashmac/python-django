#WAP to take user input email and validate wether it is correct email or not


email= input("enter your email:")
if "@" in email and "." in email:
    print("entered email is valid")
else:
    print("entered email is not valid")
