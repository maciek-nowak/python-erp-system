# data structure:
# id: string
#     Unique and randomly generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# month: number
# day: number
# year: number
# type: string (in = income, out = outcome)
# amount: number (dollar)


# importing everything you need
import os
# User interface module
import ui
# data manager module
import data_manager
# common module
import common

def data_structure():
    '''

    '''
    ds = {
          'month (1-12)': lambda x: x.isdigit() and int(x) >= 1 and int(x) <= 12,
          'day (1-31)': lambda x: x.isdigit() and int(x) >= 1 and int(x) <= 31,
          'year (1900-9999)': lambda x: x.isdigit() and int(x) >= 1900 and int(x) <= 9999,
          'type (\'in\' or \'out\')': lambda x: x == 'in' or x == 'out',
          'ammount (dollar)': lambda x: x.isdigit()
         }

    return ds

def ask_user_for_data(data_structure):
    record = []
    for key in data_structure:
        user_input = ui.get_inputs([key], '')[0] 
        while not data_structure[key](user_input):
            user_input = ui.get_inputs([key], 'Wrong input')[0]
        if user_input.isdigit():
            user_input = int(user_input)
        record.append(user_input)
    return record


def find_index_by_id(table, id_):
    """
    Returns index of table contains id_ or returns None if id_ don't exist
    """

    for i in range(len(table)):
        if table[i][0] == id_:
            return i


def start_module():
    """
    Starts this module and displays its menu.
    User can access default special features from here.
    User can go back to main menu from here.

    Returns:
        None
    """



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
    ds = data_structure()
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

    index_to_delete = find_index_by_id(table, id_)

    if index_to_delete == None:
        ui.print_error_message('no item of this id')
    else:
        table.pop(index_to_delete)

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

    # keep previous id
    record = [id_]

    # data structure
    ds = data_structure()
    # apend record by data from user
    record += ask_user_for_data(ds)

    # 

    # change data
    table = remove(table, id_)
    table.append(record)


    return table


# special functions:
# ------------------

# the question: Which year has the highest profit? (profit=in-out)
# return the answer (number)
def which_year_max(table):

    # your code

    pass


# the question: What is the average (per item) profit in a given year? [(profit)/(items count) ]
# return the answer (number)
def avg_amount(table, year):

    # your code

    pass
