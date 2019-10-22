import random
import copy


def DrawBoard(Board):
    print(Board[0][0] + '|' + Board[0][1] + '|' + Board[0][2])
    print('-+-+-')
    print(Board[1][0] + '|' + Board[1][1] + '|' + Board[1][2])
    print('-+-+-')
    print(Board[2][0] + '|' + Board[2][1] + '|' + Board[2][2])
    print()

def Who_are_Player1_Player2():
    if random.randint(0, 1) == 0:
        print("Computer player goes first.")
        Player1 = ComputerPlayer        
        Player2 = HumanPlayer     
    else:
        print("Human player goes first.")
        Player2 = ComputerPlayer        
        Player1 = HumanPlayer           
    return Player1, Player2


def IsSpaceFree(Board, i ,j):
    if i < 0 or i >= 3 or j < 0 or j >=  3:
        return False
    if Board[i][j] == ' ':
        return True
    else:
        return False


def GetNumberOfChessPieces(Board):
    n=0
    for i in range(0, 3):
        for j in range(0, 3):
            if Board[i][j] == 'X' or Board[i][j] == 'O':
                n+=1
    return n


def UpdateBoard(Board, Tag, Choice):
    row = Choice[0]
    col = Choice[1]
    Board[row][col] = Tag


def HumanPlayer(Tag, Board):
    while True:
        print("Make your choice")
        try:
            row = int(input("row = "))
            col = int(input("col = "))
            if IsSpaceFree(Board, row, col) is False:
                print("This space is occupied")
            else:
                break
        except ValueError:
            print("That is not valid number.")
    print("HumanPlayer("+Tag+") has made the choice")
    return (row, col)


def ComputerPlayer(Tag, Board):     
    if IsBoardEmpy(Board) == True:
        print("ComputerPlayer("+Tag+") has made the choice")
        ChoiceOfComputerPlayer = (0, 0)
        return ChoiceOfComputerPlayer

    row_best, col_best = -1, -1
    for i in range(0, 3):
        for j in range(0, 3):
            if IsSpaceFree(Board, i, j):
                NewBoard = copy.deepcopy(Board)
                NewBoard[i][j]='X'
                OutCome = Judge(NewBoard)
                if OutCome == 1:
                    row_best, col_best = i, j
                    break
                NewBoard[i][j]='O'
                OutCome = Judge(NewBoard)
                if OutCome == 2:
                    row_best, col_best = i, j
                    break
    if row_best >= 0 and col_best >= 0:
        ChoiceOfComputerPlayer = (row_best, col_best)
    else: 
        while True:
            row = random.randint(0, 3)
            col = random.randint(0, 3)
            if IsSpaceFree(Board, row, col):
                ChoiceOfComputerPlayer = (row, col)
                break
    print("ComputerPlayer("+Tag+") has made the choice")
    return ChoiceOfComputerPlayer


def Judge(Board):
    Outcome = 0
    for L in ['X', 'O']:
        Result = ((Board[0][0]==L and Board[0][1]==L and Board[0][2]==L) or
                  (Board[1][0]==L and Board[1][1]==L and Board[1][2]==L) or
                  (Board[2][0]==L and Board[2][1]==L and Board[2][2]==L) or
                  (Board[0][0]==L and Board[1][0]==L and Board[2][0]==L) or
                  (Board[0][1]==L and Board[1][1]==L and Board[2][1]==L) or
                  (Board[0][2]==L and Board[1][2]==L and Board[2][2]==L) or 
                  (Board[0][0]==L and Board[1][1]==L and Board[2][2]==L) or 
                  (Board[0][2]==L and Board[1][1]==L and Board[2][0]==L))   
        if Result is True:
            if L is 'X':
                Outcome = 1
            else:
                Outcome = 2            
    if IsBoardFull(Board) == True:
        Outcome = 3
    return Outcome


def ShowOutcome(Outcome, Name1, Name2):
    if Outcome is 0:
        print("The game is still in progress")
    elif Outcome is 1:
         print(Name1, "wins the game!")
    elif Outcome is 2:
         print(Name2, "wins the game!")
    else:
        print("It is a tie!")


def TicTacToeGame():
    print("Wellcome to Tic Tac Toe")
    Board = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]
    DrawBoard(Board)

    Player1, Player2 = Who_are_Player1_Player2()

    while True:
        Choice1=Player1('X', Board)
        UpdateBoard(Board, 'X', Choice1)
        DrawBoard(Board)
        Outcome = Judge(Board)
        ShowOutcome(Outcome, Player1.__name__, Player2.__name__)
        if Outcome != 0:
            break
        Choice2 = Player2('O', Board)
        UpdateBoard(Board, 'O', Choice2)
        DrawBoard(Board)
        Outcome = Judge(Board)
        ShowOutcome(Outcome, Player1.__name__, Player2.__name__)
        if Outcome != 0:
            break

def IsBoardFull(Board):
    return (GetNumberOfChessPieces(Board) == 9)


def IsBoardEmpy(Board):
    return (GetNumberOfChessPieces(Board) == 0)


def PlayGame():
    while True:
        TicTacToeGame()
        print('Do you want to play again? (yes or no)')
        if not input().lower().startswith('y'):
            break
    print("GameOver")

PlayGame()            
