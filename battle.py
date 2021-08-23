import random
gn = input('guide name? ')
atac = random.randint(1, 5)


opponent_hp = 50
spells = ['ultimate', 'saving', 'gigalish']
atac = [1, 2, 3, 4, 5]
defend = [1, 2, 3]
battle_tech = input(f"Attack? or defend or spell book? ")
if battle_tech == 'atk' or 'attack':
    atac = random.choice(atac)
    if atac == 1:

        opponent_hp == opponent_hp - 1
        print(f"{gn}: You did 1 damage! ")
    elif atac == 2:
        opponent_hp == opponent_hp - 2
        print(f'{gn}: You did 2 damage! ')
    elif atac == 3:
        opponent_hp = opponent_hp - 3
        print(f"{gn}: You did 3 damage! ")
    elif atac == 4:
        opponent_hp = opponent_hp - 4
        print(f'{gn}: You did 4 damage! ')
    elif atac == 5:
        opponent_hp = opponent_hp - 5
        print(f'{gn}: You did 5 damagde! ')


