class Character:

    def __init__(self, name, strength, weakness, health_bar):
        '''Sätter namn, strycka, svaghet och liv för en karaktär'''
        
        self.name = name
        self.strength = strength
        self.weakness = weakness
        self.health_bar = health_bar

    def __str__(self):
        '''Returnerar en läsbar sträng av en Character'''

        return "{}".format(self.name)