def make_board(width, height):
    b = []
    for row in range (0, height):
        b.append([" "] * width)
    return b

def token(col, player, board):
    if board[0][col] != " ":
        return
    for row in range(1,len(board)):
        if board[row][col] != " ":
            board[row - 1][col] = player
            return
    board[row][col] = player

game_b = make_board(7,6)
token(2, "G", game_b)
token(4, "B", game_b)
token(2, "G", game_b) 
token(2, "B", game_b) 
