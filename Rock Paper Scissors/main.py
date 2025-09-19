import random
computer = random.choice([-1,0,1])
youstr = input("Enter your choice :")
youDict = {"a": 1, "w" : -1, "d": 0 } #Choose a for poper, w for rock and 0 for scissors
reverseDict = {1 :"Paper",-1 :"Rock",0 : "Scissors"}


you = youDict[youstr] 

print(f"You chose {reverseDict[you]} \nComputer chose {reverseDict[computer]}")

if(computer == you):
    print("Draw")
else:    
    if(computer == -1 and you ==1):
     print("You win!")
    elif(computer == -1 and you ==0):
     print("You lose!")
    elif(computer == 1 and you ==-1):
     print("You lose!")
    elif(computer == 1 and you ==0):
     print("You win!")
    elif(computer == 0 and you ==-1):
     print("You lose!")
    elif(computer == 0 and you ==1):
     print("You lose!")
    else:
     print("Something is wrong")    

    
