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


def get_name_and_vote(player_count):
    user_name = None
    incorrect_name = True
    while incorrect_name:
        user_name = input("Who are you?")
        try:
            test_user_name(user_name)
        except InvalidNameException:
            print("\tThat is not one of the Three Amigos.")
            time.sleep(1)
        else:
            incorrect_name = False
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
            if player_count < 3:
                print("Thank you, {} your vote has been recorded. Please pass the "
                      "laptop to the next amigo.".format(user_name.value))
            else:
                print("Thank you, {} your vote has been recorded.".format(user_name.value))
            invalid_vote = False


def get_decision():
    yes = 0
    no = 0
    for value in choices.values():
        if value == 'yes':
            yes += 1
        else:
            no += 1
    if yes > 1:
        print("The ayes have it! We will play {} again next week.".format(game))
        if yes == 3:
            print("There were {} yeses and {} noes.".format(yes, no))
        else:
            print("There were {} yeses and {} no.".format(yes, no))
    else:
        print("The nays have it. We are moving on folks. ")
        if no == 3:
            print("There were {} yeses and {} noes.".format(yes, no))
        else:
            print("There was {} yes and {} noes.".format(yes, no))


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
    player_count = 0
    for player in ThreeAmigos:
        player_count += 1
        get_name_and_vote(player_count)
    get_decision()
