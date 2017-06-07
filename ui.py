

def calculate_column_width(table, title_list):
    """Function calculates width of every table column.

    Args:
        table: list of lists - table to display
        title_list: list containing table headers

    Returns:
        table_columns_width (list of int): list of table column width
    """
    margin = 2
    table_columns_width = []

    # calculates the table columns width and appends them to the list
    column_nr = 0
    for title in title_list:
        column_width = len(max([str(title)] + [str(lst[column_nr]) for lst in table], key=len)) + 2 * margin
        table_columns_width.append(column_width)
        column_nr += 1

    return table_columns_width


def create_column_titles(title_list, table_columns_width):
    """Function creates first row of summary table with columns titles.

    Args:
        title_list (list): list of table column names
        table_columns_width (list of int): list of table column width

    Return:
        table_to_print (list of str): list representing summary table
    """

    table_to_print = []
    column_title_row = [2 * ' ' + str(title_list[i]) + (table_columns_width[i] - len(
        str(title_list[i])) - 2) * ' ' for i in range(len(title_list))]
    column_title_row = ('|').join(column_title_row)
    table_to_print.append(column_title_row)

    return table_to_print


def create_data_rows(table, table_columns_width, table_to_print):
    """Function creates rows of summary table with computing times.

    Args:
        table_to_print (list of str): list representing summary table
        table_columns_width (list of int): list of table column width
        table: list of lists - table to display

    Return:
        table_to_print (list of str): list representing summary table
    """

    for lst in table:
        column_nr = 0
        row = []
        for element in lst:
            row.append(2 * ' ' + str(element) + (table_columns_width[column_nr] - len(str(element)) - 2) * ' ')
            column_nr += 1

        row = ('|').join(row)
        table_to_print.append(row)

    return table_to_print


def calculate_table_width(table_columns_width):
    """Function calculates summary width of all table columns.

    Args:
        table_columns_width (list of int): list of table column width

    Return:
        total_width (int): summary width of all table columns
    """
    total_width = 0

    for column_width in table_columns_width:
        total_width += column_width

    return total_width


def finalize_table_to_print(table_to_print, table_columns_width):
    """Function prepares final shape of table to print.

    Args:
        table_to_print (list of str): list representing summary table
        table_columns_width (list of int): list of table column width

    Return:
        table_to_print (list of str): list representing summary table
    """

    # creates border rows of the table
    total_width = calculate_table_width(table_columns_width)

    first_row = '/' + (total_width + len(table_columns_width) - 1) * '-' + '\\'
    middle_row = '|' + ('|').join([width * '-' for width in table_columns_width]) + '|'
    last_row = '\\' + first_row[1:-1] + '/'

    # creates final shape of the table
    table_to_print = ['|' + line + '|\n' for line in table_to_print]
    table_to_print = (middle_row + '\n').join(table_to_print)
    table_to_print = first_row + '\n' + table_to_print + last_row

    return table_to_print


def print_table(table, title_list):
    """
    Prints table with data. Sample output:
        /-----------------------------------\
        |   id   |      title     |  type   |
        |--------|----------------|---------|
        |   0    | Counter strike |    fps  |
        |--------|----------------|---------|
        |   1    |       fo       |    fps  |
        \-----------------------------------/

    Args:
        table: list of lists - table to display
        title_list: list containing table headers

    Returns:
        This function doesn't return anything it only prints to console.
    """

    table_columns_width = calculate_column_width(table, title_list)
    table_to_print = create_column_titles(title_list, table_columns_width)
    table_to_print = create_data_rows(table, table_columns_width, table_to_print)
    table_to_print = finalize_table_to_print(table_to_print, table_columns_width)
    print(table_to_print)


def print_result(result, label):
    """
    Displays results of the special functions.

    Args:
        result: string, list or dictionary - result of the special function
        label: label of the result

    Returns:
        This function doesn't return anything it only prints to console.
    """

    print('\n', label)

    if type(result) is str:
        print(result)
    elif type(result) is list:
        print('\n'.join(result))
    elif type(result) is dict:
        for key in result:
            print(key + ':', result[key])


def print_menu(title, list_options, exit_message):
    """
    Displays a menu. Sample output:
        Main menu:
            (1) Store manager
            (2) Human resources manager
            (3) Inventory manager
            (4) Accounting manager
            (5) Sales manager
            (6) Customer relationship management (CRM)
            (0) Exit program

    Args:
        title (str): menu title
        list_options (list): list of strings - options that will be shown in menu
        exit_message (str): the last option with (0) (example: "Back to main menu")

    Returns:
        This function doesn't return anything it only prints to console.
    """

    print('\n', title)

    option_id = 1
    for option in list_options:
        print('({})'.format(option_id), option)
        option_id += 1

    print('(0)', exit_message)


def get_inputs(list_labels, title):
    """
    Gets list of inputs from the user.
    Sample call:
        get_inputs(["Name","Surname","Age"],"Please provide your personal information")
    Sample display:
        Please provide your personal information
        Name <user_input_1>
        Surname <user_input_2>
        Age <user_input_3>

    Args:
        list_labels: list of strings - labels of inputs
        title: title of the "input section"

    Returns:
        List of data given by the user. Sample return:
            [<user_input_1>, <user_input_2>, <user_input_3>]
    """

    inputs = []

    print('\n', title)

    for question in list_labels:
        answer = input(question + ' ')
        inputs.append(answer)

    return inputs


# This function displays an error message. (example: Error: @message)
#
# @message: string - the error message
def print_error_message(message):
    """
    Displays an error message

    Args:
        message(str): error message to be displayed

    Returns:
        This function doesn't return anything it only prints to console.
    """

    print('\nError:', message)
