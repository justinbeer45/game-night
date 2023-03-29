import time

def welcome():
    print("\nWelcome. Let's decide if we will play tonight's game again.\n")


def get_game_name():
    blank = True
    while blank:
        game = input("What was tonight's game:")
        if game != '':
            blank = False
            continue
        print("\tYou will need to enter a name.\n")
        time.sleep(1)


if __name__ == '__main__':
    welcome()
    get_game_name()
