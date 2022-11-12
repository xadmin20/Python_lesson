#coding: utf8
X="X"
O="O"
EMPTY=' '
TIE="Ничья"


def ask_yes_no(question):
    """Задает вопросы с ответом 'Да' или'Нет".    """
    response=None
    while response not in("y","n"):
        response=input(question).lower()
    return response


def ask_number(question, low, high):
    """Просит ввести число из диапазона."""
    response=None
    while response not in range(low,high):
        response=int(input(question))
    return response

def pieces():
    go_first=ask_yes_no("Хочешь оставить за собой первый ход?(y/n): ")
    if go_first=="y":
        print ("\n Ну что ж ,даю тебе фору играй крестиками")
        human = X
        computer = O
    else:
        print("\n Спасибо за то чтопредоставил перове право  хода компьютеру")
        computer = X
        human = O
    return computer, human

def new_board():
    "Создает новую игровую доску"
    board = []
    for square in range(9):
        board.append(" ")
    return board
def  display_board(board):
    print("\n\t", board[0], "|", board[1],"|",board[2])
    print("\t",  "---------")
    print("\n\t", board[3], "|", board[4],  "|", board[5])
    print("\t",  "---------")
    print("\n\t", board[6], "|", board[7],  "|",  board[8],"\n")

def legal_moves(board):
    """Создает список доступных ходов """
    moves=[]
    for square in range(9):
        if board[square] == " ":
            moves.append(square)
    return moves
def winner(board):
    """Определяет победителя в игре """
    WAYS_TO_WIN=((0,1,2),
                 (3,4,5),
                 (6,7,8),
                 (0,3,6),
                 (1,4,7),
                 (2,5,8),
                 (0,4,8),
                 (2,4,6))
    for row in WAYS_TO_WIN:
        if board[row[0]]==board[row[1]]==board[row[2]] !=" ":
            winner=board[row[0]]
            return winner
        if EMPTY not in board:
            return TIE
    return None

def human_move(board,human):
    legal=legal_moves(board)
    move=None
    while move not in legal:
        move=ask_number("Ваш ход.",0, 9)
        if move not in legal:
            print ("\nЭто поле уже занято. Выберие другое поле.\n")
    print("Хорошо.....")
    return move
def computer_move(board, computer, human):
    board=board[:]
    #поля от лучшего к худшему
    BEST_MOVES=[4,0,2,6,8,1,3,5,7]
    print("Мой выбор", end=" ")
    for move in legal_moves(board):
        board[move]=computer
        if winner(board)==computer:
            print(move)
            return move
        board[move]=" "
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move
def next_turn(turn):
    if turn==X:
        return O
    else:
        return X
def congrat_winner(the_winner, computer, human):
    if the_winner !=TIE:
        print("Три",the_winner,"в ряд!\n")
    else:
        print("Ничья!\n")
    if the_winner == computer:
        print("Победил кмопьютер!")
    elif the_winner==human:
        print("Поздравляю,Вы победили компьютер!")
    elif the_winner==TIE:
        print("Ничья!")
def main():
    computer, human =pieces()
    turn = X
    board = new_board()
    display_board(board)
    while not winner(board):
        if turn == human:
            move = human_move(board,human)
            board[move] = human
        else:
            move = computer_move(board,computer,human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)
    the_winner = winner(board)
    congrat_winner(the_winner,computer,human)

main()
input("\n\nНажмите Enter, чтобы выйти.")