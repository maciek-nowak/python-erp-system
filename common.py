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

    checkout = True
    while checkout:
        generated += chr(random.randrange(97, 123))
        generated += chr(random.randrange(65, 91))
        generated += str(random.randrange(0, 10))
        generated += str(random.randrange(0, 10))
        generated += chr(random.randrange(65, 91))
        generated += chr(random.randrange(97, 123))
        for i in range(2):
            generated += chr(random.randrange(33, 48))
        for index in range(len(table)):
            if generated == table[index][0]:
                checkout = True
            else:
                checkout = False
        return generated

def find_index_by_id(table, id_):
    """
    Returns:
        int: index of table contains id_
        None: if id_ don't exist
    """

    for i in range(len(table)):
        if table[i][0] == id_:
            return i

