class Weapon:

    def __init__(self, name, damage):
        '''Sätter namn och damage'''

        self.name = name
        self.damage = damage

    def __str__(self):
        '''Returnerar en läsbar sträng för objekt i Weapon'''

        return "- {}".format(self.name)

