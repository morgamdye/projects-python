import random

# generates a random number between 1 and 100 to the game
number = random.randint(1, 100)
guess = 0

# function that registrates all the game's logic
def number_guess(x, y):
    # is the game's main loop, repeating until the user guess right
    while x != y:
        try:
                # asks for user's input and converts it to int
                x = int(input('Guess the number: '))
                # checks if the input is in the proposed range
                if x < 1 or x > 100:
                    print('Thiss guess is NOT between 1 and 100!\n')
                    continue
        
                # checks if the input is equal to, lesser than or greater than the right number
                if x == y:
                    print('Congrats, you guessed right!')
                elif x < y:
                    print(f'The right number is greater than {x}.\n')
                else:
                     print(f'The right number is lesser than {x}.\n')
        # error handles a wrong input
        except ValueError:
            print('Only integer numbers between 1 and 100.\n')

# introductory message
print('I\'m thinking in a number between 1 and 100.')

# call the main function
number_guess(guess, number)
