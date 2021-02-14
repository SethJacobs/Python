# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# There are 3 global variables to define:
#  num_columns: an integer giving the number of columns
#  num_rows: an integer giving the number of rows
#  sheet_contents: a dict storing all non-default spreadsheet contents explicitly.
#            The keys are (column, row) tuples, with integer column and row values where
#            1, not 0, is the first row/column. The dict values are the cell values.
#            Any cell value that parses as an integer should be stored
#            as an integer, otherwise as a string.  For any cells not explicitly set to
#            values, the dictionary should return a single blank space (" "). (Check
#            the documentation of the get() method for dicts.)
#
import sys

num_columns = -1  # initial value
num_rows = -1  # initial value
sheet_contents = {}


#  Examines sys.argv and sets up the 3 global variables that represent the spreadsheet.
#  This function must validate all input before populating the dictionary.
# @param args a string array that defaults to sys.argv but can be overridden
# @return True if all data validates, False otherwise
#
def init_spreadsheet(args=sys.argv):
    if not validateRange(args):
        print(
            "Please specify a valid spreadsheet range, with highest column between A and J and highest row as an integer between 1 and 9")
        return False
    else:
        global num_columns
        num_columns = ord(args[1]) - 65
        global num_rows
        num_rows = int(args[2])

    for i in range(3, len(args) - 1):
        string = args[i]
        column = string[0]
        row = string[1]
        if is_valid_integer(args[i + 1]):
            sheet_contents.update({(column, row): int(args[i + 1])})
        else:
            sheet_contents.update({(column, row): args[i + 1]})

        values = list(sheet_contents.values())

    return True


# @param col the column of the desired cell (first column is 'A', not 1 or 0)

# @param row the row of the desired cell (first row is 1, not 0)


# @return the value of the given cell found in contents.  It should not throw an error


#
def get_cell_value(col, row):
    cell = (str(col), str(row))
    if sheet_contents.get(cell) is None:
        return " "
    return sheet_contents.get(cell)


# does cellLabel refer to the cell at col, row?

# @param col (integer)
# @param row (integer)
# @param cellLabel a string, such as "B5"
# @return True if it does refer to that cell, False if not

#

def is_current(col, row, cellLabel):
    column = chr(col + 64)
    cell = (column, str(row))
    if cell == cellLabel:
        return True
    return False


# Print out the column headers for the spreadsheet, from 'A' through the last column
# specified in the user's range input. The column headers must be printed as specified in
# the sample output shown earlier, including a first empty cell for row labels.
# This should also print the row separator line preceding the column headers, but NOT
# the row separator line following the headers.
# @param lastColumn - the last column to print (first column is 'A', not 1 or 0)

# @param lastRow - the last data row to print (first data row is 1, not 0)

# @return None
#
def print_column_headers(last_column, last_row):
    print(format_row_separator(last_column))
    headers = "|   |"
    line = "|"
    i = 0
    while i <= last_column:
        headers = headers + chr(i + 65).center(9) + line.ljust(1)
        i += 1
    print(headers)


# format a row separator line of + and – characters as in the sample output.
# You should use string replication (string * int) to generate this for the
# appropriate number of columns, not a loop. This includes separators for the
# initial column of row labels.
# @param lastColumn - the last column to print (first column is 'A', not 1 or 0)


# @return the properly formatted separator line as a string
#
def format_row_separator(last_column):
    return "+---" + "+---------" * (int(last_column) + 1) + "+"


# Format the string for the contents of a data cell.  The contents must be exactly 9
# characters, justified properly for the type of data.  There should be a vertical bar
# column separator (|) preceding the contents.  If this is the last column, there should
# also be a vertical bar column separator following the contents. Thus, the total length
# of the string will be either 10 or 11 characters.
# @param column - the column of this cell (first column is 'A', not 1 or 0)

# @param row - the row for this cell (first row is 1, not 0)
# @return the formatted data cell string.
#
def format_data_cell(column, row):
    boarder = "|"
    data = str(get_cell_value(column, row))
    line = boarder.ljust(1) + data.center(9)
    if ord(column) - 65 == num_columns:
        line = line + boarder.ljust(1)

    return line


