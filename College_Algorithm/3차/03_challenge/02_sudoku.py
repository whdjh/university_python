#typing 모듈을 사용하면 numbers: list 대신 numbers:List[int]처럼 사용할 수 있다. 
#여기서 numbers: List[int]는 numbers가 리스트 자료형이고 각 요소는 모두 int형이어야 한다는 뜻이다. 
from typing import List

class Sudoku:
    def solve(self, sudoku_board: List[List[str]]) -> None:
        self.board = sudoku_board
        next_row, next_col = self.find_next_empty()
        if next_row == 9 and next_col == 9:
            return
        for i in range(1, 9):
            self.bfs(next_row, next_col, str(i))
    
    def check_row(self, row, num):
        for x in range(0, 9):
            if self.board[row][x] == num:
                return False
        return True
  
    def check_col(self, col, num):
        for y in range(0, 9):
            if self.board[y][col] == num:
                return False
        return True
  
    def check_33(self, row, col, num):
        box_x = int(col // 3) * 3
        box_y = int(row // 3) * 3
        for y in range (box_y, box_y + 3):
            for x in range (box_x, box_x + 3):
                if self.board[y][x] == num:
                    return False
        return True
  
    def find_next_empty(self):
        for y in range(0, 9):
            for x in range(0, 9):
                if self.board[y][x] == '0':
                    return [y, x]        
        return [9, 9]
    
    def bfs(self, row, col, num):
        if not self.check_row(row, num):
            return False
        elif not self.check_col(col, num):
            return False
        elif not self.check_33(row, col, num):
            return False
        self.board[row][col] = str(num)
        next_row,next_col = self.find_next_empty()    
        if next_row == 9 and next_col == 9:
            return True
    
        for next_num in range(1,10):
            if self.bfs(next_row, next_col, str(next_num)):
                return True

        self.board[row][col] = '0'
        return False

solver = Sudoku()

sudoku_quiz = \
[['0','5','1','3','0','9','0','0','6'],\
['0','2','0','8','7','1','3','4','5'],\
['0','0','0','2','0','0','0','0','0'],\
['2','1','9','7','6','4','0','3','0'],\
['0','0','0','1','3','0','0','0','0'],\
['7','3','0','0','0','8','0','6','2'],\
['5','0','0','4','2','0','0','0','3'],\
['0','0','0','9','1','5','0','0','7'],\
['1','9','0','0','0','0','2','0','0']]
solver.solve(sudoku_quiz)

for row in range (0, 9):
    print(sudoku_quiz[row])