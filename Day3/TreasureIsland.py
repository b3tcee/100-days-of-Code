#Treasure Island Project

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

direction = input("You find yourself in the heart of a forest . Do you want to go left or right? ").lower()

if direction == "left" :
   choice = input("You come across an old lady, do you 'help' her or 'walk' past her? ").lower()
else:
    print("You walked into a path of Goblins, they enjoyed your bones.")
    quit()
    
if choice == "walk" :
    time = input("You get to the shore of The Woes of Man, do you follow the boat with the 'pixie' or 'death'? ").lower()
else:
    print("She was an evil witch and used you to make her potion. Tasty")
    quit()

if time == "death":
    house = input("You made it across the Woes of Man and as a reward the King wants to give you a house? Which house do you pick? The 'Candy', 'Rock' or 'Gold' house?  ").lower()
else:
    print("Your boat capsized. Sorry :(")
    quit()

if house == "Candy":
    print("There was a pot of treasure underneath the Marshmellow Trees. You Win! :D")
elif house == "Sandy":
    print("The House was filled with dust, you died of Asthma. You lose :(")
    quit()
elif house == "Gold":
    print
    quit()
else:
    print("The King finds you ungrateful, he stones you to death.")
