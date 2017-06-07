# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# manufacturer: string
# purchase_date: number (year)
# durability: number (year)


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

    menu_list = ['Show table', 'Add game to inventory',
                 'Remove game from inventory', 'Update data for game']
    file_name = '/home/wera/codecool/python-lightweight-erp-project-zrzedliwy-starszy-pan-i-dzieciaki/inventory/inventory.csv'
    error_message = 'Select number from 0 to 4, pointing the action you want to be done'
    title = 'Inventory'
    table = data_manager.get_table_from_file(file_name)

    stay = True
    while stay:
        ui.print_menu(title, menu_list, 'Back to main menu')

        task_selection = ui.get_inputs([''], 'Please enter a number')

        while not common.is_selection_proper(task_selection, len(menu_list)):
            task_selection = ui.get_inputs([''], 'Please enter a number')
            ui.print_error_message(error_message)

        if task_selection[0] == '1':

            show_table(table)

        elif task_selection[0] == '2':

            table = add(table)

        elif task_selection[0] == '3':

            id_ = ask_for_id(table, 'Please enter an id of person to remove')
            table = remove(table, id_)

        elif task_selection[0] == '4':
            id_ = ask_for_id(table, 'Please enter an id of person whos data going to be updated')
            update(table, id_)

        else:
            stay = False


def ask_for_id(table, what_for):
    '''
    asks for for id, checks if it exists in table

    Args:
        table: list of lists
        what_for: (str) exmpl; 'Please enter an id of person to remove'

    Returns:
        id_: str
    '''

    id_ = ui.get_inputs([''], what_for)[0]
    while not is_id_on_table(table, id_):
        id_ = ui.get_inputs([], what_for)[0]

    return id_


def is_id_on_table(table, id_):
    '''
    function chcecks if table contain record of given id
    
    Args:
        table: list of lists

    Returns:
        Boolean
    '''
    for i in range(len(table)):
        if table[i][0] == id_:     # IS IT PROPER?
            return True
    return False


def show_table(table):
    """
    Display a table

    Args:
        table: list of lists to be displayed.

    Returns:
        None
    """

    title_list = ['id', 'name of game', 'company', 'amount']
    ui.print_table(table, title_list)


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

# the question: Which items have not exceeded their durability yet?
# return type: list of lists (the inner list contains the whole row with their actual data types)
#
# @table: list of lists
def get_available_items(table):

    # your code

    pass


# the question: What are the average durability times for each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [avg] }
#
# @table: list of lists
def get_average_durability_by_manufacturers(table):

    # your code

    pass
