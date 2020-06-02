from Survivor import Survivor
from Zombie import Zombie
import random

class Character_Collection:
    '''Ansvarar för Survivor och Zombie'''

    def __init__(self):
        '''Håller alla Survivor och Zombie i varsin lista. Kör metoderna default_survivors och default_enemies där förutbestämda karaktärer skapas'''

        self.survivor = []
        self.enemy = []
        self.default_survivors()
        self.default_enemies()

    def add_survivor_list(self, survivor):
        '''Lägger till en Survivor i listan'''

        self.survivor.append(survivor)
    
    def add_enemy_list(self, enemy):
        '''Lägger till en Enemy i listan'''

        self.enemy.append(enemy)

    def create_survivor(self, *args, **kwargs):
        '''Skapar Survivor'''

        return Survivor(*args, **kwargs)

    def create_enemy(self, *args, **kwargs):
        '''Skapar Zombie(enemy)'''

        return Zombie(*args, **kwargs)

    def default_survivors(self):
        '''Skapar Survivor och lägger till de i en listan'''

        s1 = self.create_survivor(None, "Kenny", "Water", "Bad eyes", 88)
        self.survivor.append(s1)

        s2 = self.create_survivor(None, "Morgan", "Stick", "Crazy", 76)
        self.survivor.append(s2)
        
        s3 = self.create_survivor(None, "Rick", "Police", "Children", 92)
        self.survivor.append(s3)

        s4 = self.create_survivor(None, "Andrea", "Woman", "Too good", 90)
        self.survivor.append(s4)

        s5 = self.create_survivor(None, "Michone", "Strong", "Rick", 95)
        self.survivor.append(s5)

    def default_enemies(self):
        '''Skapar Zombie(enemy) och lägger till de i en listan'''

        e1 = self.create_enemy(10, "Water Zombie", "Stealth", "Slow", 88)
        self.enemy.append(e1)

        e2 = self.create_enemy(5, "Only head Zombie", "Stealth", "Slow", 88)
        self.enemy.append(e2)

        e3 = self.create_enemy(7, "SWAT-helmet wearing Zombie", "Helmet", "Can't bite", 54)
        self.enemy.append(e3)

        e4 = self.create_enemy(14, "No teeth Zombie", "Scratching", "Can't bite", 60)
        self.enemy.append(e4)

        e5 = self.create_enemy(12, "Child Zombie", "Cute", "Small", 55)
        self.enemy.append(e5)

    def get_survivor(self, name):
        '''Hämtar en Survivor i listan om den stämmer överens med "name" '''

        for survivor in self.survivor:
            if survivor.name == name:
                return survivor

    def get_enemy(self):
        '''Hämtar en slumpmässig Zombie i listan enemy (som innehåller alla zombies'''

        return random.choice(self.enemy)

