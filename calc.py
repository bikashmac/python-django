#make exampke of about 10 pre defined function which can manipulation string with describe.

first_num= input("enter first number:")
a=int(first_num)
symbol= input("enter action you want to perform")
second_num= input("enter second number:")
b=int(second_num)
if symbol == '+':
    print(a+b)
elif symbol == '-':
    print(a-b)
elif symbol == '*':
    print(a*b)
elif symbol == '/':
    print(a/b)

#WAP to find input number is prime or composit

num= input("enter a number")
s=int(num)
if s>1:
    for i in range(2,s):
        if (s % i) == 0:
            print(s,"is not a prime number")
        else:
            print(s,"is a prime number")
        else:
print(s,"is not a prime number")
