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
                 'Remove employee from register', 'Update data of employee', 'oldest', 'avg']
    file_name = 'hr/persons.csv'
    error_message = 'Select number from 0 to 6, pointing the action you want to be done'
    title = 'Human Resources'
    table = data_manager.get_table_from_file(file_name)

    stay = True
    while stay:
        ui.print_menu(title, menu_list, 'Back to main menu')

        task_selection = ui.get_inputs(['Please enter a number'], '')

        while not common.is_selection_proper(task_selection, len(menu_list)):
            ui.print_error_message(error_message)
            task_selection = ui.get_inputs(['Please enter a number'], '')

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

        elif task_selection[0] == '5':

            ui.print_result(get_oldest_person(table), 'The oldest: ')

        elif task_selection[0] == '6':
            ui.print_result(get_persons_closest_to_average(table), 'Closest to average with age is ')

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
        id_ = ui.get_inputs([''], what_for)[0]

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
    file_name = './hr/persons.csv'
    attribute_list = ['id', 'name', 'year of birth']
    a_person = [common.generate_random(table)]

    a_person += ui.get_inputs(['name and surname', 'year of birth'], 'Please, provide personal information')
    table.append(a_person)
    data_manager.write_table_to_file(file_name, table)

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

    index_to_delete = common.find_index_by_id(table, id_)

    if index_to_delete is None:
        ui.print_error_message('no item of this id')
    else:
        table.pop(index_to_delete)

    file_name = './hr/persons.csv'
    data_manager.write_table_to_file(file_name, table)

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

    for i in range(len(table)):
        if table[i][0] == id_:
            person = table[i]
            removal_index = i
            break

    list_of_options = ["id", "name and surname", "year of bearth"]

    option_selection = ui.get_inputs(list_of_options, "Do you want to update (y/n) : ")
    for i in range(len(option_selection)):
        if option_selection[i] == 'y' and i == 0:
            person[i] = common.generate_random(table)
        elif option_selection[i] == 'y':
            person[i] = ui.get_inputs([list_of_options[i]], "New {} is ".format(list_of_options[i]))[0]

    table.remove(table[removal_index])
    table.append(person)

    file_name = './hr/persons.csv'
    data_manager.write_table_to_file(file_name, table)

    return table


# special functions:
# ------------------

# the question: Who is the oldest person ?
# return type: list of strings (name or names if there are two more with the same value)
def get_oldest_person(table):

    current_year = 2017   # OMG GDZIE JEST CZAS
    min_birth_year = current_year
    old_people = []

    for i in range(len(table)):
        if int(table[i][2]) < min_birth_year:
            min_birth_year = int(table[i][2])

    for i in range(len(table)):
        if int(table[i][2]) == min_birth_year:
            old_people.append(table[i][1])

    return old_people


# the question: Who is the closest to the average age ?
# return type: list of strings (name or names if there are two more with the same value)
def calculate_add(values):
    """Function calculates summary width of all table columns.

    Args:
        table_columns_width (list of int): list of table column width

    Return:
        total_width (int): summary width of all table columns
    """
    total = 0

    for value in values:
        total += value

    return total


# the question: Who is the closest to the average age ?
# return type: list of strings (name or names if there are two more with the same value)
def get_persons_closest_to_average(table):
    current_year = 2017
    ages = [current_year - int(record[2]) for record in table]
    sum_ages = calculate_add(ages)
    average_age = sum_ages / len(table)

    names = []
    smallest_difference_to_avg = abs(current_year - int(table[0][2]) - average_age)
    for record in table:
        difference_to_avg = abs(current_year - int(record[2]) - average_age)

        if difference_to_avg < smallest_difference_to_avg:
            smallest_difference_to_avg = difference_to_avg
            names = [record[1]]
        elif difference_to_avg == smallest_difference_to_avg:
            names.append(record[1])

    return names
