'''
Andrew Harris
Number Guess
'''


rightNumber = 77 #Assigning correct number value
guessCount = 0  #Setting guess counter to 0
myName=input("Please enter your name: ") #Setting myName var to input value of prompt
print("Hello " + myName) #Printing response to user with their input name
userGuess=int(input('Please guess a number between 1 and 100: ')) #Setting userGuess var as integer of input value from prompt 
while userGuess != rightNumber: #Beginning of loop 
    if userGuess > rightNumber: #Checking if user guess is greater than rightNumber var
        print("You guessed too high!") #Message for greater than input
        guessCount=guessCount+1 #Incrementing guess counter
        userGuess=int(input('Please guess a number between 1 and 100: ')) #Prompting user again
    elif userGuess < rightNumber: #Checking if user guess is less than rightNumber var
        print("You guessed too low!") #Message for less than input
        guessCount=guessCount+1 #Incrementing guess counter
        userGuess=int(input('Please guess a number between 1 and 100: ')) #Prompting user again
guessCount=guessCount+1 #incrementing guess counter outside of while loop
if guessCount == 1: #adding additional check for correct message grammar 
    print(f'Congratulations, {myName} you guessed the right number in a single try!') #message for right guess on first try
else:
    print(f'Congratulations, {myName} you guessed the right number in {guessCount} tries!') #message for all other right guesses
    
