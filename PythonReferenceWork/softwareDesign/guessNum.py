# key point here is speration of concerns

import random

class GuessNumber:
    def __init__(self, number, mn=0, mx=100):
        self.number = number
        self.mn = mn
        self.mx = mx
        self.guesses = 0
    
    def get_guess(self):
        guess = input(f"What is your guess between {self.mn} and {self.mx}? \n")

        if self.valid_guess(guess):
            return int(guess)
        else:
            print("Invalid guess. Please enter a valid guess")
            return self.get_guess()

    def valid_guess(self, guess):
        try:
            number = int(guess)
        except:
            return False
        
        return self.mn <= number <= self.mx

    def play(self):
        while True:
            self.guesses += 1

            guess = self.get_guess()

            if guess < self.number:
                print("Too Low")
            elif guess > self.number:
                print("Too High")
            else:
                break
        
        print(f"Correct, it took you {self.guesses} guesses")

if __name__ == "__main__":
    MN = 0
    MX = 200
    NUMBER = random.randint(MN, MX)
    game = GuessNumber(NUMBER, MN, MX)

    print(NUMBER)

    game.play()
