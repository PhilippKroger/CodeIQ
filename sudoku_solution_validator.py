'''
https://www.codewars.com/kata/529bf0e9bdf7657179000008/train/python
https://github.com/justinzhou93/Codewars-Python-practice/blob/master/Sudoku-solution-validator.py
'''


def valid_solution(board):
    k = 0

    for i in range(len(board)):  # Проверка по горизонтали
        if len(board[i]) == len(set(board[i])):
            k += 1
        else:
            return False
    vert_l = []
    for i in range(len(board)):  # Проверка по вертикали left
        if board[i][0] not in vert_l:
            vert_l.append(board[i][0])
            k += 1
        else:
            continue

    for i in range(len(board)):  #
        for j in range(i+1, len(board)):
            if board[i][i] != board[j][j]:
                print(board[i], board[j], board[i][i], board[j][j])
            else:
                continue

    vert_r = []
    for i in range(len(board)):  # Проверка по вертикали right
        if board[i][8] not in vert_l:
            vert_l.append(board[i][8])
            k += 1
        else:
            continue

    if k == 18:
        return True
    else:
        return False


print(valid_solution(
    [[1, 2, 3, 4, 5, 6, 7, 8, 9]
        , [2, 3, 4, 5, 6, 7, 8, 9, 1]
        , [3, 4, 5, 6, 7, 8, 9, 1, 2]
        , [4, 5, 6, 7, 8, 9, 1, 2, 3]
        , [5, 6, 7, 8, 9, 1, 2, 3, 4]
        , [6, 7, 8, 9, 1, 2, 3, 4, 5]
        , [7, 8, 9, 1, 2, 3, 4, 5, 6]
        , [8, 9, 1, 2, 3, 4, 5, 6, 7]
        , [9, 1, 2, 3, 4, 5, 6, 7, 8]]
))
