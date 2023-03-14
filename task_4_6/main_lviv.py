import game_lviv

finished = False

#set street
kozelnytska = game_lviv.Street("Вулиця Козельницька",['north', 'take', 'talk', 'fight'])
kozelnytska.set_description('Тиха, спокійна вулиця. Колегіум УКУ  поряд не забудь взяти речі')
stryiska = game_lviv.Street("Вулиця Стрийська", ['north', 'south', 'take', 'talk', 'fight'])
stryiska.set_description("Ніхто не знає, що тут робиться. Будь обережний")
franka = game_lviv.Street("Вулиця Івана Франка", ['north', 'south', 'take', 'talk', 'fight'])
franka.set_description("До центру вже не так далеко, можеш поки насолодитись видами")
shevchenka = game_lviv.Street('Проспект Шевченка', ['north', 'south', 'take', 'talk', 'fight'])
shevchenka.set_description('Десь біля памʼятника грає "Місто весни". Краса...')
rynok = game_lviv.Street('Площа Ринок', ['south', 'take', 'talk', 'fight'])
rynok.set_description("Гарне місце для побачень, але трохи людно")
rynok.change_trigered()

kozelnytska.link_street(stryiska, "north")
stryiska.link_street(franka, "north")
stryiska.link_street(kozelnytska, 'south')
franka.link_street(shevchenka, 'north')
franka.link_street(stryiska, 'south')
shevchenka.link_street(rynok, "north")
shevchenka.link_street(franka, 'south')
rynok.link_street(shevchenka, "south")

#set character and enemy
knave = game_lviv.Enemy("Лотр", "Старий грабіжник з обідраним одягом", trigered= True, item = "money")
knave.set_conversation("Зупинись і віддай мені свої гроші")
knave.set_bad_speach("Ви не змогли захиститись. Лотр забрав ваші гроші")
knave.set_good_speech("Лотр злякався і втік")
knave.set_weakness(["pepper spray", "knife"])
stryiska.set_character(knave)

students = game_lviv.Character("Група студентів", "Юні аспірантки, що набухують бандитів", action = True)
students.set_conversation("Хей, друже, хочеш пива?")
students.set_choose({'No': ["Ти шо нас не поважаєш? Вон звідси", False], "Yes": ["Дуже добре, тримай своє пиво", True]})
franka.set_character(students)

cavalier = game_lviv.Character("Кавалер", "Хіпстер схожий на Дієґо Марадону", action = True)
cavalier.set_requered('ciggarates')
cavalier.set_conversation("Вельмишановний, знайдеться цигарка?")
cavalier.set_choose({'No': ["Дуже й дуже сумно", False, False], "Yes": ["Ох нічого собі, що ви курите. Тримайте сотку, для вас не шкода", True, True]})
shevchenka.set_character(cavalier)

girl = game_lviv.Character('Анастасія',"Дівчина, з якою ви йдете на побачення", action = True, trigered = True)
girl.set_requered('money')
girl.set_item('Симпатію')
girl.set_conversation("Ох ти прийшов майже без запізнення, ходімо тоді на каву\n[Ви гарно посіділи і прийшла черга оплачувати замовлення]\n\
Ти ж заплатиш?"
)
girl.set_choose({'No': ["Яке жахіття, привів на каву і не заплатить навіть.\
 Більше з тобою ніколи, нікуди не піду\n\nПобачення провалено, ви програли", False, False],\
 "Yes": ["Чудово, можливо сходимо і на вихідних прогуляти?\n\nПобачення успішно завершено. Ви виграли!", True, False]})
rynok.set_character(girl)
#set items

knife = game_lviv.Weapon("knife", 5)
knife.set_description("Ніж подарований батьком")
kozelnytska.set_item(knife)


pepper_spray = game_lviv.Weapon("pepper spray", 3)
pepper_spray.set_description('Перцовий балончик, краще тримати біля себе')
kozelnytska.set_item(pepper_spray)

money = game_lviv.Support("money")
money.set_description("Трохи готівки, десь на одну прогулянку")
kozelnytska.set_item(money)
cavalier.set_item(money)

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
                return current_str, backpack

            # Do I have this item?
            if not backpack:
                print('У тебе немає чим битись(')
                inhabitant.bad_talk()
                current_str.character = None
                if inhabitant.steal and inhabitant.steal in backpack:
                    backpack.remove(inhabitant.steal)
                return current_str, backpack
            
            while True:
                print("What will you fight with?")
                print(f'Item in your backpack - {backpack}')
                fight_with = input()
                if fight_with in backpack:

                    if inhabitant.fight(fight_with) == True:
                        # What happens if you win?
                        print("Hooray, you won the fight!")
                        current_str.character = None
                        inhabitant.good_talk()
                        return current_str, backpack
                    else:
                        # What happens if you lose?
                        print("Oh dear, you lost the fight.")
                        current_str.character = None
                        inhabitant.bad_talk()
                        if inhabitant.steal and inhabitant.steal in backpack:
                            print(f'You lose {inhabitant.steal}')
                            backpack.remove(inhabitant.steal)
                        return current_str, backpack
                else:
                    print("You don't have a " + fight_with)
        

print("Вітаю у типовій грі-блукалці. Твоє завдання, щоб виграти сходити вдало на побачення з дівчиною")
print("усі можливі ходи тобі підкажуть. Нехай щастить")
while finished == False:
    finished = current_str.trigered
    print("\n")
    current_str.get_details()

    inhabitant = current_str.get_character()

    if inhabitant is not None and inhabitant.trigered:
        inhabitant.describe()
        current_str, backpack = action(backpack, inhabitant)
        continue
    elif inhabitant is not None:
        inhabitant.describe()

    items, items_name = current_str.get_item()
    if items:
        for item in items: 
            item.describe()
    print(f'Твій рюкзак - {backpack}')
    print(f'Можливі ходи - {current_str.action}')
    command = input("> ")

    if command in ["north", "south", "east", "west"]:
        # Move in the given direction
        current_str = current_str.move(command)
    elif command == "talk":
        # Talk to the inhabitant - check whether there is one!
        
        if inhabitant is not None:
            if inhabitant.action:
                backpack = inhabitant.action_char(backpack)
                current_str.character = None
            else:
                inhabitant.talk()
        else:
            print('There is no one to talk with')
    elif command == "fight":
        if inhabitant is not None and isinstance(inhabitant, game_lviv.Enemy):
            finished, current_str, backpack = action(backpack, inhabitant)
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
