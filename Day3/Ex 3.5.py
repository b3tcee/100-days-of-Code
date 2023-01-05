#LOVE calculator

#Get User and Partner's name
print("Welcome to the love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()

#Conactenate new name
new_name = name1 + name2

#create the count to count the letters
#Using the OR logical operator 
count1= 0
for letter in new_name:
    if(letter == "l" or letter == "o" or letter == "v" or letter == "e") :
     count1 +=1

count2 = 0
for letter in new_name:
    if(letter == "t" or letter == "r" or letter == "u" or letter == "e"):
        count2 += 1
        

loveScore =int(str(count2) + str(count1)) 


if loveScore < 10 or loveScore > 90:
    print(f"Your score is {loveScore}, you go together like coke and mentos.")
elif loveScore >= 40 and loveScore <=50:
    print(f"Your score is {loveScore}, you are alright together.")
else:
    print(f"Your score is {loveScore}.")





