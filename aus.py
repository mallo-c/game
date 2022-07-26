import random 
rule = "/example"
options = {}
playerbalance = 10
def main(actions):
    playername = input('ник: ')
    playermoney = int(input('ставка: '))
    global playername, playermoney
    if playermoney < playerbalance:
        print('ERORR BALANCE') #
    else:
            if random.randint(1, 6) == 1:
                if random.randint(1, 6) != 1:
                    playerbalance *= 1.5
                    print(f'Победил: {playername}')
                    print(playerbalance)
                else:
                    print('Ничья')
            else:
                if random.randint(1, 6) == 1:
                    playerbalance -= playermoney
                    print('Поражение')
                    print(playerbalance)
                else:
                    print('Ничья')
    
            
    return "<h1>Hello</h1>"
main(None)

