import random

class entity():
    def __init__(self, name, attack, health):
        self.name = name
        self.attack = attack
        self.health = health

class attack():
    def __init__(self, damage, attack_str):
        self.damage = damage
        self.attack_str = attack_str

    def do_attack(self, enemy):
        print(f'{self.attack_str} doing {self.damage} points of damage')
        enemy.health = enemy.health - self.damage

def xdy(x,y):
    pass

def fetch_enemy():
    return entity('Goblin', attack(random.choice(range(1,4)), 'swings club'), 15)

if __name__ == '__main__':
    player = entity('Kazagha', attack(random.choice(range(1,12)),'swings sword'), 100)
    enemy = fetch_enemy()

    while(player.health > 0 and enemy.health > 0):
        print(f'{player.name} is at {player.health} points of health')

        player.attack.do_attack(enemy)
        enemy.attack.do_attack(player)