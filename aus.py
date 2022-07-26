import random

rule = "/example"
options = {}


def main(actions):
    playerbalance = 10
    playername = input("ник: ")
    playermoney = int(input("ставка: "))
    if playermoney < playerbalance:
        print("ERORR BALANCE")  #
    else:
        rand = random.randint(1, 6)
        if rand <= 3:
            playerbalance *= 1.5
            print(f"Победил: {playername}")
            print(playerbalance)
        elif rand <= 5:
            playerbalance -= playermoney
            print("Поражение")
            print(playerbalance)
        else:
            print("Ничья")
    return "<h1>Hello</h1>"


main(None)
