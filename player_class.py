class Player:
    def __init__(self):
        self.coins = 0
        self.lives = 3
        self.party = []

    def add_coins(self, amount):
        if amount < 0:
            print(" Cannot add negative coins.")
            return
        self.coins += amount
        print(f" Added {amount} coins. Total coins: {self.coins}. Lives: {self.lives}")

    def lose_coins(self, amount):
        if amount < 0:
            print(" Cannot lose negative coins.")
            return
        if amount >= self.coins:
            self.coins = 0
            print(f" Lost all coins. Total coins: 0. Lives: {self.lives}")
        else:
            self.coins -= amount
            print(f" Lost {amount} coins. Total coins: {self.coins}. Lives: {self.lives}")

    def lose_life(self):
        self.lives -= 1
        print(f" Lost a life. Lives left: {self.lives}. Coins: {self.coins}")
        if self.lives <= 0:
            print("☠️ Oh no! You have no lives left!")

    def gain_life(self):
        self.lives += 1
        print(f" Gained a life! Total lives: {self.lives}. Coins: {self.coins}")

    def check_win_condition(self):
        return self.coins >= 100 and "Warrior" in self.party

    def check_lose_condition(self):
        return self.lives <= 0
