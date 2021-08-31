import time
import sys
from random import randint
chance = randint(1, 5)
def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1/10)


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
traveling = True
while traveling == True:

    slowprint("you are going to the grasslands, through there you can go to the hell gate to fight the God Of Plants")
    traveling = False
    fight = True
    while fight == True:
        print("You have arrived in the Grasslands and spotted the God Of Plants, you go into battle thinking you can easily defeat him, you are so wrong.")
        choose = input('Will you move to the right, left, forwards or backwards? ')
        if choose == 'left':
            print("you moved left and the God Predicted your move and killed you ")
            print("Game will end now.")
            exit()
        elif choose == 'right':
                print("you rolled to the right and tripped on your sword during it, you were spotted by the God and killed")
                print('The game will end now.')
                exit()
        elif choose == 'backwards':
                print("You backflipped backwards but that was a simple move and you were smited into nothingness.")
                print('The game will end now')
                exit()
        elif choose == 'forwards':
                print("You leaped backwards and attacked the god, it was unpredictable and stupid but you pulled it off *clap clap*.")
                run = input('The God is on half health, will you attack him or try running away? ')
        if run == 'Run' or 'run' or 'run away':
                print('calculating your chance to escape now....')
                if chance >= 3:
                    print('You ran away and are now going to die lonely')
                    fight = False
                elif chance <= 2:
                    print('You could not run away, you will fight through the god')
                    combat = input("will you attack him from right or left? ")
                    if combat == 'left':
                        print('You beat him, go you!')
                        fight = False
                    elif combat == 'right':
                        print('you have died')
                        print('the game will end now')
                        exit()
                elif run == 'fight' or 'attack':
                    combat = input("will you attack him from right or left? ")
                    if combat == 'left':
                            print('You beat him, go you!')
                            fight = False
                            print('you will live in peace alone now')
                            exit()
                    elif combat == 'right':
                            print('you have died')
                            print('the game will end now')
                            exit()




    else:
        traveling = True

















