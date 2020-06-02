from Character import Character

class Zombie(Character):
    '''Ärver från klassen Character'''

    def __init__(self, damage, *args, **kwargs):
        '''Sätter de attribut som ärvts från Character samt eget attribut "damage".'''

        self.damage = damage
        super().__init__(*args, **kwargs)