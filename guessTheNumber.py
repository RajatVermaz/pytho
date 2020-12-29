import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess!= random_number:
        guess = int(input('Guess a number : '))
        if guess < random_number:
            print('Sorry, try again. Too low')
        elif guess > random_number:
            print('Sorry, try again. Too high')
    print(f'Excillent you guess the number {random_number} correctly')

guess(20)