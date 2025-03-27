import random
import math

##Generate a random number

guess_number = random.randint(1,4)

print(guess_number)

## Choice a random color

colors = ['RED', 'BLUE', 'YELLOW']
random_color = random.choice(colors)
print(random_color)

##"Shuffle cards" 🚀

cards = ['As', 'King', 'Queen', 'Jay', '10']
random.shuffle(cards)

print(cards)