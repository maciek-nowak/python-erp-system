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
    """
    Function gets input from user and runs proper function

    Args:
        table (list): list of lists with customer data

    Returns:
        table (list): list of lists with customer data
        go_back_to_main (bool): if True exit to main menu
    """

    go_back_to_main = False

    inputs = ui.get_inputs(["Please enter a number:"], "")
    option = inputs[0]
    if option == "1":
        show_table(table)
    elif option == "2":
        table = add(table)
    elif option == "3":
        show_table(table)
        id_ = ui.get_inputs(["User id:"], "Please choose customer to remove.")[0]
        table = remove(table, id_)
    elif option == "4":
        show_table(table)
        id_ = ui.get_inputs(["User id:"], "Please choose customer to update.")[0]
        table = update(table, id_)
    elif option == "5":
        ui.print_result(get_longest_name_id(table), 'Id of customer with longest name:')
    elif option == "6":
        ui.print_result(get_subscribed_emails(table), 'Customers subscribed to newsletter:')
    elif option == "0":
        go_back_to_main = True
    else:
        ui.print_error_message("There is no such option.")

    return table, go_back_to_main


def handle_menu():
    """
    Function prints CRM module menu

    Returns:
        None
    """

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

    try:
        table = data_manager.get_table_from_file('crm/customers.csv')
    except FileNotFoundError:
        table = []

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


def check_email(e_mail):
    """
    Function checks if given e_mail is in proper format

    Args:
        e_mail (str): string with customer e_mail

    Returns:
        is_correct (bool): if True e_mail is in proper format
    """

    is_correct = True
    if len(e_mail) < 5:  # checks email length
        is_correct = False
    if '@' not in e_mail:   # checks if email contains '@'
        is_correct = False
    else:
        email_parts = e_mail.split('@')
        # checks if email contains dot in second part
        if len(email_parts[0]) < 1 or '.' not in email_parts[1] or len(email_parts) > 2:
            is_correct = False
    if '.' not in e_mail:
        is_correct = False
    else:
        email_parts = e_mail.split('.')
        if len(email_parts[-1]) < 1:
            is_correct = False
    # checks if email parts contains at least 1 character
    if '@' in e_mail and '.' in e_mail:
        if len(e_mail.split('@')[1].split('.')[-2]) < 1:
            is_correct = False

    return is_correct


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        table (list): table with a new record
    """

    name = ''
    while not name:
        name = ui.get_inputs(['Customer name:'], "Please provide new customer data")[0]
        if not name:
            ui.print_error_message("It's not a proper name.")

    is_correct = False
    while not is_correct:
        e_mail = ui.get_inputs(['Customer e-mail:'], " ")[0]
        is_correct = check_email(e_mail)
        if not is_correct:
            ui.print_error_message("This isn't proper e-mail")

    is_subscribed = ''
    while is_subscribed not in ['0', '1']:
        is_subscribed = ui.get_inputs(['Is the customer subscribed to the newsletter [1 - yes / 0 - no]:'], "")[0]
        if is_subscribed not in ['0', '1']:
            ui.print_error_message("Acceptable answer are only 0 for 'no' and 1 for 'yes'.")

    new_record = [common.generate_random(table), name, e_mail, is_subscribed]
    table.append(new_record)

    data_manager.write_table_to_file('crm/customers.csv', table)
    return table


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        table (list): table without specified record.
    """

    for i in range(len(table)):
        if table[i][0] == id_:
            table.pop(i)
            data_manager.write_table_to_file('crm/customers.csv', table)
            return table

    ui.print_error_message("There is no customer with given id in database.")
    return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table (list): list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        table (list): table with updated record
    """

    for i in range(len(table)):
        if table[i][0] == id_:
            table = add(table)
            table[-1][0] = id_
            table[i] = table.pop()
            data_manager.write_table_to_file('crm/customers.csv', table)
            return table

    ui.print_error_message("There is no customer with given id in database.")
    return table


# special functions:
# ------------------


# the question: What is the id of the customer with the longest name ?
# return type: string (id) - if there are more than one longest name, return the first by descending alphabetical order
def get_longest_name_id(table):
    """
    Function returns id of customer with longest name

    Args:
        table (list): list of lists with customer data

    Returns:
        longest_name_id (str): id of customer with longest name
    """

    longest_name = ''
    longest_name_id = ''

    for record in table:
        if len(record[1]) > len(longest_name):
            longest_name = record[1]
            longest_name_id = record[0]

        elif len(record[1]) == len(longest_name):
            longest_name = min(record[1].lower(), longest_name.lower())
            if longest_name == record[1].lower():
                longest_name_id = record[0]

    return longest_name_id


# the question: Which customers has subscribed to the newsletter?
# return type: list of strings (where string is like email+separator+name, separator=";")
def get_subscribed_emails(table):
    """
    Function returns list of customers subscribed to the newsletter

    Args:
        table (list): list of lists with customer data

    Returns:
        list_of_subscribers (list): list of strings containing names and e-mails of customers subscribed to newsletter
    """

    list_of_subscribers = []

    for record in table:
        is_subscribed = record[3]
        if is_subscribed == '1':
            list_of_subscribers.append(record[2] + ';' + record[1])

    return list_of_subscribers
