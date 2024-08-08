name = "apple is sweet"

b= "and it's healthy"
c=name+" "+b  #(apple is sweet and it's healthy)

cost= 100

print(name.upper())   #used to make all letters capital(APPLE IS SWEET )
print(name.lower())   #used to make all letters lowercase(apple is sweet)
print(name.title())   #used to make first letter of each sentence capital(Apple Is Sweet)
print(name.capitalize())   #used to only first letter capital in sentence(Apple is sweet)
print(name.swapcase())   #used to change whole sencence into lower to upper or vice versa(APPLE IS SWEET)
print(name[2:6])  #used to print certain number of letters(ple)
print(name.replace("is","are"))  #used to replace cetrain words or letter with other in sentence(apple are sweet)
print(name.split("is"))   #used to split a sentense from certain letter or word or character( 'apple','sweet')
print(c)
txt=f"and cost {cost}"
print(c+" "+txt)    #(apple is sweet and it's healthy and cost 100)
print(c.count("a"))  #used to count the number of characters or letters in sentence(3)



#string.lower()
#string.title()
#string.capitalize()
#string.swapcase()


