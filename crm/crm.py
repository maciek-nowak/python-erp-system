# data structure:
# id: string
#     Unique and randomly generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# email: string
# subscribed: boolean (Is she/he subscribed to the newsletter? 1/0 = yes/not)


# importing everything you need
import os
# User interface module
import ui
# data manager module
import data_manager
# common module
import common


def choose_and_start_option(table):
    go_back_to_main = False

    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == "1":
        show_table(table)
    elif option == "2":
        table = add(table)
    elif option == "3":
        show_table(table)
        id_ = ui.get_inputs(["User id"], "Please choose customer to remove")[0]
        table = remove(table, id_)
    elif option == "4":
        show_table(table)
        id_ = ui.get_inputs(["User id:"], "Please choose customer to update")[0]
        table = update(table, id_)
    elif option == "5":
        ui.print_result(get_longest_name_id(table), 'Id of customer with longest name')
    elif option == "6":
        ui.print_result(get_subscribed_emails(table), 'Customers subscribed to newsletter')
    elif option == "0":
        go_back_to_main = True
    else:
        ui.print_error_message("There is no such option.")

    return table, go_back_to_main


def handle_menu():
    options = ["List customer data",
               "Add new customer",
               "Remove customer",
               "Update customer data",
               "Find customer with longest name",
               "Print customers subscribed to newsletter"]

    ui.print_menu("Customer Relationship Management (CRM)", options, "Return to Main menu")


def start_module():
    """
    Starts this module and displays its menu.
    User can access default special features from here.
    User can go back to main menu from here.

    Returns:
        None
    """

    table = data_manager.get_table_from_file('crm/customers.csv')

    go_back_to_main = False
    while not go_back_to_main:
        handle_menu()
        table, go_back_to_main = choose_and_start_option(table)


def show_table(table):
    """
    Display a table

    Args:
        table: list of lists to be displayed.

    Returns:
        None
    """

    title_list = ['id', 'name', 'e-mail', 'subscribed']
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

    for i in range(len(table)):
        if table[i][0] == id_:
            table.pop(i)
            data_manager.write_table_to_file('crm/customers.csv', table)
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
            table = add(table)
            table[-1][0] = id_
            table.insert(i, table.pop())
            data_manager.write_table_to_file('crm/customers.csv', table)
    return table


# special functions:
# ------------------


# the question: What is the id of the customer with the longest name ?
# return type: string (id) - if there are more than one longest name, return the first by descending alphabetical order
def get_longest_name_id(table):

    # your code

    pass


# the question: Which customers has subscribed to the newsletter?
# return type: list of strings (where string is like email+separator+name, separator=";")
def get_subscribed_emails(table):

    # your code

    pass
