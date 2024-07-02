import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def number_guess_game():
    while True:
        clear_console()
        print("============================================")
        print("Please make sure to check out my parser: https://github.com/MilimCode/Rule34-Image-Parser")
        print("============================================")
        print("Welcome to the Number Guess Game!")
        print("============================================")
        guess = input("Guess a number between 1 and 10: ")
        target = int.from_bytes(os.urandom(1), "big") % 10 + 1
        if guess == str(target):
            print("Correct! You guessed the number!")
        else:
            print(f"Sorry, the correct number was {target}.")
        input("Press Enter to play again...")

if __name__ == '__main__':
    number_guess_game()
