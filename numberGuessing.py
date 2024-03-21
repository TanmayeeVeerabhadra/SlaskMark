import random
import time

def introduction():
    print("May I ask you for your name?")
    name = input()
    print('Hi '+name + ", we are going to play a game. \nI am thinking of a number between 1 and 200.\n\nTry to Guess the Number")
    print('\nRemember you only have 6 attempts to Guess the number')
    time.sleep(.5)
    print("\nGo ahead. Guess!")
    return name

def guess_number(name):
    num= random.randint(1, 200)
    num_guess_taken = 0
    while num_guess_taken < 6:
        try:
            if(num_guess_taken==5):
                print('Oh Come on! This is your last attempt')
            else:
                print('This is your Guess Number : '+str(num_guess_taken+1))
            guess = int(input("Come on! Guess the Number: "))
            if 1 <= guess <= 200:
                num_guess_taken += 1
                if guess < num:
                    print("Your guess is too low for my number.")
                elif guess > num:
                    print("Your guess is too high for my number.")
                else:
                    print('Good job, ' + name + '! You guessed my number in ' + str(num_guess_taken) + ' guesses!')
                    return
            else:
                print("Please enter a number between 1 and 200.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        print('\n')

    print('Nope. The number I was thinking of was ' + str(num))

play_again = "yes"
while play_again.lower() in ["yes", "y"]:
    player_name = introduction()
    guess_number(player_name)
    play_again = input("\nDo you want to play again? (yes/no): ")