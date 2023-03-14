"""Module of game classes"""

class Street:

    trigered = True

    def __init__(self, name, trigered = False):
        self.item = None
        self.character = None
        self.name = name
        self.direction = {}
        self.items_name = []
        self.items = []
        self.trigered = trigered

    def __repr__(self):
        return self.name
    
    def set_description(self, description):
        self.description = description
    
    def link_street(self, room, direction):
        self.direction[direction] = room

    def set_character(self, character = None):
        self.character = character

    def set_item(self, item = None):
        self.items_name.append(item.name)
        self.items.append(item)

    def get_character(self):
        return self.character
    
    def get_item(self):
        return self.items, self.items_name
    
    def move(self, way):
        return self.direction[way]

    def change_trigered(self):
        Street.trigered = self.trigered
    
    def get_details(self):
        print(f'{self.name}')
        print('--------------------')
        print(f'{self.description}')
        for key, value in self.direction.items():
            print(f'The {value} is {key}')

    def update_items(self, items):
        self.items_name = items
        self.items = [i for i in self.items if i.name in self.items_name ]

class Character:


    def __init__(self, name, description, action = False):
        self.name = name
        self.description = description
        self.action = action

    def set_choose(self, dct):
        self.choose = dct

    def action_char(self, backpack):
        while True:
            print(f"You can choose between {[i for i in self.choose]}")
            your_choose = input()
            if your_choose in self.choose:
                print(f"[{self.name} says]: {self.choose[your_choose][0]}")
                if self.choose[your_choose][1]:
                    print(f"Ви отримали {self.item}")
                    backpack.append(self.item)
                return backpack
            else:
                print('Ви не можете це вибрати. Спробуйте ще раз')

    def set_conversation(self, speech):
        self.speech = speech

    def set_good_speech(self, speech):
        self.good_speech = speech
    
    def set_bad_speach(self, speech):
        self.bad_speech = speech
    
    def set_weakness(self, item):
        self.weakness = item

    def describe(self):
        print(f'{self.name} is here!')
        print(self.description)
    
    def set_item(self, item):
        self.item = item

    def trigered(self):
        return Street.trigered

    def talk(self):
        print(f"[{self.name} says]: {self.speech}")
    
    def bad_talk(self):
        print(f"[{self.name} says]: {self.bad_speech}")

    def good_talk(self):
        print(f"[{self.name} says]: {self.good_speech}")
    
class Item:
    def __init__(self, name):
        self.name = name

    def set_description(self, description):
        self.description = description

    def describe(self):
        print(f'The [{self.name}] is here - {self.description}')

    def __repr__(self) -> str:
        return f"'{self.name}'"

    def get_name(self):
        return self.name
    
class Weapon(Item):

    def __init__(self, name, damage):
        super().__init__(name)
        self.damage = damage

class Support(Item):

    def __init__(self, name, damage_boost = None, health_boost = None):
        super().__init__(name)
        self.dam_boost = damage_boost
        self.health_boost = health_boost

class Enemy(Character):
    def __init__(self, name, description, health, damage):
        super().__init__(name, description)
        self.damage = damage
        self.health = health
