import random

dice_number = [1,2,3,4,5,6]
dice_roll = random.choice(dice_number)
number = int(input('introdu un nr de la 1 la 6: '))
if number < dice_roll:
    print(f'ai pierdut, a fost un numar mai mic, ai ales {number} dar a fost {dice_roll}')
elif number > dice_roll:
    print(f'ai pierdut, a fost un numar mai mare, ai ales {number} dar a fost {dice_roll}')
else:
    print(f'super, ai ghicit, ai ales {number} si a fost {dice_roll}')

