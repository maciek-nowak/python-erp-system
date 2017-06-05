# implement commonly used functions here

import random
import csv

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


def import_from_csv(filename):
    imported_things = []
    with open(filename, 'r') as string:
        reader = csv.reader(string, delimiter=';')
        for row in reader:
            imported_things.append(row)

    return imported_things
