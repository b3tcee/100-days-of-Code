#PEMDAS LR
#()
# **
#* /
# + -
# print(3 * 3 + 3 / 3 - 3)

#  Don't change the code below 
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
#  Don't change the code above 

#Write your code below this line 
BMI = float(weight) / int(float(height) ** 2 )
print(int(BMI))