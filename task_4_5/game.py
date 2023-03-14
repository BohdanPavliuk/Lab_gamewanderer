"""Module of game classes"""

class Room:

    def __init__(self, name):
        self.item = None
        self.character = None
        self.name = name
        self.direction = {}

    def __repr__(self):
        return self.name
    
    def set_description(self, description):
        self.description = description
    
    def link_room(self, room, direction):
        self.direction[direction] = room

    def set_character(self, character = None):
        self.character = character

    def set_item(self, item = None):
        self.item = item

    def get_character(self):
        return self.character
    
    def get_item(self):
        return self.item
    
    def move(self, way):
        return self.direction[way]
    
    def get_details(self):
        print(f'{self.name}')
        print('--------------------')
        print(f'{self.description}')
        for key, value in self.direction.items():
            print(f'The {value} is {key}')


class Enemy:
    defeated = 0

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def set_conversation(self, speech):
        self.speech = speech
    
    def set_weakness(self, item):
        self.weakness = item

    def describe(self):
        print(self.description)

    def talk(self):
        print(f"[{self.name} says]: {self.speech}")

    def fight(self, item):
        if self.weakness == item:
            Enemy.defeated += 1
            return True
        return False
    
    def get_defeated(self):
        return self.defeated
    
class Item:
    def __init__(self, name):
        self.name = name

    def set_description(self, description):
        self.description = description

    def describe(self):
        print(f'The [{self.name}] is here - {self.description}')

    def get_name(self):
        return self.name

