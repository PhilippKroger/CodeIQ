'''
https://www.codewars.com/kata/529bf0e9bdf7657179000008/train/python
https://github.com/justinzhou93/Codewars-Python-practice/blob/master/Sudoku-solution-validator.py
'''


def valid_solution(board):
    k = 0

    vert_l = []
    for i in range(len(board)):  # Проверка по вертикали left
        if board[i][0] not in vert_l:
            vert_l.append(board[i][0])
            k += 1
        else:
            continue

    vert_r = []
    for i in range(len(board)):  # Проверка по вертикали right
        if board[i][8] not in vert_l:
            vert_l.append(board[i][8])
            k += 1
        else:
            continue

    vert_r_7 = []
    for i in range(len(board)):  # Проверка по вертикали right
        if board[i][7] not in vert_r_7:
            vert_r_7.append(board[i][7])
            k += 1
        else:
            continue

    vert_r_6 = []
    for i in range(len(board)):  # Проверка по вертикали right
        if board[i][6] not in vert_r_6:
            vert_r_6.append(board[i][6])
            k += 1
        else:
            continue

    vert_r_5 = []
    for i in range(len(board)):  # Проверка по вертикали right
        if board[i][5] not in vert_r_5:
            vert_r_5.append(board[i][5])
            k += 1
        else:
            continue

    vert_r_4 = []
    for i in range(len(board)):  # Проверка по вертикали right
        if board[i][4] not in vert_r_4:
            vert_r_4.append(board[i][4])
            k += 1
        else:
            continue

    vert_r_3 = []
    for i in range(len(board)):  # Проверка по вертикали right
        if board[i][3] not in vert_r_3:
            vert_r_3.append(board[i][3])
            k += 1
        else:
            continue

    vert_r_2 = []
    for i in range(len(board)):  # Проверка по вертикали right
        if board[i][2] not in vert_r_2:
            vert_r_2.append(board[i][2])
            k += 1
        else:
            continue

    vert_r_1 = []
    for i in range(len(board)):  # Проверка по вертикали right
        if board[i][1] not in vert_r_1:
            vert_r_1.append(board[i][1])
            k += 1
        else:
            continue

    if k == 180:
        return True
    else:
        return False


print(valid_solution(
    [[5, 3, 4, 6, 7, 8, 9, 1, 2],
     [6, 7, 2, 1, 9, 5, 3, 4, 8],
     [1, 9, 8, 3, 4, 2, 5, 6, 7],
     [8, 5, 9, 7, 6, 1, 4, 2, 3],
     [4, 2, 6, 8, 5, 3, 7, 9, 1],
     [7, 1, 3, 9, 2, 4, 8, 5, 6],
     [9, 6, 1, 5, 3, 7, 2, 8, 4],
     [2, 8, 7, 4, 1, 9, 6, 3, 5],
     [3, 4, 5, 2, 8, 6, 1, 7, 9]]
))
