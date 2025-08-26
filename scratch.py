import random

while True:
    player_total = 0
    bot_total = 0
    ties = 0
    options = ["rock",
            "paper",
            "scissors"]
    while player_total < 2 and bot_total < 2:
        player = input("Rock, paper, scissors: ").lower()
        bot = random.choice(options)
        print("Bot: ", bot)
        if player == bot:
            print("It's a tie")
            ties += 1
        elif (player == "rock" and bot == "scissors") or \
                (player == "paper" and bot == "rock") or \
                (player == "scissors" and bot == "paper"):
            print("You win!")
            player_total += 1
        elif player not in options:
            print("Write in a correct option.")
        else:
            print("You lose.")
            bot_total += 1
    if player_total == 2:
        print(f"You won best out of three and had ", ties, "tie(s)!")

    else:
        print(f"You lost best out of three and had ", ties, "tie(s).")

    replay = input("Play again?(yes or no): ").lower()
    if replay == "yes":
        player_total = 0
        bot_total = 0
    else:
        break

    #let's add tie tracking (done)
#when printing, print result + amount of ties (done)
#error handling (probably done)
#!!! maybe add replay !!!