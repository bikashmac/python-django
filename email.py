#WAP to take user input email and validate wether it is correct email or not
email= input("enter your email:")
if "@" in email and "." in email:
    print("entered email is valid")
else:
    print("entered email is not valid")




#WAP to take user input mark percentage and find their division.



input_mark= input("enter a your mark percentage:")
mark=int(input_mark)
if mark<40:
    print("you are fail")
elif mark>40 and mark<60:
    print("you got 2nd division.")    
elif mark>60 and mark<80:
    print("you got 1st division.")
elif mark>80 and mark<100:
    print("you got distinsion.") 
else:
     print("entered mark is wrong.")
