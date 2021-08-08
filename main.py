import time
import pickle
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
        nk = print('???: So i shall call you that')
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











