import random

class entity():
    def __init__(self, name, attack, health):
        self.name = name
        self._attack = attack
        self.health = health

    def attack(self, enemy):
        attack_text = self._attack.do_attack(enemy)
        print(f'{self.name} {attack_text}')

class attack():
    def __init__(self, damage, attack_str):
        self.damage = damage
        self.attack_str = attack_str

    def do_attack(self, enemy):
        d = self.damage()
        enemy.health = enemy.health - d
        return f'{self.attack_str} doing {d} points of damage'

def _1d4():
    return random.choice(range(1,4))

def _1d12():
    return random.choice(range(1,12))

def _nDx(n, x):
    pass

def fetch_enemy():
    return entity('Goblin', attack(_1d4, 'swings club'), 15)

if __name__ == '__main__':
    player = entity('Kazagha', attack(_1d12,'swings sword'), 100)
    enemy = fetch_enemy()

    while(player.health > 0 and enemy.health > 0):
        print(f'{player.name} is at {player.health} points of health')

        player.attack(enemy)
        enemy.attack(player)