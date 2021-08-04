import time
Start = input('Would you like to start the adventure? Yes Or No ')
if Start == 'yes'.lower():
    Name = input('What shall thou name be? ')
    print(f'Greeting adventurer {Name}, thou adventure shall start now.')
    time.sleep(2)
    print('Ahh, welcome adventurer, what is your name? ')
    time.sleep(2)
    print(f'Uhhh, my name is {Name}')
    nick = input(f'Do you want me to call you {Name} Or call you something else? Say 1 or 2 ')
    if nick == '1':
        nk = print('So i shall call you that')
        nickname = Name
        print(f'{nickname}, i like that')


    elif nick == '2':
        nn = input('What shall i call you then? ')
        nickname = nn










