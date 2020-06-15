import random
i = 0
while i < 100:
    x = random.randint(1,3)
    user = input("rock paper or sissors? ")
    if user == "rock":
        user = int(1)
        if x == 1:
            print ("Tie")
        elif x == 2:
            print ("Computer Win")
        else:
            print ("User Wins")  
    if user == "paper":
        user = int(2)
        if x == 1:
            print ("User Wins") 
        elif x == 2:
            print ("Tie")
        else:
            print ("Computer Win")
    if user == "scissors":
        user = int(3)
        if x == 1:
            print ("Computer Win")
        elif x == 2:
            print ("User Wins")
        else:
            print ("Tie")
    print ("Would you like to play again?")   
    cont = input("yes or no? ")     
    if cont == "yes":
        i += 1
    elif cont == "no":
        i=100
        print ("Pussy")
