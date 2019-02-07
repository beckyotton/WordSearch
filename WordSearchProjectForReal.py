from random import*

def createletters(letter):
    for m in range(0, 26):
        letter.append(alphabet)


def createboard(level, option):
    print("function1")
    if option.lower() == "easy":
        level = 7
    elif option.lower() == "medium":
        level = 9
    elif option.lower() == "hard":
        level = 12
    for i in range(0, level):
        board.append([])
        for j in range(0, level):
            board[i].append(" ")
    return level


def word(lines, choose):
    while choose < level:
        randomnum = randint(0, 99)
        wordC = lines[randomnum]
        if word not in chosen:
            chosen.append(wordC.strip())
            choose = choose + 1

def addwords(level):
    print("func3")
    for i in range(0, level):
        walk = 1
        direction = randint(1, 2)
        while walk == 1:
            xlocation = randint(0, level - len(chosen[i]))
            ylocation = randint(0, level - 1)
            if len(chosen[i]) == 3:
                if board[ylocation][xlocation] == " " and board[ylocation][xlocation + 1] == " " and board[ylocation][xlocation + 2] == " ":
                    splitword = list(chosen[i])
                    if direction == 1:
                        for j in range(0, len(splitword)):
                            board[ylocation][xlocation+j] = (splitword[j])
                    else:
                        for j in range(0, len(splitword)):
                            board[ylocation][xlocation + 2 - j] = (splitword[j])
                walk = 2
            elif len(chosen[i]) == 4:
                if board[ylocation][xlocation] == " " and board[ylocation][xlocation + 1] == " " and board[ylocation][xlocation+2] == " " and board[ylocation][xlocation+3] == " ":
                    splitword = list(chosen[i])
                    if direction == 1:
                        for j in range(0, len(splitword)):
                            board[ylocation][xlocation + j] = (splitword[j])
                    else:
                        for j in range(0, len(splitword)):
                            board[ylocation][xlocation + 3 - j] = (splitword[j])
                walk = 2
            elif len(chosen[i]) == 5:
                if board[ylocation][xlocation] == " " and board[ylocation][xlocation + 1] == " " and board[ylocation][xlocation + 2] == " " and board[ylocation][xlocation + 3] == " " and board[ylocation][xlocation + 4]:
                    splitword = list(chosen[i])
                    if direction == 1:
                        for j in range(0, len(splitword)):
                            board[ylocation][xlocation + j] = (splitword[j])
                    else:
                        for j in range(0, len(splitword)):
                            board[ylocation][xlocation + 4 - j] = (splitword[j])
                walk = 2
            elif len(chosen[i]) == 6:
                if board[ylocation][xlocation] == " " and board[ylocation][xlocation + 1] == " " and board[ylocation][xlocation + 2] == " " and board[ylocation][xlocation + 3] == " " and board[ylocation][xlocation + 4] and board[ylocation][xlocation + 5] == "0":
                    splitword = list(chosen[i])
                    if direction == 1:
                        for j in range(0, len(splitword)):
                            board[ylocation][xlocation + j] = (splitword[j])
                    else:
                        for j in range(0, len(splitword)):
                            board[ylocation][xlocation + 5 - j] = (splitword[j])
                walk = 2


def addletters(level, letter):
    for x in range(0, level):
        for y in range(0, level):
            v = randint(0, 1)
            if board[x][y] == ' ':
                board[x][y] = letter[v]


def user(found):
    
'''
def add():
    length =
    for i in range (0, length):
'''


pick = 1
level = 0
randomnum = 0
choose = 0
board = []
chosen = []
splitword = []
letter = ['x', 'x']
lines = open("words.txt", "r").readlines()
alphabet = open("alphabet.txt", "r").readlines()
#letter.append(alphabet.strip())
print(letter)
'''
option = input("Choose level: Easy, Medium, Hard.\n")
while option.lower() != "easy" and option.lower() != "medium" and option.lower() != "hard":
    option = input("Choose level: Easy, Medium, Hard.\n")
'''
while True:
    option = input("Choose level: Easy, Medium, Hard.\n").lower()
    if option == 'easy' or option == 'medium' or option == 'hard':
        print("good")
        break
    else:
        print("bad")

level = createboard(level, option)
word(lines, choose)
addwords(level)
print(chosen)
addletters(level, letter)

for i in range(level):
    print(board[i])
