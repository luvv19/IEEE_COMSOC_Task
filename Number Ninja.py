import random                   #importing random module

#fuction defined for lowwer difficulty gameplay
def low():
    x = random.randint(1,200)
    for i in range(18):
        guess = int(input("Enter an integer from 1 to 200: "))
        while True:
            if guess < x:
                print ("guess is low")
                guess = int(input("Enter an integer from 1 to 200: "))
            elif guess > x:
                print ("guess is high")
                guess = int(input("Enter an integer from 1 to 200: "))
            else:
                print ("you guessed it right! Bye!")
                opt=int(input("0-Main Menu\n1-play low again\n ->"))      
                if opt==0:
                    Home()
                elif opt==1:
                    low()
                else:
                    exit()   
                break

#defining function for intermediate difficulty gameplay
def medium():
    x = random.randint(1,600)
    for i in range(12):
        guess = int(input("Enter an integer from 1 to 600: "))
        while True:
            if guess < x:
                print ("guess is low")
                guess = int(input("Enter an integer from 1 to 600: "))
            elif guess > x:
                print ("guess is high")
                guess = int(input("Enter an integer from 1 to 600: "))
            else:
                print ("you guessed it right! Bye!")
                opt=int(input("0-Main Menu\n1-play medium again\n ->"))
                if opt==0:
                    Home()
                elif opt==1:
                    medium()
                else:
                    exit()   
                break

#defining function for higher difficulty gameplay
def hard():
    x = random.randint(1,1000)
    for i in range(6):
        guess = int(input("Enter an integer from 1 to 1000: "))
        while True:
            if guess < x:
                print ("guess is low")
                guess = int(input("Enter an integer from 1 to 1000: "))
            elif guess > x:
                print ("guess is high")
                guess = int(input("Enter an integer from 1 to 10020: "))
            else:
                print ("you guessed it right! Bye!")
                opt=int(input("0-Main Menu\n1-play hard again\n ->"))
                if opt==0:
                    Home()
                elif opt==1:
                    hard()
                else:
                    exit() 
                break

#main menu function
def Home():
    print("\t Number Ninja\n")
    print("Select the game difficulty:")
    print(" 1- Low")
    print(" 2- Medium")
    print(" 3- Hard")
    print(" 0- Exit")

    option=int(input("Enter the number to perform function:"))
    if option == 1:
        low()
    elif option == 2:
        medium()
    elif option == 3:
        hard()
    else:
        exit()
Home()                              #calling the main menu function