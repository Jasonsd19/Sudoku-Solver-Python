from math import floor

# Sample boards along with their solutions to test the program
board_hardest = [
    8, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 3, 6, 0, 0, 0, 0, 0,
    0, 7, 0, 0, 9, 0, 2, 0, 0,
    0, 5, 0, 0, 0, 7, 0, 0, 0,
    0, 0, 0, 0, 4, 5, 7, 0, 0,
    0, 0, 0, 1, 0, 0, 0, 3, 0,
    0, 0, 1, 0, 0, 0, 0, 6, 8,
    0, 0, 8, 5, 0, 0, 0, 1, 0,
    0, 9, 0, 0, 0, 0, 4, 0, 0
]

sol_hardest = [
    8, 1, 2, 7, 5, 3, 6, 4, 9,
    9, 4, 3, 6, 8, 2, 1, 7, 5,
    6, 7, 5, 4, 9, 1, 2, 8, 3,
    1, 5, 4, 2, 3, 7, 8, 9, 6,
    3, 6, 9, 8, 4, 5, 7, 2, 1,
    2, 8, 7, 1, 6, 9, 5, 3, 4,
    5, 2, 1, 9, 7, 4, 3, 6, 8,
    4, 3, 8, 5, 2, 6, 9, 1, 7,
    7, 9, 6, 3, 1, 8, 4, 5, 2
]

board_easy = [
    0, 0, 0, 2, 6, 0, 7, 0, 1,
    6, 8, 0, 0, 7, 0, 0, 9, 0,
    1, 9, 0, 0, 0, 4, 5, 0, 0,
    8, 2, 0, 1, 0, 0, 0, 4, 0,
    0, 0, 4, 6, 0, 2, 9, 0, 0,
    0, 5, 0, 0, 0, 3, 0, 2, 8,
    0, 0, 9, 3, 0, 0, 0, 7, 4,
    0, 4, 0, 0, 5, 0, 0, 3, 6,
    7, 0, 3, 0, 1, 8, 0, 0, 0
]

board_medium = [
    2, 4, 7, 0, 5, 0, 0, 0, 9,
    8, 3, 0, 9, 2, 0, 4, 5, 1,
    0, 0, 0, 4, 0, 3, 6, 7, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 8,
    0, 0, 2, 0, 0, 0, 1, 0, 5,
    7, 0, 0, 5, 0, 0, 0, 9, 6,
    0, 7, 3, 2, 0, 0, 0, 8, 0,
    0, 6, 5, 8, 0, 0, 0, 1, 0,
    1, 0, 0, 0, 0, 5, 9, 0, 0
]

sol = [
    2, 4, 7, 1, 5, 6, 8, 3, 9,
    8, 3, 6, 9, 2, 7, 4, 5, 1,
    5, 1, 9, 4, 8, 3, 6, 7, 2,
    3, 5, 1, 6, 9, 4, 7, 2, 8,
    6, 9, 2, 3, 7, 8, 1, 4, 5,
    7, 8, 4, 5, 1, 2, 3, 9, 6,
    9, 7, 3, 2, 6, 1, 5, 8, 4,
    4, 6, 5, 8, 3, 9, 2, 1, 7,
    1, 2, 8, 7, 4, 5, 9, 6, 3
]

# Index of board along with rows/columns/nonets for use in program
board_index = [
    0,  1,  2,  3,  4,  5,  6,  7,  8,
    9,  10, 11, 12, 13, 14, 15, 16, 17,
    18, 19, 20, 21, 22, 23, 24, 25, 26,
    27, 28, 29, 30, 31, 32, 33, 34, 35,
    36, 37, 38, 39, 40, 41, 42, 43, 44,
    45, 46, 47, 48, 49, 50, 51, 52, 53,
    54, 55, 56, 57, 58, 59, 60, 61, 62,
    63, 64, 65, 66, 67, 68, 69, 70, 71,
    72, 73, 74, 75, 76, 77, 78, 79, 80
]

col_1_index = [
    0, 9, 18, 27, 36, 45, 54, 63, 72
]

col_2_index = [
    1, 10, 19, 28, 37, 46, 55, 64, 73
]

col_3_index = [
    2, 11, 20, 29, 38, 47, 56, 65, 74
]

col_4_index = [
    3, 12, 21, 30, 39, 48, 57, 66, 75
]

col_5_index = [
    4, 13, 22, 31, 40, 49, 58, 67, 76
]

col_6_index = [
    5, 14, 23, 32, 41, 50, 59, 68, 77
]

col_7_index = [
    6, 15, 24, 33, 42, 51, 60, 69, 78
]

col_8_index = [
    7, 16, 25, 34, 43, 52, 61, 70, 79
]

col_9_index = [
    8, 17, 26, 35, 44, 53, 62, 71, 80
]

columns = [
    col_1_index, col_2_index, col_3_index,
    col_4_index, col_5_index, col_6_index,
    col_7_index, col_8_index, col_9_index
]

row_1_index = [
    0,  1,  2,  3,  4,  5,  6,  7,  8
]

row_2_index = [
    9,  10, 11, 12, 13, 14, 15, 16, 17
]

row_3_index = [
    18, 19, 20, 21, 22, 23, 24, 25, 26
]

row_4_index = [
    27, 28, 29, 30, 31, 32, 33, 34, 35
]

row_5_index = [
    36, 37, 38, 39, 40, 41, 42, 43, 44
]

row_6_index = [
    45, 46, 47, 48, 49, 50, 51, 52, 53
]

row_7_index = [
    54, 55, 56, 57, 58, 59, 60, 61, 62
]

row_8_index = [
    63, 64, 65, 66, 67, 68, 69, 70, 71
]

row_9_index = [
    72, 73, 74, 75, 76, 77, 78, 79, 80
]

