
class SudokuSolver:
    board = [[0, 7, 0, 9, 0, 4, 5, 0, 1],
             [0, 0, 0, 0, 0, 7, 6, 0, 0],
             [0, 0, 0, 6, 1, 3, 0, 0, 7],
             [0, 5, 7, 0, 0, 2, 0, 9, 6],
             [3, 0, 6, 7, 0, 5, 2, 0, 0],
             [0, 8, 0, 1, 9, 0, 7, 0, 0]]

   # board = [[0, 7, 0, 9, 0, 4, 5, 0, 1],
    #         [0, 0, 0, 0, 0, 7, 6, 0, 0],
     #        [0, 0, 0, 6, 1, 3, 0, 0, 7],
      #       [0, 5, 7, 0, 0, 2, 0, 9, 6],
       #      [3, 0, 6, 7, 0, 5, 2, 0, 0],
        #     [0, 8, 0, 1, 9, 0, 7, 0, 0],
         #    [0, 1, 0, 0, 0, 0, 0, 6, 2],
          #   [9, 2, 8, 5, 0, 1, 0, 0, 4],
           #  [0, 6, 0, 4, 0, 0, 0, 8, 5]]

    def is_valid_row(self, row, check_value):
        for val in self.board[row]:
            if check_value == val:
                return False

        return True

    def is_valid_column(self, col,  check_value):
        for i in range(0, len(self.board)):
            if check_value == self.board[i][col]:
                return False

        return True

    def is_valid_area(self, row, col, check_value):
        row = int((row // 3.5) * 3)
        col = int((col // 3.5) * 3)
        for i in range(0, 3):
            for j in range(0, 3):
                if check_value == self.board[row + i][col + j]:
                    #print("row "+str(row+i)+" col "+str(col+j)+" Check value is "+str(check_value) +" board value "+str(self.board[row + i][col + j]))
                    return False

        return True

    def is_valid_placement(self, row, col, check_value):
        return self.is_valid_row(row, check_value) and self.is_valid_column(col, check_value) and self.is_valid_area(row, col, check_value)

    def solve(self, row, col):
        if col == len(self.board[row]):
            col = 0
            row = row + 1

            if row == len(self.board):
                return True

        if self.board[row][col] != 0:
            return self.solve(row, col+1)

        for value in range(1, 10):
            if self.is_valid_placement(row, col, value):
                self.board[row][col] = value
                if self.solve(row, col+1):
                    return True

        return False


    def print_board(self):
        for row in self.board:
            print(row)



if __name__ == '__main__':
    sudoku_solver = SudokuSolver()
    sudoku_solver.solve(0, 0)
    sudoku_solver.print_board()

    