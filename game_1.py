import random
random_number = random.randrange(1,100)

    
a=1
while a<10:
    guess_number = int(input("guess any number::"))
    if guess_number == random_number:
        print("congratulation!! you guessed correct ")
        break
    if guess_number<random_number:
        print("your guess is less than random number")
    else:
        print("your guess is greater than random number")

    a=a+1