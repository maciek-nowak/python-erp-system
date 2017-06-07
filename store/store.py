# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# title: string
# manufacturer: string
# price: number (dollars)
# in_stock: number

# importing everything you need
import os
# User interface module
import ui
# data manager module
import data_manager
# common module
import common


def get_data_structure():
    """
    """
    ds = {
          'title': lambda x: True,
          'manufacturer': lambda x: True,
          'price (dollars)': lambda x: x.isdigit(),
          'in stock (amount)': lambda x: x.isdigit()
        }

    return ds


def ask_user_for_data(data_structure):
    """

    """

    record = []
    for key in data_structure:
        # ask user for input specific data
        user_input = ui.get_inputs([key], '')[0]

        # ask user for input specific data until data meet requirements
        while not data_structure[key](user_input):
            user_input = ui.get_inputs([key], 'Wrong input')[0]

        record.append(user_input)
    return record


def start_module():
    """
    Starts this module and displays its menu.
    User can access default special features from here.
    User can go back to main menu from here.

    Returns:
        None
    """

    # your code

    pass


def show_table(table):
    """
    Display a table

    Args:
        table: list of lists to be displayed.

    Returns:
        None
    """

    # your code

    pass


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table: table to add new record to

    Returns:
        Table with a new record
    """

    # generate random id
    record = [common.generate_random(table)]

    # data structure
    ds = get_data_structure()
    # append record by data from user
    record += ask_user_for_data(ds)

    # append table by record
    table.append(record)

    return table


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table: table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        Table without specified record.
    """

    # your code

    return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table: list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        table with updated record
    """

    # your code

    return table


# special functions:
# ------------------

# the question: How many different kinds of game are available of each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [count] }
def get_counts_by_manufacturers(table):

    # your code

    pass


# the question: What is the average amount of games in stock of a given manufacturer?
# return type: number
def get_average_by_manufacturer(table, manufacturer):

    # your code

    pass
