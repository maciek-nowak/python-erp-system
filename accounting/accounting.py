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


def get_data_structure():
    '''
    Data container

    Returns:
        dictionary:
            key: string containing data name and description of requirements
            value: lambda function checking compliance of requirements
    '''
    ds = {
          'month (1-12)': lambda x: x.isdigit() and int(x) >= 1 and int(x) <= 12,
          'day (1-31)': lambda x: x.isdigit() and int(x) >= 1 and int(x) <= 31,
          'year (1900-9999)': lambda x: x.isdigit() and int(x) >= 1900 and int(x) <= 9999,
          'type (\'in\' or \'out\')': lambda x: x == 'in' or x == 'out',
          'amount (dollar)': lambda x: x.isdigit()
         }

    return ds


def ask_user_for_data(data_structure):
    """
    Ask user for data checking for compliance with requirements

    Args:
        data_structure: dictionary
    Returns:
        List containing record
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

    title = 'Accounting menu'
    options = ['add', 'remove', 'update', 'show table']
    functions = [add, remove, update, show_table]
    user_input = ''

    while user_input != '0':
        # read data
        table = data_manager.get_table_from_file('accounting/items.csv')

        # UI
        ui.print_menu(title, options, 'exit')
        user_input = ui.get_inputs(['Choose option'], '')[0]

        # bulletproof
        if user_input.isdigit() and int(user_input) <= len(options) and user_input != '0':
            user_input = int(user_input)

            # ask for id in remove and update functions
            if(user_input == 2 or user_input == 3):
                id_ = ui.get_inputs(['id'], '')[0]
                functions[user_input-1](table, id_)

            # don't ask for id in remove and update functions
            else:
                functions[user_input-1](table)

        # writing data
        data_manager.write_table_to_file('accounting/items.csv', table)


def show_table(table):
    """
    Display a table

    Args:
        table: list of lists to be displayed.

    Returns:
        None
    """

    header = ['id', 'month', 'day', 'year', 'type', 'amount']
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

    if index_to_delete is None:
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
    # check is id_ exists in table
    if not find_index_by_id(table, id_):
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

    return table


def count_year_profit(table):
    years = {}
    for record in table:
        year = record[3]
        profit = 0
        if record[4] == 'in':
            profit += int(record[5])
        elif record[4] == 'out':
            profit -= int(record[5])
        if year in years:
            years[year] += profit
        else:
            years[year] = profit
    return years


# special functions:
# ------------------

# the question: Which year has the highest profit? (profit=in-out)
# return the answer (number)

def which_year_max(table):

    year_profit = count_year_profit(table)
    max_year = table[0][3]

    for year in year_profit:
        if int(year_profit[year]) > int(year_profit[max_year]):
            max_year = year

    return int(max_year)


# the question: What is the average (per item) profit in a given year? [(profit)/(items count) ]
# return the answer (number)
def avg_amount(table, year):
    year = str(year)
    years_profit = count_year_profit(table)
    year_transactions = 0
    for record in table:
        if record[3] == year:
            year_transactions += 1
    try:
        return int(years_profit[year])/int(year_transactions)
    except KeyError:
        ui.print_error_message('no such year in database')