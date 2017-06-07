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
    file_name = '/home/wera/codecool/python-lightweight-erp-project-zrzedliwy-starszy-pan-i-dzieciaki/hr/persons.csv'
    error_message = 'Select number from 0 to 4, pointing the action you want to be done'
    title = 'Human Resources'
    table = data_manager.get_table_from_file(file_name)

    stay = True
    while stay:
        ui.print_menu(title, menu_list, 'Back to main menu')

        task_selection = ui.get_inputs(['Please enter a number'], '')

        while not common.is_selection_proper(task_selection, len(menu_list)):
            task_selection = ui.get_inputs(['Please enter a number'], '')
            print_error_message(error_message)

        if task_selection[0] == '1':
            show_table(table)

        elif task_selection[0] == '2':
            table = add(table)

        '''elif task_selection[0] == '3':
            remove(table, id_)

        elif task_selection[0] == 4:
            update(table, id_)

        else:
            stay = False'''


def show_table(table):
    """
    Display a table

    Args:
        table: list of lists to be displayed.

    Returns:
        None
    """

    title_list = ['id', 'name', 'year of birth']
    ui.print_table(table, title_list)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table: table to add new record to

    Returns:
        Table with a new record
    """
    attribute_list = ['id', 'name', 'year of birth']
    a_person = [common.generate_random(table)]

    a_person += ui.get_inputs(['name and surname', 'year of birth'], 'Please, provide personal information')
    table.append(a_person)

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

    table = common.remove(table, id_)

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

    table = common.update(table, id_)

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
