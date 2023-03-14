"""Module of game classes"""

class Street:
    trigered = True
    def __init__(self, name, action = []):
        self.item = None
        self.character = None
        self.name = name
        self.direction = {}
        self.items_name = []
        self.items = []
        self.action = action
        self.trigered = False

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
        self.trigered = Street.trigered
    
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


    def __init__(self, name, description, action = False, trigered = False):
        self.name = name
        self.description = description
        self.action = action
        self.trigered = trigered

    def set_choose(self, dct):
        self.choose = dct

    def set_requered(self, item):
        self.requered = item

    def action_char(self, backpack):
        self.talk()
        while True:
            print(f"You can choose between {[i for i in self.choose]}")
            your_choose = input()
            if your_choose in self.choose:
                if self.choose[your_choose][1] and not self.requered in backpack:
                    print(f'У вас немає {self.requered} в рюкзаку')
                    your_choose = 'No'
                print(f"[{self.name} says]: {self.choose[your_choose][0]}")
                if self.choose[your_choose][2]:
                    print(f"Ви отримали {self.item}")
                    if self.item not in backpack:
                        backpack.append(self.item.name)
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
    def __init__(self, name, description, action = False, trigered = False, item = None, health = 0, damage = 0):
        super().__init__(name, description, action, trigered)
        self.damage = damage
        self.health = health
        self.steal = item
    
    def fight(self, item):
        if item in self.weakness:
            return True
        return False

if __name__ == '__main__':
    cls = Enemy('da', 'dawdw')
    print(isinstance(cls, Enemy))