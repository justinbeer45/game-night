import time
from enum import Enum

game = None
choices = {}


class ThreeAmigos(Enum):
    MASON = "Mason"
    VALARIE = "Valarie"
    JUSTIN = "Justin"


class InvalidNameException(Exception):
    """Raised when user input is not Mason, Valarie, or Justin."""
    pass


class InvalidVoteException(Exception):
    """Raised when user vote is not clearly affirmative or negative"""
    pass


def welcome():
    print("\nWelcome. Let's decide if we will play tonight's game again.\n")


def get_game_name():
    blank = True
    while blank:
        global game
        game = input("What was tonight's game:")
        if game != '':
            blank = False
            continue
        print("\tYou will need to enter a name.\n")
        time.sleep(1)


def get_name_and_vote():
    user_name = None
    for amigo in ThreeAmigos:
        print(amigo.value)
    incorrect_name = True
    while incorrect_name:
        user_name = input("Who are you?")
        try:
            test_user_name(user_name)
        except InvalidNameException:
            print("\tThat is not one of the names.")
            time.sleep(1)
        else:
            incorrect_name = False
            # print("\nWelcome, {}.".format(user.title()))
            user_name = ThreeAmigos[user_name.upper()]
    invalid_vote = True
    while invalid_vote:
        voter_choice = input("{}, would you like to play {} again next week?".format(user_name.value, game))
        try:
            yn = test_user_vote(voter_choice)
        except InvalidVoteException:
            print("\tI'm sorry, I'm not sure what you mean.")
            print("\tWould you like to play {} again next week, YES or NO?".format(game))
        else:
            global choices
            choices.update({user_name.value: yn})
            invalid_vote = False


def test_user_vote(choice):
    if choice[0].lower() == 'y':
        choice = 'yes'
        return choice
    elif choice[0].lower() == 'n':
        choice = 'no'
        return choice
    else:
        raise InvalidVoteException


def test_user_name(name):
    if name.title() in [amigo.value for amigo in ThreeAmigos]:
        pass
    else:
        raise InvalidNameException


if __name__ == '__main__':
    welcome()
    get_game_name()
    for player in ThreeAmigos:
        get_name_and_vote()
    for user, vote in choices.items():
        print("{} chose {}".format(user, vote.upper()))

