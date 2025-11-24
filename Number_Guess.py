# Bugün basit bir sayı tahmin etme oyunu yapıcaz.

import random

def main():
    print("Welcome to the guess number game")
    print("Please write number between 1 and 100")

    secret = random.randint(1,100) # 1 ile 100 arasında rastgele bir sayı yazar.
    attempts = 0

    while True:
        guess = int(input("Your guess"))
        attempts += 1 

        if guess < secret:
            print("Above")
        elif guess > secret:
            print("Down")
        else:
            print(f"Congratulations you got it on the {attempts}." )
            break

if __name__ == "__main__":
    main()