rows = [
    row_1_index, row_2_index, row_3_index,
    row_4_index, row_5_index, row_6_index,
    row_7_index, row_8_index, row_9_index
]

nonet_1_index = [
    0, 1, 2,
    9, 10, 11,
    18, 19, 20
]

nonet_2_index = [
    3, 4, 5,
    12, 13, 14,
    21, 22, 23
]

nonet_3_index = [
    6, 7, 8,
    15, 16, 17,
    24, 25, 26
]

nonet_4_index = [
    27, 28, 29,
    36, 37, 38,
    45, 46, 47
]

nonet_5_index = [
    30, 31, 32,
    39, 40, 41,
    48, 49, 50
]

nonet_6_index = [
    33, 34, 35,
    42, 43, 44,
    51, 52, 53
]

nonet_7_index = [
    54, 55, 56,
    63, 64, 65,
    72, 73, 74
]

nonet_8_index = [
    57, 58, 59,
    66, 67, 68,
    75, 76, 77
]

nonet_9_index = [
    60, 61, 62,
    69, 70, 71,
    78, 79, 80
]

nonets = [
    nonet_1_index, nonet_2_index, nonet_3_index, 
    nonet_4_index, nonet_5_index, nonet_6_index,
    nonet_7_index, nonet_8_index, nonet_9_index
]

## Main Program ##

def solver(bd):
# Generative recursion, we generate and recurse over boards when needed
    if is_solved(bd):
        return bd
    else:
        return solver_bds(next_bds(bd))


def solver_bds(bds):
# Backtracking, the solver will try each branch and back track to an earlier branch when necessary
    for board in bds:
        try_path = solver(board)
        if try_path != "No Solution":
            return try_path
    return "No Solution"


def next_bds(bd):
# Generates the next set of possible board states, and returns only valid boards
    result = []
    index = get_empty_index(bd)
    for i in range(1, 10):
        copy = bd[:]
        copy[index] = i
        if is_valid_board(copy):
            result.append(copy)
    return result


def is_valid_board(bd):
# Checkes if the given board is valid by checking for duplicates in
# each row/column/nonet.
    for val, index in zip(bd, board_index):
        if val == 0:
            continue
        column = get_column(bd, index)
        row = get_row(bd, index)
        nonet = get_nonet_values(bd, index)
        if val in column or val in row or val in nonet:
            return False
    return True


def get_nonet_values(bd, index):
# Returns a list of current values for nonent that 
# includes the given index on the given board
    result = []
    for nonet in nonets:
        if index in nonet:
            nonet_indexes = nonet
    for i in nonet_indexes:
        if index == i:
            continue
        else:
            result.append(bd[i])
    return result


def get_column(bd, index):
# Returns a list of current values for column that 
# includes the given index on the given board
    this_position = position(index)
    result = []
    col_index = columns[this_position[0]]
    for i in col_index:
        if i == index:
            continue
        result.append(bd[i])
    return result


def get_row(bd, index):
# Returns a list of current values for row that 
# includes the given index on the given board
    this_position = position(index)
    result = []
    row_index = rows[this_position[1]]
    for i in row_index:
        if i == index:
            continue
        result.append(bd[i])
    return result


def get_empty_index(bd):
# Returns the next empty index on the board, if it exists
    for i in range(len(bd)):
        if bd[i] == 0:
            return i
    return False


def is_solved(bd):
# Checks if the board is solved
    return andmap(is_valid_value, bd)


def is_valid_value(num):
# Checks if the given value is valid (for Sudoku)
    valid_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    if num in valid_values:
        return True
    else:
        return False


def andmap(func, objs):
    for boolean in (func(obj) for obj in objs):
        if not boolean:
            return False
    return True


def position(index):
# Returns the position (column, row) equivalent
#  for the given index on a board
    column = index % 9
    row = floor(index / 9)
    return column, row


def print_board(bd):
# Helper function to print the board to terminal
    if bd == "No Solution":
        return "No Solution"
    line = ""
    counter = 0
    for val in bd:
        if counter % 3 == 0 and counter != 0:
            line += "| "
            if counter % 9 == 0 and counter != 0:
                line += "\n"
                if counter % 27 == 0:
                    line += "-----------------------" + "\n"
        line += str(val) + " "
        counter += 1
    return line + "|"

def int_str_to_list(row):
# Converts string of integers to list of integers
# Also checks if list contains valid Sudoku integers and is valid length
# Throws TypeError if any condition is not met
    result = []
    int_list = row.split()

    if len(int_list) != 9:
        raise TypeError

    for val in int_list:
        result.append(int(val))

    for val in result:
        if not input_is_valid_value(val):
            raise TypeError

    return result

def input_is_valid_value(num):
# Checks if the given value is valid (for Sudoku)
    valid_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    if num in valid_values:
        return True
    else:
        return False

def start_program():
    print("Welcome to the Sudoku solver!")
    print("Simply enter the values of the Sudoku board you wish to solve")
    print("starting from the first row of the board all the way to the last.")
    print("Make sure the values are separated by a space, use '0' for unknown/empty spaces.")
    print("For example, the input for the following board")
    print("")
    print(print_board(board_easy))
    print("")
    print("Would be: '0 0 0 2 6 0 7 0 1' for the first row and '7 0 3 0 1 8 0 0 0' for the last.")

    board = []
    for i in range(1,10):
        row = input("Please enter row number {s}: ".format(s = i))
        try:
            board += int_str_to_list(row)
        except:
            print("")
            print("Something went wrong!")
            print("Make sure you're entering the values correctly and try again.")
            input("Press any key to continue")
            print("")
            start_program()
            quit()

    print("Solving, this may take some time...")
    print("")
    print(print_board(solver(board)))



if __name__ == "__main__":
    start_program()
