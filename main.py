# coding: utf8
import settings
from random import randint, shuffle


def print_greetings():
    print "%s\n%s" % (settings.welcome_greetings, settings.version)


def throw_dice():
    return randint(1, 6)


def throw_dices():
    return [throw_dice() for _ in range(2)]


def get_new_player_position(current_cell, thrown_number):
    """
    Initial cell of the first circle is also a final cell of the next circles,
    thus it also should be valued at 44.
    Although it seems to be like a temporary solution,
    for now there could not be any O cell or get_new_player_position function won`t work.

    This test brings the position after the initial throw.
    >>> get_new_player_position(settings.initial_cell, 2)
    2

    This test estimates the position after finishing
    the first circle and hitting the start field.
    >>> get_new_player_position(settings.cells_number, 1)
    1

    This test estimates the position after crossing the start field.
    >>> get_new_player_position(settings.cells_number, 5)
    5

    """
    return (current_cell + thrown_number) % settings.cells_number


def get_number_of_players():
    """
    >>> get_number_of_players(float)
    ValueError: Number must be exact integer
    >>> get_number_of_players(m>4)
    ValueError: Max players - 4
    >>> get_number_of_players(m<2)
    ValueError: Min players - 2
    """
    while True:
        m = raw_input("Enter the number of players: ")
        try:
            m = int(m)
            if m <= 1:
                raise ValueError("Min number of players is 2")
            elif m > settings.max_players_number:
                raise ValueError('Max number of players - 4, enter the correct number!')
            print('Ok!')
            return m
        except ValueError as error:
            print error


def input_player_name(player, names):
    while True:
        name = raw_input('Player_%d name: ' % (player + 1))
        if name not in names:
            return name
        print "Name %s exists" % name


def get_player_profile(player, names):
    return [
        input_player_name(player, names),
        settings.initial_funds,
        settings.initial_cell
    ]


def get_all_players_names(profiles):
    return [profile[0] for profile in profiles]


def generate_profiles(number_of_players):
    profiles = []  # TODO: make it dictionary not list
    for player_number in range(number_of_players):
        current_profile = get_player_profile(
            player_number,
            get_all_players_names(profiles)
        )
        profiles.append(current_profile)
    return profiles


def shuffle_players_profiles(profiles):
    shuffled_list = profiles[:]
    shuffle(shuffled_list)
    return shuffled_list


def main():
    print_greetings()
    number_of_players = get_number_of_players()
    shuffled_profiles = shuffle_players_profiles(generate_profiles(number_of_players))
    print shuffled_profiles
    while True:
        for player in shuffled_profiles:
            raw_input(player[0] + '>>>')
            print(player[0] + " thow the dice!") # 13
            temp_throw = throw_dice()[:]
            print("dice 1 roll:      ")
            print("dice 2 roll:      ")
    # if x == y:
    #         player_droll = 1
    #      else:
    #         player_droll = 0
    #      gameboard_playermove(player,x + y),0)


main()
