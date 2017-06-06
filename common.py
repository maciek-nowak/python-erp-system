# implement commonly used functions here

import random


# generate and return a unique and random string
# other expectation:
# - at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter
# - it must be unique in the list
#
# @table: list of lists
# @generated: string - randomly generated string (unique in the @table)
def generate_random(table):
    """
    Generates random and unique string. Used for id/key generation.

    Args:
        table: list containing keys. Generated string should be different then all of them

    Returns:
        Random and unique string
    """

    generated = ''

    # your code

    return generated


def is_selection_proper(task_selection, max_possible_choice):
    '''
    checks if input is valid
    Args:
        task_selection: list (len(list)=1)
    Returns:
        task_selection: list (len(list)=1) cappable to navigate tghrough the program
    '''
    if int(task_selection[0]) not in range(max_possible_choice):
        return False
    else:
        return True
