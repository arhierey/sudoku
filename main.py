class Sudoku():
    def __init__(self):
        self.numbers = [[0, 0, 0, 0, 0, 0, 0, 0, 0] for i in range(9)]

    def __str__(self):
        return '\n'.join('|'.join(str(self.numbers[i][j]) for j in range(9)) for i in range(9))

    def generate(self):
        pass

    def solve(self):
        pass


sudoku = Sudoku()
print(sudoku)