# Print a complete data row preceded by a row separator line. If this is the last row of
#  the spreadsheet, then also print a trailing row separator line
# @param row - the row to be printed (first row is 1, not 0)
# @return None
#
def print_data_row(row):
    print (format_row_separator(num_columns))
    boarder = "|"
    spaces = "         "
    line = "| " + str(row) + " |"
    for i in range(num_columns + 1):
        data = str(get_cell_value(chr(i + 65), row))
        if is_valid_integer(data):
            if data != "None":
                line = line + data.rjust(9) + boarder.ljust(1)
            else:
                line = line + spaces.center(9) + boarder.ljust(1)
        else:
            if data != "None":
                line = line + data.ljust(9) + boarder.ljust(1)
            else:
                line = line + spaces.center(9) + boarder.ljust(1)

    print(line)


# Print a complete spreadsheet based on the data in the 3 global variables.  You may
# assume at this point that all data in those variables has been validated.
# @return None
#
def print_sheet():
    print_column_headers(num_columns, num_rows)
    for i in range(num_rows):
        print_data_row(i + 1)
    print(format_row_separator(num_columns))


# Check all cell labels to make sure they are an upper-case character followed by
# an integer, and that both the column and row are within the specified range.

# @param input a list of strings consisting of sys.argv without
#               sys.argv[0] and sys.argv[1]

# @param lastCol last valid column (first column is 'A', not 1 or 0)

# @param lastRow last valid row number
# @return the first invalid cell label if there is one, otherwise None

#
def validate_all_cell_labels(input, lastCol, lastRow):
    for i in range(1, len(input), 2):
        string = input[i]
        if len(string) > 2:
            return string
        if ord(string[0]) < ord('A') or ord(string[0]) > lastCol + 65:
            return string
        if int(string[1]) < 1 or int(string[1]) > lastRow:
            return string
        if not string[0].isalpha() or not string[1].isdigit():
            return string
    return None


# MAJOR CHANGE SINCE LAST SEMESTER
# Checks all cell values to make sure they are printable in 9 characters or less
# @param input a list of strings consisting of sys.argv without
#               sys.argv[0] and sys.argv[1]
# @return the first invalid value if there is one, otherwise None
#
def validate_all_cell_values(input):
    for i in range(1, len(input), 2):
        string = str(input[i])
        if len(str(get_cell_value(string[0], string[1]))) > 9:
            return input[i + 1]
    return None


# Checks if strings input[0] and input[1] represent integers between 1 and 9
# @param input a list of strings that defaults to sys.argv
# @return True if range is OK, False otherwise
#
def validateRange(input=sys.argv):
    if len(str(input[2])) > 1:
        return False
    if ord(input[2]) < ord('1') or ord(input[2]) > ord('9') or ord(input[1]) < ord('A') or ord(input[1]) > ord('J'):
        return False
    return True


# Returns the integer form of a String or the String unchanged if not an integer
# @param arg the String which may or may not represent an integer

# @return the integer value if arg was a string representation of an integer,s
#         otherwise the arg unchanged


#
def get_integer(arg):
    if is_valid_integer(arg):
        return int(arg)
    else:
        return arg


# checks if the string arg represents an integer

# @param arg

# @return True if it's a valid double, False if not

#
def is_valid_integer(arg):
    if arg.isdigit():
        return True
    return False


# Initializes the spreadsheet and performs all required validation.
# If the validation passes, prints the spreadsheet.

# @param args defaults to sys.argv

# @return True if all validation passes, False if not
#
def main(args=sys.argv):
    if len(args) < 3:
        print("Invalid input: must specify at least highest column and row.")
        return False
    if (len(args) + 1) % 2 != 0:
        print("Invalid input: must specify the spreadsheet range, followed by cell-value pairs. You entered an odd "
              "number of inputs.")
        return False
    if not validateRange(args):
        print(
            "Please specify a valid spreadsheet range, with highest column between A and J and highest row as an integer between 1 and 9")
        return False
    init_spreadsheet(args)
    if validate_all_cell_labels(args[2:], num_columns, num_rows) is not None:
        print("Invalid cell label: " + validate_all_cell_labels(args[2:], num_columns, num_rows))
        return False
    if validate_all_cell_values(args[2:]) is not None:
        print("Invalid cell value: " + validate_all_cell_values(args[2:]))
        return False
    print_sheet()
    return True


if __name__ == "__main__":
    main(sys.argv)
