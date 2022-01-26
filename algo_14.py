import random

door = ['goat', 'auto']

def choose_doors(choices):
    choice = random.choice(choices)
    print('you did your choice ')
    option = input('one of the door revealed,  and it is not prize door'
                   'do you want to change your mind')
    if option == 'n':
        if choice == 'auto':
            print(f'your choice was {choice}')
            print('you win auto')
        elif choice == 'goat':
            print(f'your choice was {choice}')
            print('you loose, it is not prize door')

        elif option == 'y':
            print(f'your original choice was {choice}')
        if choice == 'goat':
            choice = 'auto'
            print(f'your new choice {choice}')
            print('you win the auto')
        elif choice == 'auto':
            choice = 'goat'
            print(f'your new choice {choice}')
            print('you loooooooose!!')





