import random
from random import randint

monster_lst = [{'name': 'Anguirus', 'attack_min': 5, 'attack_max': 8, 'health': 90},
{'name': 'Gigan', 'attack_min': 10, 'attack_max': 12, 'health': 85},
{'name': 'Megalon', 'attack_min': 12, 'attack_max': 16, 'health': 95},
{'name': 'Mecha King Ghidorah', 'attack_min': 18, 'attack_max': 20, 'health': 105},
{'name': 'Mothra', 'attack_min': 20, 'attack_max': 22, 'health': 110}]

player_name = input("Please enter player's name: ")
print(f"Welcome {player_name}! Let's play attack!")

def calculate_monster_attack(attack_min, attack_max):
    return randint(attack_min, attack_max)

def game_ends(winner_name):
    print(f"{winner_name} won!")

game_results = []
def print_game_result():
    for result in game_results:
        print(result)

game_running = True
while game_running == True:
    turns = 10
    player = {'name': player_name, 'attack': random.randint(10,22), 'heal': random.randint(15,25), 'health': random.randint(85,105)}
    monster = random.choice(monster_lst)

    print('-' * 20)
    print(player['name'] + ' has ' + str(player['health']) + ' health')
    print(monster['name'] + ' has ' + str(monster['health']) + ' health')

    new_round = True

    player_moves = []

    while new_round == True and turns > 0:
        turns -= 1

        player_won = False
        monster_won = False  

        print("-" * 20)
        print("Please select action ")
        print("1 - Attack")
        print("2 - Heal")
        print("3 - Exit game")

        player_choice = input()
        player_moves.append(player_choice)
        

        if player_choice == '1': 
            monster['health'] -= player['attack']

            if monster['health'] <= 0:
                player_won = True

            else:
                player['health'] -=  calculate_monster_attack(monster['attack_min'], monster['attack_max'])
                
                if player['health'] <= 0:
                    monster_won = True
                 
        elif player_choice == '2': 
            
            if len(player_moves) >= 2 and (player_moves[-1] == '2' and player_moves[-2] == '2'):
                print("You have healed enough! Please attack!")
            else:
                player['health'] = player['health'] + player['heal']

                player['health'] -=  calculate_monster_attack(monster['attack_min'], monster['attack_max'])
                    
                if player['health'] <= 0:
                    monster_won = True
                elif monster['health'] <= 0:
                    player_won = True

        elif player_choice == '3': 
            new_round = False
            game_running = False

        else:
            print("Please select again")

       
        if turns == 0:
            if monster['health'] > player['health']:
                monster_won = True
            elif player['health'] > monster['health']:
                player_won = True
            else:
                print("It's a tie")
            new_round = False

        if player_won == False and monster_won == False:
            print(str(player['name']) , 'has ' + str(player['health']) , 'left')
            print(str(monster['name']) , ' has ' + str(monster['health']) , 'left')

        elif player_won:
            game_ends(player['name'])
            round_result = {'name': player['name'], 'player_health': player['health'], 'rounds': 10 - turns, 'defeated': monster['name'], 'monster_health': monster['health']}
            game_results.append(round_result)
            print("Game result summary")
            print_game_result()
            new_round = False
    
        elif monster_won:
            game_ends(monster['name'])
            round_result = {'name': monster['name'], 'monster_health': monster['health'], 'rounds': 10 - turns, 'defeated': player['name'], 'player_health': player['health']}
            game_results.append(round_result)
            print("Game result summary")
            print_game_result()
            new_round = False

        if player_won == True or monster_won == True:
            new_round = False

  