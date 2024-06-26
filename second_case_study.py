import random

def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1 + die2

def main():
    print("Welcome to the Dice Game!")
    
    first_roll = roll_dice()
    print(f"You rolled {first_roll}")
    
    if first_roll in [7, 11]:
        print("You win!")
    elif first_roll in [2, 3, 12]:
        print("You lose! (Craps)")
    else:
        point = first_roll
        print(f"Your point is {point}. You need to roll {point} again before rolling a 7 to win.")
        
        while True:
            roll = roll_dice()
            print(f"You rolled {roll}")
            
            if roll == point:
                print("You win!")
                break
            elif roll == 7:
                print("You lose!")
                break

main()