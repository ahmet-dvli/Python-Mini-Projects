# Bu mini projede ise basit bir 2 kişilik mini zar oyunu yapıcaz. 

import random

print("Welcome to Dice Game.")

while True:
    input("Player 1 press enter to roll the dice.")
    p1 = random.randint(1,6)
    print("Player 1", p1)

    input("Player 2 press enter to roll the dice.")
    p2 = random.randint(1,6)
    print("Player 2", p2)

    if p1 > p2:
        print("Player 1 Win.")
    elif p2 > p1:
        print("Player 2 Win.")
    else:
        print("İt is draw. İs rolling again...")
        continue

    Try_Again = input("Would you like to play again (e/h): ").lower()
    if Try_Again != "e":
        print("Game over. Thanks for playing.")
        break 