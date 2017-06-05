# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# birth_date: number (year)


# importing everything you need
import os
# User interface module
import ui
# data manager module
import data_manager
# common module
import common


def start_module():
    """
    Starts this module and displays its menu.
    User can access default special features from here.
    User can go back to main menu from here.

    Returns:
        None
    """

    menu_list = ['Show table of employees', 'Add employee to register',
                 'Remove employee from register', 'Update data of employee']
    message = 'Select number from 0 to 4, pointing the action you want to be done'

    ui.print_menu('Human Resources', menu_list, 'Back to main menu')
    
    task_selection = ui.get_inputs(['action number: '], 'What to do?')
    while task_selection[0] not in '12340':
        ui.print_error_message(message)
        task_selection = ui.get_inputs(['action number: '], 'What to do?')

    if task_selection[0] == '0':
        pass
    elif task_selection[0] == '1':
        pass
    elif task_selection[0] == '2':
        pass
    elif task_selection[0] == '3':
        pass
    elif task_selection[0] == '4':
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

    # your code

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

# the question: Who is the oldest person ?
# return type: list of strings (name or names if there are two more with the same value)
def get_oldest_person(table):

    # your code

    pass


# the question: Who is the closest to the average age ?
# return type: list of strings (name or names if there are two more with the same value)
def get_persons_closest_to_average(table):

    # your code

    pass
