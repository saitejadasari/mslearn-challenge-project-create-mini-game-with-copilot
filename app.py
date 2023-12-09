import random

print("Let's play Rock, Paper, Scissors...")

options = ["rock", "paper", "scissors"]

wins = 0
ties = 0
total = 0
while True:
    inp = input("Enter your choice: ").lower()
    total += 1
    if inp == "screen":
        print("Total Games = ", total)
        print("Wins", wins, " Losses", total-wins-ties, " Ties", ties)
        cont = input("Do you want to continue. Y or N? ").lower()
        if cont == 'n':
            break
    elif not inp in options:
        print("Invalid option. Try again!")
        continue
    else:
        ch = random.choice(options)
        print("choice:", ch)

        if inp == ch:
            ties += 1
            print("It's a tie")
        elif (inp == "rock" and ch == "paper") or (inp == "paper" and ch == "scissors") or (inp == "scissors" and ch == "rock"):
            print("You Lost!")
        else:
            wins += 1
            print("You Win!")
        
        cont = input("Do you want to continue. Y or N? ").lower()
        if cont == 'n':
            break


print("Total Games =", total)
print("Wins", wins, " Losses", total-wins-ties, " Ties", ties)
