from Player import Player
from Character_Collection import Character_Collection
from Statistics import Statistics
import random
import time

class Game:
    '''Huvudklassen för programmet som användaren interagerar med. Ansvarar för Player, Character_Collection och Statistics'''

    def __init__(self):
        '''Välkomnar användaren och skapar sedan Character_Collection, Player och Statistics. Sätter även en enemy(Zombie). Kör sedan menyn'''
        
        self.welcome()
        self.characters = Character_Collection()
        self.player = self.create_player()
        self.enemy = self.characters.get_enemy()
        self.statistic = Statistics(0, 0)
        self.menu()

    def create_player(self):
        '''Skapar en Player, där användaren måste skriva in namn samt välja en Character(Survivor).'''

        while True:
            name = input("Vad heter du? ")

            if name == "" or name == " ":
                print("Skriv in ett namn är du snäll!")

            else:
                break

        while True:
            print("\n*** Välj karaktär ***")
            self.list_survivors()
            character = input("\nAnge karaktär: ").capitalize()
            survivor = self.characters.get_survivor(character)

            if type(survivor) is str:
                print("Karaktären finns inte!")

            else:
                break

        return Player(name, survivor)

    def list_survivors(self):
        '''Listar alla Survivor som finns i Character_Collection'''
        
        for survivor in self.characters.survivor:
            print('- {}'.format(survivor.name))

    def welcome(self):
        '''Välkomnar användaren'''
        
        print("-" *40)
        print("Welcome to Zombie Fight")
        print("-" *40)

    def print_menu(self):
        '''Skriver ut menyn'''
        
        print("\n" + "*" *17 + " MENY " + "*" *17)
        print("1) Spela")
        print("2) Byt karaktär")
        print("3) Visa spelarinfo")
        print("0) Avsluta")
        print("*" *40)

    def menu(self):
        '''Hanterar menyn och användarens val'''

        wrong_alternative = [
            "Hoppsan, du valde ett felaktigt alternativ!",
            "Nämen, det blev inte riktigt rätt nu.",
            "Kom igen, finns det alternativet verkligen i listan ovan?",
            "Ange ett giltigt alternativ!"
        ]

        while True:
            self.print_menu()
            choice = input("Val: ")

            if choice == "1":
                self.play_game()

            elif choice == "2":
                self.change_character()

            elif choice == "3":
                self.show_player_info()

            elif choice == "0":
                break

            else:
                print(random.choice(wrong_alternative))

        print("Tack för denna gång!")

    def play_game(self):
        '''
        Spelet körs. 
        Användaren får välja vapen, vapnet har damage som minskar health_bar på Zombie. 
        Zombie har damage som minskar health_bar på Survivor.
        Statistik hålls och noteras om det blev förlust eller vinst.
        Enemy (Zombie) byts ut efter matchen är slut.
        '''
        
        survivor = self.player.chosen_character
        survivor_hp = survivor.health_bar

        enemy = self.enemy
        enemy_hp = self.enemy.health_bar

        print("********** FIGHT **********")
        print("{} ({}) -VS- {}\n".format(survivor.name, self.player.name, enemy.name))

        while True:
            print("*"*6 + " CHOSE WEAPON " + "*"*6)
            self.player.chosen_character.list_weapons()
            choose_weapon = input("Välj ditt vapen: ").capitalize()
            weapon = self.player.chosen_character.choose_weapon(choose_weapon)

            if type(weapon) is str:
                print("Inte ett giltigt alternativ")
            
            else:
                break
        
        survivor_weapon = self.player.chosen_character.chosen_weapon

        whose_turn = random.randint(1,2)
        if whose_turn % 2 == 0:
            print("Du börjar!")

        else:
            print("{} börjar".format(enemy.name))


        while survivor_hp > 0 and enemy_hp > 0:
            print("*"*5 + "STATUS" + "*"*5)
            print("Namn: {} ({})\nHP: {}\n----------\nNamn: {}\nHP: {}".format(survivor.name, self.player.name, survivor_hp, enemy.name, enemy_hp))
            print("*"*16 + "\n")
            time.sleep(0.8)

            if whose_turn % 2 == 0:
                current_attack = int(survivor_weapon.damage * random.uniform(0.5, 1.5))
                
                if enemy.weakness == "Slow":
                    current_attack = int(current_attack * 1)

                elif enemy.weakness == "Can't bite":
                    current_attack = int(current_attack * 1.2)

                elif enemy.weakness == "Small":
                    current_attack = int(current_attack * 1)

                print("Du attackerar: {}\n".format(current_attack))
                enemy_hp = (enemy_hp-current_attack)
            
            else:
                enemy_attack = int(enemy.damage * random.uniform(0.5, 1.5))

                if survivor.weakness == "Bad eyes" and enemy.strength == "Stealth":
                    enemy_attack = int(enemy_attack * 1.10)

                elif survivor.weakness == "Crazy" and enemy.strength == "Helmet":
                    enemy_attack = int(enemy_attack * 1.25)

                elif survivor.weakness == "Children" and enemy.strength == "Cute":
                    enemy_attack = int(enemy_attack * 1.5)

                elif survivor.weakness == "Too good" and enemy.strength == "Scratching":
                    enemy_attack = int(enemy_attack * 1.05)

                elif survivor.weakness == "Rick" and enemy.strength == "Stealth":
                    enemy_attack = int(enemy_attack * 1)

                print("Fienden attackerar: {}\n".format(enemy_attack))
                survivor_hp = (survivor_hp-enemy_attack)

            whose_turn += 1

        winning = [
            "You're a real survivor!",
            "No Zombie can take you!",
            "Good job!"
        ]

        losing = [
            "Oh no, you got bit!",
            "Eaten by zombies...",
            "R.I.P"
        ]

        if survivor_hp > 0:
            print("Survivor wins!")
            print(random.choice(winning))

            self.statistic.wins += 1

        else:
            print("Zombie wins!")
            print(random.choice(losing))

            self.statistic.loses += 1

        self.enemy = self.characters.get_enemy()
        
    def change_character(self):
        '''Användaren kan välja att byta karaktär'''

        while True:
            print("*** Byt karaktär ***")
            self.list_survivors()
            character = input("Ange karaktär: ").capitalize()
            survivor = self.characters.get_survivor(character)

            if type(survivor) is str:
                print("Karaktären finns inte")

            else:
                break
        
        self.player.chosen_character = survivor

    def show_player_info(self):
        '''Visar användarens (Player) namn och vald karaktär, samt statistik över antal vinster och förluster'''

        print("\n***** SPELARINFO *****")
        print("Spelarnamn: {} \nKaraktär: {}\n".format(self.player.name, self.player.chosen_character))
        print("Vinster: {} \nFörluster: {}".format(self.statistic.wins, self.statistic.loses))


Game()
