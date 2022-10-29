import random as rnd


def print_matrix(matrix):
    for index in range(len(matrix)):
        print(matrix[index])


def whats_missing(numbers):
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    missing = []
    for index in range(9):
        if nums[index] not in numbers:
            missing.append(nums[index])
    return missing


def get_cell(matrix, row, column):
    cell = []
    cols, rows = [], []
    if row < 3:
        rows = [0, 1, 2]
    elif 3 <= row < 6:
        rows = [3, 4, 5]
    elif 6 <= row <= 9:
        rows = [6, 7, 8]

    if column < 3:
        cols = [0, 1, 2]
    elif 3 <= column < 6:
        cols = [3, 4, 5]
    elif 6 <= column <= 9:
        cols = [6, 7, 8]

    cell.extend([matrix[rows[0]][index] for index in cols])
    cell.extend([matrix[rows[1]][index] for index in cols])
    cell.extend([matrix[rows[2]][index] for index in cols])
    return cell


def rules_checker(matrix, row, column):
    numbers = []
    line0 = [matrix[row][index] for index in range(9)]
    line1 = [matrix[index][column] for index in range(9)]
    cell = get_cell(matrix, row, column)

    numbers.extend(line0)
    numbers.extend(line1)
    numbers.extend(cell)

    missing = whats_missing(numbers)

    new_num = 0

    if matrix[row][column] == 0:
        if len(missing) != 0:
            new_num = rnd.choice(whats_missing(numbers))
        matrix[row][column] = new_num
    return matrix


square = [[0, 0, 0, 0, 0, 0, 0, 0, 0] for i in range(9)]
print_matrix(square)
print('-->')

cond = [0 in square[index] for index in range(9)]
while any(cond):
    square = [[0, 0, 0, 0, 0, 0, 0, 0, 0] for i in range(9)]
    for i in range(9):
        for j in range(9):
            square = rules_checker(square, i, j)
    cond = [0 in square[index] for index in range(9)]

print_matrix(square)
