#1)if condition
#2)if condition.....elif condition
#3)if.....else

#age = 18
#f age>18:
  #  print("you can vote")

   #wap which take input as age and print they are old or not
   # 

#age= input()
#if age<18:
# print("you are not old") 
#else:
# print("you are old")


input_age= input("enter a age:")
age=int(input_age)
if age<5:
  print("you are infant")
elif age>5 and age<13:
  print("you are kid")
elif age>13 and age<19:
  print("you are teen")
elif age>19 and age<50:
  print("you are adult")
elif age>50 and age<100:
  print("you are old")
else:
  print("you are dead")


