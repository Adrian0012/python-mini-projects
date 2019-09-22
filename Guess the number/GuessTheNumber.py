import random

print('----------------------------------------------------')
print('---------------GUESS THE NUMBER---------------------')
print('----------------------------------------------------')
print()

the_number = random.randint(0, 100)

guess = -1
# in order to place 'guess' in a while loop it has to be defined
# defining 'guess' as -1 has been done because it will never be typed by the player

name = input('what is your name ')

while guess != the_number:
    guess_text = input('Guess the number between 0 and 100: ')
    guess = int(guess_text)

    if guess < the_number:
        # print ('too low')
        print('Sorry {1}, your guess of {0} was too low'.format(guess, name))
    elif guess > the_number:
        print('Sorry {1}, your guess of {0} was too high'.format(guess, name))
    else:
        print('excellent work {1}, your guess of {0} was right'.format(guess, name))

print('Done!')
