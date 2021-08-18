import time
#stats
health = (100)
atk = (5)
defense = (5)
mana = (50)
import random
atkchoose = ['Swordsmen', 'musketeer', 'beserker']
defchoose = ['backup', 'tanker', 'sheilder']
manachoose =['mage', 'sage', 'elementalist']
healthchoose = ['healer', 'priest', 'lifestealer']


Start = input('Would you like to start the adventure? Yes Or No ')
if Start == 'yes'.lower():
    Name = input('What shall thou name be? ')
    print(f'Greeting adventurer {Name}, thou adventure shall start now.')
    time.sleep(2)
    print('???: Ahh, welcome adventurer, what is your name? ')
    time.sleep(2)
    print(f'{Name}: Uhhh, my name is {Name}')
    time.sleep(2)
    nick = input(f'???: Do you want me to call you {Name} Or call you something else? Say 1 or 2 ')
    if nick == '1':
        print('???: So i shall call you that')
        nickname = Name
        print(f'{nickname}, i like that')


    elif nick == '2':
        nn = input('What shall i call you then? ')
        nickname = nn
time.sleep(2)
travel = input(f'???: Ok {nickname}, now i know what to call you, are you heading to Vortex? ')
if travel == 'Yes'.lower():
    print('Alright, ill take you there, when we get there we will have to meet the cardinal.')
else:
    answer1 = input('???: Are you sure? ')
    if answer1 == 'Yes'.lower():
        print('ill take you there anyway.')

time.sleep(5)
print("two days later.....")
time.sleep(2)
print('???: We are here, Vortex City, The home town of all people born')
time.sleep(3)
print(f"Alright {nickname}, lets go to the cardinal at the castle of cardinals")
time.sleep(3)
print(f"{nickname}: Before we go, what's your name? ")
time.sleep(3)
gn = input(f"???: My name? My Name Is....")
time.sleep(1)
print(f"{gn}: Thats right, my name is {gn}.")
print("Area: The Castle Of Cardinals, Vortex City")
print(f"{gn}: We are here {nickname}, to the castle, the castle of the cardinals before, now and future.")
ready = input('Are you ready? ')
if ready == 'yes':
    print(f'{gn}: Alright, Lets go')
else:
    print(f"{gn}: im anonoying so i take you there anyways mate")
time.sleep(3)
print('At the castle of the cardinals...')
time.sleep(2)
print(f'{gn}: hello cardinal, it is i {gn}, and i have brought you a new volunteer to do the mission')
time.sleep(2)
print(f'{nickname}: Wait what, i didnt volunteer for this, this is ubsurd, i trusted you {gn}.')
time.sleep(2)
print(f'???: Hush boy, Let me speak...')
time.sleep(2)
print(f'{nickname}: uhhh ok, sorry mr.cardinal')
time.sleep(2)
print(f'???: Now, thou speak {gn}.')
time.sleep(2)
quest = input(f'{gn}: I have brought this youth to do this adventure quest, will he accept? ')
if quest == 'yes' or 'ye' or 'yuh':
    print(f'???: Ok {nickname}, thou has chosen to pursue this quest, do so with respect')
    time.sleep(2)
    print(f'???: here are your stats child: Health: {health}, Attack: {atk}, Defense: {defense}, Mana(magic): {mana} ')
    prominant = input(f'Now i ask you what will be your most prominant stat? Remember this, your answer will decide your class, choose carefully: ')
    if prominant == 'atk' or 'attack':
        atk = atk + 50
        classs = 'swordsmen'
        print(f'Now you will be a , and your most prominant stat will be attack which is now {atk}.')













