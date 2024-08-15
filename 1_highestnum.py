data="9762876"
high=0



for number in data:
    number=int(number)
    if number > high:
        high=number
    
print("highest number is:",high)
