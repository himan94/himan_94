board = []

for a in range(3):
    board.append(["."] * 3)

def print_board(board):
   for row in board:
       print " ".join(row)

print_board(board)

count = 0
m = 0
while m < 5:

    guess_row = int(raw_input("Player 1 Guess Row:"))
    guess_col = int(raw_input("player 1 Guess Col:"))
    r1 = guess_row -1
    c1 = guess_col -1
    board[r1][c1] = "X"
    count = count +1
    print_board(board)
    
    
    if(board[0][0] =="X" and board[1][0]=="X" and board[2][0]=="X") or \
    (board[0][1] =="X" and board[1][1]=="X" and board[2][1]=="X") or \
    (board[0][2] =="X" and board[1][2]=="X" and board[2][2]=="X") or \
    (board[0][0] =="X" and board[0][1]=="X" and board[0][2]=="X") or \
    (board[1][0] =="X" and board[1][1]=="X" and board[1][2]=="X") or \
    (board[2][0] =="X" and board[2][1]=="X" and board[2][2]=="X") or \
    (board[0][0] =="X" and board[1][1]=="X" and board[2][2]=="X") or \
    (board[0][2] =="X" and board[1][1]=="X" and board[2][0]=="X"):
        print"player 1 wins"
        break
    elif(board[0][0] =="0" and board[1][0]=="0" and board[2][0]=="0") or \
    (board[0][1] =="0" and board[1][1]=="0" and board[2][1]=="0") or \
    (board[0][2] =="0" and board[1][2]=="0" and board[2][2]=="0") or \
    (board[0][0] =="0" and board[0][1]=="0" and board[0][2]=="0") or \
    (board[1][0] =="0" and board[1][1]=="0" and board[1][2]=="0") or \
    (board[2][0] =="0" and board[2][1]=="0" and board[2][2]=="0") or \
    (board[0][0] =="0" and board[1][1]=="0" and board[2][2]=="0") or \
    (board[0][2] =="0" and board[1][1]=="0" and board[2][0]=="0"):
        print"player 2 wins"
        break

    if count == 9:
        print"its a draw"
        break
    
    guess_ro = int(raw_input("Player 2 Guess Row:"))
    guess_co = int(raw_input("Player 2 Guess Col:"))
    r2 = guess_ro -1
    c2 = guess_co -1
    board[r2][c2] = "0"
    count = count+1
    print_board(board)
    m = m+1
            


    
    
    
