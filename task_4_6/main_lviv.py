import Lab_gamewanderer.task_4_6.game_lviv as game_lviv

finished = False

#set street
kozelnytska = game_lviv.Street("Вулиця Козельницька")
kozelnytska.set_description('Тиха, спокійна вулиця. Колегіум УКУ  поряд - не забудь попередити куратора')
stryiska = game_lviv.Street("Stryiska")
stryiska.set_description("Ніхто не знає, що тут робиться. Будь обережний")
franka = game_lviv.Street("Ivana Franka")
franka.set_description("До центру вже не так далеко, можеш поки насолодитись видами")
shevchenka = game_lviv.Street('Shevchenka')
shevchenka.set_description('Десь біля памʼятника грає "Місто весни". Краса...')
krakiv = game_lviv.Street('Krakivska', False)
krakiv.set_description("Шотів тут вже і немає... потрібно знайти інше місце, щоб випити")


kozelnytska.link_street(stryiska, "north")
stryiska.link_street(shevchenka, "north")
stryiska.link_street(kozelnytska, 'south')
shevchenka.link_street(krakiv, "north")
shevchenka.link_street(stryiska, 'south')
krakiv.link_street(shevchenka, "south")

#set character and enemy
knave = game_lviv.Enemy("Лотр", "Старий грабіжник з обідраним одягом", 5, 2)
knave.set_conversation("Зупинись і віддай мені свої гроші")
knave.set_bad_speach("Ви не змогли захиститись. Лотр забрав ваші гроші")
knave.set_good_speech("Лотр злякався і втік")
knave.set_weakness(["перцовий балончик", "ніж"])
stryiska.set_character(knave)

students = game_lviv.Character("Група студентів", "Юні аспірантки, що набухують бандитів", True)
students.set_conversation("Хей, друже, хочеш пива?")
students.set_choose({'Ні': ["Ти шо нас не поважаєш? Вон звідси", False], "Так": ["Дуже добре, тримай своє пиво", True]})
shevchenka.set_character(students)

cavalier = game_lviv.Character("Кавалер", "Хіпстер схожий на Дієґо Марадону")
cavalier.set_conversation(["Вельмишановний, знайдеться цигарка?"])

pepper_spray = game_lviv.Weapon("pepper spray", 3)
pepper_spray.set_description('Перцовий балончик, краще тримати біля себе')
kozelnytska.set_item(pepper_spray)

money = game_lviv.Support("money")
money.set_description("Трохи готівки, десь на одну прогулянку")
kozelnytska.set_item(money)

ciggarates = game_lviv.Support("ciggarates")
ciggarates.set_description("Chapmans вишневі")
kozelnytska.set_item(ciggarates)

bear = game_lviv.Item('bear')
bear.set_description('Львівське не різдвяне')
students.set_item(bear)

current_str = kozelnytska
backpack = []

def action(backpack, inhabitant):
                # Fight with the inhabitant, if there is one
            
            if inhabitant.action:
                backpack = inhabitant.action_char(backpack)
                current_str.character = None
                return False, current_str, backpack

            # Do I have this item?
            if not backpack:
                print('У тебе немає чим битись(')
                inhabitant.bad_talk()
                current_str.character = None
                return False, current_str, backpack
            print("What will you fight with?")
            print(f'Item in your backpack - {backpack}')
            fight_with = input()
            if fight_with in backpack:

                if inhabitant.fight(fight_with) == True:
                    # What happens if you win?
                    print("Hooray, you won the fight!")
                    current_str.character = None
                    inhabitant.good_talk
                    return False, current_str, backpack
                else:
                    # What happens if you lose?
                    print("Oh dear, you lost the fight.")
                    print("You are in hospital. That's the end of the game")
                    inhabitant.bad_talk
                    return True, current_str, backpack
            else:
                print("You don't have a " + fight_with)
        


#set items

while finished == False:

    print("\n")
    current_str.get_details()

    inhabitant = current_str.get_character()
    if inhabitant is not None and inhabitant.trigered():
        inhabitant.describe()
        inhabitant.talk()
        finished, current_str, backpack = action(backpack, inhabitant)
        continue
    elif inhabitant is not None:
        inhabitant.describe()

    items, items_name = current_str.get_item()
    if items:
        for item in items: 
            item.describe()

    command = input("> ")

    if command in ["north", "south", "east", "west"]:
        # Move in the given direction
        current_str = current_str.move(command)
    elif command == "talk":
        # Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "fight":
        if inhabitant is not None:
            action(backpack, inhabitant)
        else:
            print("There is no one here to fight with")
    elif command == "take":
        if items:
            print(f'Що саме ви хочете взяти? (можливий вибір {items})')
            item = input()
            if item in items_name:
                print("You put the " + item + " in your backpack")
                items_name.remove(item)
                backpack.append(item)
                current_str.update_items(items_name)
            else:
                print('There is no item you name   ')
        else:
            print("There's nothing here to take!")
    else:
        print("I don't know how to " + command)