# project-3c

# Author: Craig Sperlazza
# Date: 10/7/2019
# Description: This is a number guessing game that asks the user to guess a number and then alerts the user if her guess was too high, too low, or correct

print("Enter the number for the player to guess.")
user_int = int(input())

guess_count = 0 #The guess count variable is set to 0. This is done outside the loop so we can count the number of guesses without it resetting to 0 each time

play_game = True  #The while loop will run until the player guesses correctly, then we will set play_game variable to false and exit the loop

print("Enter your guess.")

while play_game:
    player_guess = int(input())
    if player_guess > user_int:  #All 3 conditionals will add 1 to the guess_count variable at the beginning of each loop through the conditional
        print("Too high - try again:")
        guess_count += 1
    elif player_guess < user_int:
        print("Too low - try again:")
        guess_count += 1
    elif player_guess == user_int:
        guess_count += 1 #set this before the play_game so it counts the guess prior to exiting the loop
        play_game = False  #if the player guesses correctly we set the play_game variable to False and exit the loop
if guess_count == 1:
    print("You guessed it in 1 try.")
else:
    print("You guessed it in", guess_count,  "tries.")

