import random


print("========================")
print("Rock paper scissors game")
print("========================")


def game():
    user = input("Write the following: 'ro' for rock, 'pa' for paper, 'sc' for scissors.=> ").lower()
    computer = random.choice(["ro", "pa", "sc" ])

    if(winplayer(user, computer)):

        return "You Won"
    return "You lost"


def winplayer(player, opponet):

    if(player == "ro" and opponet == "sc") or (player == "pa" and opponet == "ro") or (player == "sc" and opponet == "pa"):
        return True
    else:
        False

print(game())