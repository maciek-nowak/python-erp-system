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

    #letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o,','p','q','r','s','t','u','v','w','x','y','z']
    #losujemy i dodajemy
    #wielkie od 65 do 90 włacznie
    #male od 97 do 122 włacznie
    #znaki 33 do 47 włacznie
    checkout = True
    while checkout:
        generated += chr(random.randrange(97,123))
        generated += chr(random.randrange(65,91))
        generated += str(random.randrange(0,10))
        generated += str(random.randrange(0,10))
        generated += chr(random.randrange(65,91))
        generated += chr(random.randrange(97,123))
        for i in range(2):
            generated += chr(random.randrange(33,48))
        for index in range(len(table)):
            if generated == table[index][0]:
                checkout = True
            else:
                checkout = False
        return generated
