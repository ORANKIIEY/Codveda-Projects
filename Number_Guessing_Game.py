import random

def guessing_game():
    secret = random.randint(1, 100)
    max_attempts = 7
    attempts = 0

    print("Welcome! I am thinking of a number between 1 and 100.")
    print("You have " + str(max_attempts) + " attempts.")
    print("")

    while attempts < max_attempts:
        attempts = attempts + 1
        remaining = max_attempts - attempts

        guess_input = input("Attempt " + str(attempts) + "/" + str(max_attempts) + " - Your guess: ")

        if guess_input.isdigit() == False:
            print("Please enter a valid number.")
            print("")
            attempts = attempts - 1
            continue

        guess = int(guess_input)

        if guess < 1 or guess > 100:
            print("Please guess between 1 and 100.")
            print("")
            attempts = attempts - 1
            continue

        if guess == secret:
            print("")
            print("Correct! The number was " + str(secret) + ".")
            print("You got it in " + str(attempts) + " attempts!")
            return
        elif guess > secret:
            print("Too high! " + str(remaining) + " attempts remaining.")
            print("")
        else:
            print("Too low! " + str(remaining) + " attempts remaining.")
            print("")

    print("")
    print("Game over! The number was " + str(secret) + ". Better luck next time!")

guessing_game()
