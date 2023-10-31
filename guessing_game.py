import random
jackpot = random.randint(1, 100)
counter = 1

guess = int(input("Guess It "))

while guess != jackpot:
    if guess < jackpot:
        print("Guess higher")
    else:
        print("Guess lower")
    guess = int(input("Guess Again "))    
    counter += 1
    
print("Correct Answer")
print("You took", counter, "attempts")