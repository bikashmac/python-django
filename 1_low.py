data="9762876"
low=10



for number in data:
    number=int(number)
    if number < low:
        low=number
    

print("lowest number is:",low)

