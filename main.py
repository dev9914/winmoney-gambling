import random
print('Guess the number between 0 to 9 ')
randNumber = random.randint(0,9)
guesses = 0
userGuess = None
while(userGuess != randNumber):
    userGuess = int(input("Enter your guess: "))
    guesses +=1
    if(userGuess == randNumber):
        print("You guessed it right!") 
    else:
        if(userGuess>randNumber):
            print("You guessed it wrong! Enter a samller number")
        else:
            print("You guessed it wrong! Enter a larger number")
        

print(f"You gussed the number in {guesses} guesses")
if(randNumber==5):
    print("your colour is green and voilet both")
elif(randNumber==0):
    print("your colour is red and voilet both")
elif(randNumber%2== 0):
    print("Your colour is red")
else:
    print("Your colour is green")


with open("highscore.txt","r") as f:
    highscore  = int(f.read())

if(guesses<highscore):
    print("You have just broken the high score!")
    with open("highscore.txt", "w") as f:
        f.write(str(guesses))