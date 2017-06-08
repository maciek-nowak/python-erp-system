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
    Data container

    Returns:
        data_structure: dictionary
            key: data name
            value: lambda returns True if input meets requirements
    """
    data_structure = {
          'title': lambda x: True,
          'manufacturer': lambda x: True,
          'price (dollars)': lambda x: x.isdigit(),
          'in stock (amount)': lambda x: x.isdigit()
        }

    return data_structure


def ask_user_for_data(data_structure):
    """
    Recieves data from user

    Args:
        data_structure: dictionary

    Returns:
        record: list
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


def choose_option(option, table):
    """
    Switches options(functions), makes changes to table

    Args:
        option: string
        table: list of list

    Returns:
        table: list of list
    """

    if option == '1':
        show_table(table)

    elif option == '2':
        ui.print_result('Please enter data for', 'Adding new data')
        return add(table)

    elif option == '3':
        id_ = ui.get_inputs(['id: '], 'Which record you want to delete?')[0]
        return remove(table, id_)

    elif option == '4':
        id_ = ui.get_inputs(['id: '], 'Which record you want to update?')[0]
        return update(table, id_)

    elif option == '5':
        result = get_counts_by_manufacturers(table)
        ui.print_result(result, 'Amounts of game by manufacturer: ')

    elif option == '6':
        manufacturer = ui.get_inputs(['manufacturer: '], 'Counting average for')[0]
        result = str(get_average_by_manufacturer(table, manufacturer))
        ui.print_result(result, 'Average amount of games by ' + manufacturer + ':')

    else:
        ui.print_error_message('There is no such option')

    return table


def start_module():
    """
    Starts this module and displays its menu.
    User can access default special features from here.
    User can go back to main menu from here.

    Returns:
        None
    """

    title = 'Store menu'
    options = ['Show table', 'Add', 'Remove', 'Update', 'Games by manufacturer', 'Average stock by manufacturer']
    user_input = ''
    file_path = 'store/games.csv'

    while user_input != '0':
        try:
            table = data_manager.get_table_from_file(file_path)
        except FileNotFoundError:
            ui.print_error_message('Ther is no data file')
            table = []

        ui.print_menu(title, options, 'Return to main menu')
        user_input = ui.get_inputs(['Choose option'], '')[0]
        table = choose_option(user_input, table)
        data_manager.write_table_to_file(file_path, table)


def show_table(table):
    """
    Display a table

    Args:
        table: list of lists to be displayed.

    Returns:
        None
    """

    header = ['id', 'title', 'manufacturer', 'price', 'in stock']
    ui.print_table(table, header)


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

    pass


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

    pass


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table: list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        table with updated record
    """

    # check is id_ exists in table
    index_to_update = common.find_index_by_id(table, id_)

    if index_to_update is None:
        ui.print_error_message('no such id')
        return table

    # keep previous id
    record = [id_]

    # data structure
    ds = get_data_structure()

    # append record by data from user
    record += ask_user_for_data(ds)

    # change data
    table = remove(table, id_)
    table.append(record)

    pass


# special functions:
# ------------------

# the question: How many different kinds of game are available of each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [count] }
def get_counts_by_manufacturers(table):
    """
    Counts amount of game by each manufacturer

    Args:
        table: list of list

    Returns:
        dictionary
    """

    result = {}
    for record in table:
        manufacturer = record[2]
        if manufacturer in result.keys():
            result[manufacturer] += 1
        else:
            result[manufacturer] = 1
    return result


# the question: What is the average amount of games in stock of a given manufacturer?
# return type: number
def get_average_by_manufacturer(table, manufacturer):
    """
    Compute average ammount of games in stock of a givn manufacturer

    Args:
        table: list of lists
        manufacuter: string

    Returns:
        float
    """
    ammount_by_manufacturer = 0
    for record in table:
        if record[2] == manufacturer:
            ammount_by_manufacturer += int(record[4])

    counts = get_counts_by_manufacturers(table)
    if manufacturer not in counts:
        ui.print_error_message('There is no such manufacturer')
        return 0.0
    else:
        return ammount_by_manufacturer/counts[manufacturer]
