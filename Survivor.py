from Character import Character
from Weapon import Weapon

class Survivor(Character):
    '''Ärver attribut från Character'''

    def __init__(self, weapon:Weapon, *args, **kwargs):
        '''
        Sätter attributen som ärvts av Character men också chosen_weapon som är av klassen Weapon. 
        Sparar alla weapon i en lista.
        Kör default_weapons() som skapar objekt av klassen Weapon
        '''

        self.chosen_weapon = weapon
        super().__init__(*args, **kwargs)
        self.all_weapons = []
        self.default_weapons()

    def default_weapons(self):
        '''Skapar objekt av klassen Weapon'''

        knife = Weapon("Knife", 11)
        self.all_weapons.append(knife)

        gun = Weapon("Gun", 12)
        self.all_weapons.append(gun)

        screwdriver = Weapon("Screwdriver", 7)
        self.all_weapons.append(screwdriver)

        broomstick = Weapon("Broomstick", 9)
        self.all_weapons.append(broomstick)

    def list_weapons(self):
        '''Listar alla weapon som finns i listan all_weapons'''

        for weapon in self.all_weapons:
            print(weapon)

    def choose_weapon(self, weapon):
        '''Sätter chosen_weapon genom att jämföra "weapon" och w.name, finns det inte i listan returneras "" istället'''

        for w in self.all_weapons:
            if w.name == weapon:
                self.chosen_weapon = w
                return w
        return " "




