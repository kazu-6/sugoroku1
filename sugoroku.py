import random

num_masu = 30
num_player = 1


def main():
    print('双六をはじめますか？y/n')
    init = input('>>')
    location = 0
    if init == 'y':
        for turn in range(1, 30):
            print( '今は' + str(turn) + 'ターンです。' )
            num_dice = random.randint(1, 6)
            print('サイコロの目は' + str(num_dice) + 'です')
            location += num_dice
            print('ゴールまであと' + str(num_masu - location) + 'マスです。')
            if location >= 30:
                break
        print('ゴールです！')

    elif init == 'n':
        print('またね！')

    else:
        main()



if __name__ == '__main__':
    main()
