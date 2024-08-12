#WAP to find input number is prime or composit

num= input("enter a number:")
s=int(num)
if s>1:
    for i in range(2,s):
        if s % i == 0:
            print(s,"is not a prime number")
        else:
            print(s,"is a prime number")
