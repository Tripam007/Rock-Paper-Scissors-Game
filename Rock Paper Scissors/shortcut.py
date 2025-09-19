import random
computer = random.choice([-1,0,1])
youstr = input("Enter your choice :")
youDict = {"a": 1, "w" : -1, "d": 0 }
reverseDict = {1 :"Paper",-1 :"Rock",0 : "Scissors"} #Choose a for poper, w for rock and 0 for scissors
you = youDict[youstr] 

print(f"You chose {reverseDict[you]} \nComputer chose {reverseDict[computer]}")

if(computer == you):
    print("Draw")
else:
    if((computer - you) == -1 or (computer - you)== 2 ) :
        print("You lose!")       
    else:
        print("You win!")    