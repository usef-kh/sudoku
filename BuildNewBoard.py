from collections import defaultdict
import random


class GenerateBoard:
    def __init__(self):
        self.board = [['.'for _ in range(9)] for _ in range(9)]

        self.rows = defaultdict(set)
        self.cols = defaultdict(set)
        self.blocks = defaultdict(set)
        self.numList = list('123456789')
        self.indexList = list('02345678')
        self.board =  [[".", ".", "9", "7", "4", "8", ".", ".", "."],
             ["7", ".", ".", ".", ".", ".", ".", ".", "."],
             [".", "2", ".", "1", ".", "9", ".", ".", "."],
             [".", ".", "7", ".", ".", ".", "2", "4", "."],
             [".", "6", "4", ".", "1", ".", "5", "9", "."],
             [".", "9", "8", ".", ".", ".", "3", ".", "."],
             [".", ".", ".", "8", ".", "3", ".", "2", "."],
             [".", ".", ".", ".", ".", ".", ".", ".", "6"],
             [".", ".", ".", "2", "7", "5", "9", ".", "."]]

    def fillBoard(self, k):
        while k >0:
            num = random.choice(self.numList)
            r = int(random.choice(self.indexList))
            c = int(random.choice(self.indexList))
            if self.board[r][c] == '.':
                if num not in self.rows[r] and num not in self.cols[c] and num not in self.blocks[(r // 3, c // 3)] and len(self.blocks[(r // 3, c // 3)]) <= 5:
                    self.fill(c, r, num)
                    k -= 1

    def fill(self, c, r, v):
        self.board[r][c] = v
        self.rows[r].add(v)
        self.cols[c].add(v)
        self.blocks[(r // 3, c // 3)].add(v)

    def unfill(self, r, c, v):
        self.board[r][c] = '.'
        self.rows[r].remove(v)
        self.cols[c].remove(v)
        self.blocks[(r // 3, c // 3)].remove(v)

    def get_choices(self, r, c):
        choices = []
        for d in '123456789':
            if d not in self.rows[r] and d not in self.cols[c] and d not in self.blocks[(r // 3, c // 3)]:
                choices.append(d)
        return choices

    def get_empty_cell(self):
        empty = []

        for r in range(9):
            for c in range(9):
                if self.board[r][c] == '.':
                    choices = self.get_choices(r, c)
                    empty.append((r, c, choices))

        return min(empty, key=lambda x: len(x[2])) if empty else None

    def solve_board(self):
        empty = self.get_empty_cell()
        if not empty:
            return True
        else:
            r, c, choices = empty
            if not choices:
                return False

            for choice in choices:
                self.fill(r, c, choice)
                if self.solve_board():
                    return True
                else:
                    self.unfill(r, c, choice)
            return False


    def __str__(self):

        res = ''
        for i, row in enumerate(self.board):
            for j, value in enumerate(row):
                res += value + "  "
                if j == 2 or j == 5:
                    res += "| "
            if i == 2 or i == 5:
                res += "\n- - - - - - - - - - - - - - - -"

            res += '\n'
        return res


if __name__ == '__main__':
    genBoard = GenerateBoard()
    # genBoard.fill(0, 0, 1)
    # genBoard.fillBoard()

    # genBoard.fillBoard(45)
    print(genBoard)
    genBoard.solve_board()
    print(genBoard)


