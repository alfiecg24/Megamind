import random
import time # For added suspense

firstDigit = 0
secondDigit = 0
thirdDigit = 0
fourthDigit = 0
fifthDigit = 0
tries = 0
guessedFirst = 0
guessedSecond = 0
guessedThird = 0
guessedFourth = 0
guessedFifth = 0
digitsCorrect = 0
playAgain = "no"

print("Welcome to the guessing game!")
print(" ")

time.sleep(1)

mode = str(input("What level of difficulty would you like? Enter E for easy or H for hard: "))

# Easy mode

if mode == "E" or mode == "e":

    answer = random.randint(1000, 9999)

    splitAnswer = [int(a) for a in str(answer)]

    while firstDigit + secondDigit + thirdDigit + fourthDigit != 4:

        guess = input("Please enter your guess: ")
        print(" ")
        splitGuess = [int(a) for a in str(guess)]

        time.sleep(2)
            
        if splitGuess[0] == splitAnswer[0]:

            firstDigit = 1
            guessedFirst = splitGuess[0]

        if splitGuess[1] == splitAnswer[1]:

            secondDigit = 1
            guessedSecond = splitGuess[1]

        if splitGuess[2] == splitAnswer[2]:

            thirdDigit = 1
            guessedThird = splitGuess[2]

        if splitGuess[3] == splitAnswer[3]:

            fourthDigit = 1
            guessedFourth = splitGuess[3]

        if firstDigit == 1 and splitGuess[0] == guessedFirst:

            print("You got the first digit correct")
            print(" ")
            time.sleep(2)

        if secondDigit == 1 and splitGuess[1] == guessedSecond:

            print("You got the second digit correct")
            print(" ")
            time.sleep(2)

        if thirdDigit == 1 and splitGuess[2] == guessedThird:

            print("You got the third digit correct")
            print(" ")
            time.sleep(2)


        if fourthDigit == 1 and splitGuess[3] == guessedFourth:

            print("You got the fourth digit correct")
            print(" ")
            time.sleep(2)

        tries = tries + 1

        
# Hard mode

if mode == "H" or mode == "h":

    playAgain = "no"

    answer = random.randint(10000, 99999)

    splitAnswer = [int(a) for a in str(answer)]

    print(answer)

    while firstDigit + secondDigit + thirdDigit + fourthDigit + fifthDigit != 5:

        guess = input("Please enter your guess: ")
        print(" ")
        splitGuess = [int(a) for a in str(guess)]

        time.sleep(2)
            
        if splitGuess[0] == splitAnswer[0]:

            firstDigit = 1
            guessedFirst = splitGuess[0]

        if splitGuess[1] == splitAnswer[1]:

            secondDigit = 1
            guessedSecond = splitGuess[1]

        if splitGuess[2] == splitAnswer[2]:

            thirdDigit = 1
            guessedThird = splitGuess[2]

        if splitGuess[3] == splitAnswer[3]:

            fourthDigit = 1
            guessedFourth = splitGuess[3]

        if splitGuess[4] == splitAnswer[4]:

            fifthDigit = 1
            guessedFifth = splitGuess[4]

        if firstDigit == 1 and splitGuess[0] == guessedFirst:

            digitsCorrect = digitsCorrect + 1

        if secondDigit == 1 and splitGuess[1] == guessedSecond:

            digitsCorrect = digitsCorrect + 1

        if thirdDigit == 1 and splitGuess[2] == guessedThird:

            digitsCorrect = digitsCorrect + 1

        if fourthDigit == 1 and splitGuess[3] == guessedFourth:

            digitsCorrect = digitsCorrect + 1

        if fifthDigit == 1 and splitGuess[4] == guessedFifth:

            digitsCorrect = digitsCorrect + 1

        tries = tries + 1

        digitsCorrectString = str(digitsCorrect)

        time.sleep(2)

        print("You got " + digitsCorrectString + " digits correct!")
        print(" ")
        digitsCorrect = 0


triesString = str(tries)

print("Correct!")
print(" ")
time.sleep(2)
print("You took " + triesString + " tries!")
print(" ")
time.sleep(1)
print("Thanks for playing!")
