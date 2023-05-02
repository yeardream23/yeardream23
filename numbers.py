import random


def generate_random_number():
    while True:
        digit_number = int(input('What length of number? (3-5): '))
        if digit_number >= 3 and digit_number <= 5:
            return random.sample(range(0, 10), digit_number)
        else:
            print('Length of number must be between 3 and 5 :)')

print(generate_random_number())

