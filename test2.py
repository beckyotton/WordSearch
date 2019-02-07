from random import *
level = 7
board = []
for i in range(0, level):
    board.append([])
    for j in range(0, level):
        board[i].append(" ")

chosen = ["tests", "tests", "tests", "tests", "tests", "tests", "tests"]

for i in range(0, level):
    walk = 1
    direction = randint(1, 2)
    while walk == 1:
        if len(chosen[i]) == 5:
            xlocation = randint(0, level - 5)
            ylocation = randint(0, level - 1)
            if board[ylocation][xlocation] == " " and board[ylocation][xlocation + 1] == " " and board[ylocation][xlocation + 2] == " " and board[xlocation][ylocation + 3] == " " and board[xlocation][ylocation + 4] == " ":
                splitword = list(chosen[i])
                if direction == 1:
                    for j in range(0, len(splitword)):
                        board[ylocation][xlocation + j] = (splitword[j])
                else:
                    for j in range(0, len(splitword)):
                        board[ylocation][xlocation + 4 - j] = (splitword[j])
                walk = 2

print(board)