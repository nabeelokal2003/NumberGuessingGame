import random

# def player_guess():
#     choice = int(input('Enter your guess: '))
#     return choice
def difficulty(c):
    match c:
        case 'h':
            game(1, 100)
        case 'm':
            game(1, 50)
        case 'e':
            game(1, 10)
def game(min, max):
    GUESS_NUMBER = random.randint(min, max)
    count = 0
    choice = int(input('Enter your guess: '))
    count += 1

    while choice != GUESS_NUMBER:
        if choice < GUESS_NUMBER:
            print('Go higher.')
            choice = int(input('Enter your guess: '))
        if choice > GUESS_NUMBER:
            print('Go lower.')
            choice = int(input('Enter your guess: '))
        count += 1

    if choice == GUESS_NUMBER:
        print('Correct!!')
        print(f"Total amount of guesses: {count}")


if __name__ == '__main__':
    print('Welcome to Number guessing game!\n')
    print('Hard level: (1 - 100)\nMedium level: (1 - 50)\nEasy level: (1 - 10)\n')
    c = input('Enter your difficulty level (hard = h, medium = m, easy = e): ').lower()
    difficulty(c)
    while 1:
        play_again = input('Would you like to play again? (Y/N): ').upper()
        if play_again == 'Y':
            c = input('Enter your difficulty level (hard = h, medium = m, easy = e): ').lower()
            difficulty(c)
        else:
            quit()


