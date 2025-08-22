import random
import time
from player_class import Player

def log_action(location, action, player):
    with open("game_log.txt", 'a') as file:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp} | Location: {location} | Action: {action} | Coins: {player.coins} | Lives: {player.lives} | Party: {player.party}\n")

def village(player):
    print("\n You are in the Village.")
    print("1. Go to Tavern")
    print("2. Go to Forest")
    print("3. Go to Mountains")
    choice = input("Choose an option (1-3): ")
    if choice == '1':
        log_action("Village", "Went to Tavern", player)
        return "Tavern"
    elif choice == '2':
        log_action("Village", "Went to Forest", player)
        return "Forest"
    elif choice == '3':
        log_action("Village", "Went to Mountains", player)
        return "Mountains"
    else:
        print(" Invalid choice. Staying in Village.")
        return "Village"

def tavern(player):
    print("\n You enter the Tavern. A Warrior approaches you.")
    print("1. Talk to the Warrior")
    print("2. Leave Tavern")
    choice = input("Choose (1-2): ")
    if choice == '1':
        if "Warrior" in player.party:
            print(" The Warrior is already in your party.")
            action = "Talked to Warrior - Already in party"
        else:
            if random.choice([True, False]):
                print(" The Warrior joins your party for free!")
                player.party.append("Warrior")
                action = "Talked to Warrior - Joined for free"
            else:
                if player.coins >= 10:
                    player.lose_coins(10)
                    player.party.append("Warrior")
                    print(" You paid 10 coins. Warrior joins your party.")
                    action = "Talked to Warrior - Paid 10 coins"
                else:
                    print(" You don’t have enough coins. The Warrior refuses to join.")
                    action = "Talked to Warrior - Not enough coins"
        log_action("Tavern", action, player)
        return "Village"
    elif choice == '2':
        log_action("Tavern", "Left Tavern", player)
        return "Village"
    else:
        print(" Invalid choice. Staying in Tavern.")
        return "Tavern"

def forest(player):
    print("\n You are in the Forest. A mysterious chest lies nearby.")
    print("1. Open the chest")
    print("2. Leave Forest")
    choice = input("Choose (1-2): ")
    if choice == '1':
        if random.choice([True, False]):
            player.add_coins(20)
            action = "Opened Chest - Gained 20 coins"
        else:
            player.lose_life()
            action = "Opened Chest - Trap! Lost 1 life"
        log_action("Forest", action, player)
        return "Village"
    elif choice == '2':
        log_action("Forest", "Left Forest", player)
        return "Village"
    else:
        print(" Invalid choice. Staying in Forest.")
        return "Forest"

def mountains(player):
    print("\n You are at the Mountains.")
    print("1. Attempt to climb")
    print("2. Go back to Village")
    choice = input("Choose (1-2): ")
    if choice == '1':
        weather = random.choice(["sunny", "rainy"])
        if weather == "sunny":
            player.add_coins(20)
            print(" Sunny climb! You earned 20 coins.")
            log_action("Mountains", "Climbed - Sunny - Gained 20 coins", player)
            return "Treasure Room"
        else:
            player.lose_life()
            print(" Rainy and slippery. You lost a life!")
            log_action("Mountains", "Climbed - Rainy - Lost 1 life", player)
            return "Village"
    elif choice == '2':
        log_action("Mountains", "Returned to Village", player)
        return "Village"
    else:
        print(" Invalid choice. Staying at Mountains.")
        return "Mountains"

def treasure_room(player):
    print("\n You have reached the Treasure Room!")
    if player.check_win_condition():
        print(" You have 100+ coins and the Warrior! YOU WIN!")
        log_action("Treasure Room", "VICTORY!", player)
        return "WIN"
    else:
        if "Warrior" not in player.party:
            print("A guardian blocks your path! You lose a life.")
            player.lose_life()
            log_action("Treasure Room", "No Warrior - Guardian attack", player)
        elif player.coins < 100:
            print(" You need at least 100 coins to open the treasure.")
            log_action("Treasure Room", "Not enough coins", player)
        return "Village"

def main():
    player = Player()
    location = "Village"
    open("game_log.txt", 'w').close()
    print(" Welcome to the Adventure Game!")
    while location not in ["WIN", "LOSE"]:
        if player.check_lose_condition():
            print(" GAME OVER - You have no lives left.")
            log_action(location, "GAME OVER", player)
            location = "LOSE"
            break
        if location == "Village":
            location = village(player)
        elif location == "Tavern":
            location = tavern(player)
        elif location == "Forest":
            location = forest(player)
        elif location == "Mountains":
            location = mountains(player)
        elif location == "Treasure Room":
            location = treasure_room(player)
    if location == "WIN":
        print(" CONGRATULATIONS! You won the game!")

if __name__ == "__main__":
    main()
