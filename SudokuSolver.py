# contains board and method to display board
class sudoku:
    def __init__(self,board):
        self.board = board
    def __str__(self):
        visual = ""
        for i in range(0,9):
            for j in range(0,9):
                visual += str(self.board[i][j].value) + '  '
                if ((j+1) == 3) or ((j+1) == 6):
                    visual += "| "
            if ((i+1) == 3) or ((i+1) == 6):
                    visual += "\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _"    
            visual += '\n\n'
        return visual



# cell is a block in the board, cell object has a value and position 
class cell:
    def __init__(self,value,i,j):
        self.value = value
        self.possibilities ={1,2,3,4,5,6,7,8,9}
        self.row = i
        self.column = j
    def __str__(self):
        return str(self.value)
    
# get and set all the possibilities a cell has storing the final list in the cell's possibility param
def get_possibility(cell,sudoku):
    for c in sudoku.board[cell.row]:
        if c != cell and c.value != '.':
            cell.possibilities -= {c.value}
    for c in range(9):
        if c != cell.column and sudoku.board[c][cell.column] != '.':
            cell.possibilities -= {sudoku.board[c][cell.column].value}
    if cell.column < 3:
        start_col = 0
    elif cell.column < 6:
        start_col =  3
    else:
        start_col = 6

    if cell.row < 3:
        start_row = 0
    elif cell.row < 6:
        start_row =  3
    else:
        start_row = 6
    
    for r in range(start_row,start_row+3):
        for c in range(start_col,start_col+3):
            if sudoku.board[r][c] != cell and sudoku.board[r][c] != '.':
                cell.possibilities -= {sudoku.board[r][c].value}


# init - initial setup of board
board = []
given_board = [5,3,'.','.',7,'.','.','.','.',6,'.','.',1,9,5,'.','.','.','.',9,8,'.','.','.','.',6,'.',8,'.','.','.',6,'.','.','.',3,4,'.','.',8,'.',3,'.','.',1,7,'.','.','.',2,'.','.','.',6,'.',6,'.','.','.','.',2,8,'.','.','.','.',4,1,9,'.','.',5,'.','.','.','.',8,'.','.',7,9]
counter =0
for i in range(9):
    row = []
    for j in range(9):
        row.append(cell(given_board[counter],i,j))
        counter += 1
    board.append(row)

sudoku = sudoku(board)
    
print(sudoku)


# main logic
while True:
    for i in range(9):
        for j in range(9):
            if sudoku.board[i][j].value == '.':
                get_possibility(sudoku.board[i][j],sudoku)
                print(sudoku.board[i][j].possibilities)
    break


    