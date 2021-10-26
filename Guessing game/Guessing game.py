#The program chooses numbers randomly and then makes the user guess it
import random
def guessing_game(a,menu,difficulty): #We put all of our code into a program that takes care of our "game"
            

    for i in range(5): #The number of times we guess a number from 1 to 99
        a.append(random.randint(1, difficulty)) #Choosing a random number
        g = int(input("Enter an integer from 1 to "+str(difficulty)+" : "))  #Guessing a valid input, it's an error otherwise
        while a[i] != g: #we check if we haven't guessed it yet
            if g < a[i]: #checking if our guess is too low or too high
                print("guess is low")
                g = int(input("Enter an integer from 1 to 99: "))
            elif g > a[i]:
                print("guess is high")
                g = int(input("Enter an integer from 1 to 99: "))
            else: #Probably unnecesary, but I'll keep it as is for now
                break
        print("you guessed it!")

def choose_gamemode(menu):
    gamemodes={'Easy'.upper() : 1 , 'Hard'.upper() : 2 , '.Easy'.upper() : 3, '.Hard'.upper() : 4} #We declare all the possible valid inputs from the user
    for i in gamemodes:
         if i == menu or str(gamemodes[i] == menu) :
             return gamemodes[i] #We return the number assigned to the difficulty
    return False


if __name__ == "__main__":
    
    menu= input('Please select the difficulty: 1.Easy | 2.Hard').upper() #ask for difficulty
    while not choose_gamemode(menu): #check the validity
         print('WRONG')
         menu= input('Please select the difficulty: 1.Easy | 2.Hard').upper()
    if int(menu) == 1: #setting the difficulty accordingly
        difficulty = 50 #easy
    else:
        difficulty = 99 #hard
    a = [] #list for the numbers
    guessing_game(a,menu, difficulty) #the game itself
    
