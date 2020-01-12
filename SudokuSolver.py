class sudoku:
    def __init__(self,board):
        self.board = board
    def __str__(self):
        visual = ''
        for i in range(0,9):
            for j in range(0,9):
                visual += '| '+str(self.board[i][j].value)
            visual += ' |' + '\n'
            visual += "______________________________\n"
        return visual




class cell:
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return str(self.value)

while True:
    board = []
    given_board = [5,3,'.','.',7,'.','.','.','.',6,'.','.',1,9,5,'.','.','.','.',9,8,'.','.','.','.',6,'.',8,'.','.','.',6,'.','.','.',3,4,'.','.',8,'.',3,'.','.',1,7,'.','.','.',2,'.','.','.',6,'.',6,'.','.','.','.',2,8,'.','.','.','.',4,1,9,'.','.',5,'.','.','.','.',8,'.','.',7,9]
    counter =0
    for i in range(9):
        row = []
        for j in range(9):
            row.append(cell(given_board[counter]))
            counter += 1
        board.append(row)
        print(*board[i])
    
    sudoku = sudoku(board)
  
    print(sudoku)
    break