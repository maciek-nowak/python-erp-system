# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# title: string
# price: number (the actual sale price in $)
# month: number
# day: number
# year: number
# month,year and day combined gives the date the sale was made


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
    table = data_manager.get_table_from_file('sales/sales.csv')
    while True:
        options = ["Show table",
                   "add table",
                   "update table",
                   "get id item with lowest price",
                   "get item sold beetween date",
                   "remove"]
        ui.print_menu("Main menu", options, "Exit program")
        try:
            inputs = ui.get_inputs(["Please enter a number: "], "")
            option = inputs[0]
            if option == "1":
                show_table(table)
            elif option == "2":
                add(table)
            elif option == "3":
                id_ = ui.get_inputs(['give me id'], 'Update by id')
                update(table, id_[0])
            elif option == "4":
                ui.print_result(get_lowest_price_item_id(table), 'Lowest price item: ')
            elif option == "5":
                between_solds_inputs = ui.get_inputs(
                    ['Month from', 'Day from', 'Year from', 'Month to', 'Day to', 'Year to'], 'Give me this data')
                cycki = get_items_sold_between(table, between_solds_inputs[0], between_solds_inputs[1],
                                               between_solds_inputs[2], between_solds_inputs[3],
                                               between_solds_inputs[4], between_solds_inputs[5])
                show_table(cycki)
            elif option == "6":
                id_ = ui.get_inputs(['give me id'], 'remove by id')
                remove(table, id_)
            elif option == "0":
                break
            else:
                raise KeyError("There is no such option.")
        except KeyError as err:
            ui.print_error_message(err)


def show_table(table):
    """
    Display a table

    Args:
        table: list of lists to be displayed.

    Returns:
        None
    """
    title_list = ['id', 'name', 'price', 'month', 'day', 'year']
    ui.print_table(table, title_list)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table: table to add new record to

    Returns:
        Table with a new record
    """
    inputs = ['name', 'price', 'month', 'day', 'year']
    item_to_add = ui.get_inputs(inputs, 'Items to add, please enter ur data')
    try:
        if int(item_to_add[2]) > 13 and int(item_to_add[2]) < 1:
            msg = 'wrong month structure: '
            msg += str(item_to_add[2])
            ui.print_error_message(msg)
            return 0
        if int(item_to_add[3]) > 31 and int(item_to_add[3]) < 1:
            msg = 'wrong day structure: '
            msg += str(item_to_add[3])
            ui.print_error_message(msg)
            return 0
        if int(item_to_add[4]) > 9999 and int(item_to_add[4]) < 1970:
            msg = 'wrong year structure: '
            msg += str(item_to_add[4])
            ui.print_error_message(msg)
            return 0
    except ValueError as err:
        ui.print_error_message(err)

    item_to_add.insert(0, common.generate_random(table))
    table.append(item_to_add)
    data_manager.write_table_to_file('sales/sales.csv', table)

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

    delete = False
    index = 0
    id_ = str(id_[0])
    try:
        while table and index != len(table):
            if table[index][0] == id_:
                del table[index]
                data_manager.write_table_to_file('sales/sales.csv', table)  # FILENAME EVERYONE GOT THEIR OWN FILENAME!
                return table
            index += 1
    except:
        msg = 'Cannot delete item with id: '
        msg += str(id_)
        ui.print_error_message(msg)

    msg = 'Item not deleted. Propably your id is not here. ID: '
    msg += str(id_)
    ui.print_error_message(msg)
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
    update_items = []
    # szukamy id
    for lists in table:
        if lists[0] == id_:
            inputs = ['ID', 'name', 'price', 'month', 'day', 'year']
            item_to_add = ui.get_inputs(inputs, 'Item to update, please enter ur data')
            try:
                if int(item_to_add[3]) > 13 or int(item_to_add[3]) < 1:
                    msg = 'wrong month structure: '
                    msg += str(item_to_add[2])
                    ui.print_error_message(msg)
                    return 0
                if int(item_to_add[4]) > 31 or int(item_to_add[4]) < 1:
                    msg = 'wrong day structure: '
                    msg += str(item_to_add[3])
                    ui.print_error_message(msg)
                    return 0
                if int(item_to_add[5]) > 9999 or int(item_to_add[5]) < 1970:
                    msg = 'wrong year structure: '
                    msg += str(item_to_add[4])
                    ui.print_error_message(msg)
                    return 0
            except ValueError as err:
                ui.print_error_message(err)
                return 0

            remove(table, id_)
            table.append(item_to_add)

            data_manager.write_table_to_file('sales/sales.csv', table)

    return table


# special functions:
# ------------------

# the question: What is the id of the item that was sold for the lowest price ?
# return type: string (id)
# if there are more than one with the lowest price, return the first by descending alphabetical order
def get_lowest_price_item_id(table):
    """
    Returning id with lowest price

        Args:
            table: list in which record we should look for lowest price
            table (list): table to look for lowest price

        Returns:
            Id of item with lowest price
    """
    min = table[0][2]
    id_lower_price = 0
    for index in range(len(table)-1):
        if table[index][2] < min:
            min = table[index][2]
            id_lower_price = table[index][0]

    return id_lower_price


# the question: Which items are sold between two given dates ? (from_date < sale_date < to_date)
# return type: list of lists (the filtered table)
def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
    """
        Filtering table with date that is between input dates

        Args:
            table: list in which record should program look for records
            month_from: month date we would like to start looking for
            day_from: day date we would like to start looking for
            year_from: year date we would like to start looking for
            month_to: month date that we would like to stop looking for
            day_to: day date that we would like to stop looking for
            year_to: year date that we would like to stop looking for

        Returns:
            list of lists thats are filtered from/to dates
    """

    items_sold_between = []
    index = 0
    start_date = str(year_from) + str(month_from) + str(day_from)
    end_date = str(year_to) + str(month_to) + str(day_to)
    for record in table:
        if end_date > record[-1] > start_date:
            items_sold_between.append(record)

    return items_sold_between
