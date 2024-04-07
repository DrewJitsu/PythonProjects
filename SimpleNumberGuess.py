'''
Andrew Harris
CIS123
Performance Assessment 4.5
Program 3
'''

from random import randint
import math

players = [] #declaring empty array for players names
scores = [] #declaring empty array for scores
results = [[scores],[players]] #dual array for results
myName = ''
acceptableRange=[1,2,3,4,5,6,7,8,9,10] #setting range of acceptable inputs

def greetUser():
    myName = input("Please enter your name: ")#Setting myName var to input value
    players.insert(0,myName) #inserting names into 'players' array
    print("Hello " + myName) #Printing response to user with their input name
def gameRound():
    rightNumber = randint(1,10) #Assigning random number value
    guessCount = 0  #Setting guess counter to 0
    newGame='y' #setting newGame value for while loop condition

    while newGame=="y": #Setting Loop Condition
        userGuess=int(input('Please guess a number between 1 and 10: ')) #Setting userGuess var as integer of input value from prompt 
        while userGuess != rightNumber:#Beginning of loop
            if userGuess not in acceptableRange: #checking if userGuess is within range 
                    print("Your guess is outside of the range") #prompt if outside of range
                    userGuess=int(input('Please guess a number between 1 and 10: ')) #prompting to enter another guess
                    guessCount=guessCount+1 #Incrementing guess counter
            elif userGuess > rightNumber: #Checking if user guess is greater than rightNumber var
                print("You guessed too high!") #Message for greater than input
                guessCount=guessCount+1 #Incrementing guess counter
                userGuess=int(input('Please guess a number between 1 and 10: ')) #Prompting user again
            elif userGuess < rightNumber: #Checking if user guess is less than rightNumber var
                print("You guessed too low!") #Message for less than input
                guessCount=guessCount+1 #Incrementing guess counter
                userGuess=int(input('Please guess a number between 1 and 10: ')) #Prompting user again
        guessCount=guessCount+1 #incrementing guess counter outside of while loop
        scores.insert(0,guessCount) #inserting scores into scores array
        if guessCount == 1: #adding additional check for correct message grammar 
            print(f'Congratulations, {myName} you guessed the right number in a single try!') #message for right guess on first try
        else:
            print(f'Congratulations, {myName} you guessed the right number in {guessCount} tries!') #message for all other right guesses
        guessCount=0
        newGame=input(f"Should I start another game? ('y' to continue 'n' to see results)") #prompting user for new game
        if newGame=="n":
            print(f'The scores were {results}')
        rightNumber = randint(1,10)
        greetUser()

def main():
    greetUser()
    gameRound()

main()

















    
