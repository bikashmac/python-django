

while True:

    n1=float(input("enter a first number"))
    symbol=input("action to perform")
    n2=float(input("enter a second number"))
    if symbol=='+':
        print(n1+n2)
    elif symbol=='-':
        print(n1-n2)

    is_play =input("do you want to continue y/n: ")
    if is_play =='n':
        break

    


