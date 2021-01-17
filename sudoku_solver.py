class Element:
    def __init__(self, x):
        self.index = x
        self.possible = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.number = 0

    def remove_impossible_from(self, r, c, s):
        self.possible = [
            x for x in self.possible if x not in r and x not in c and x not in s]
        if len(self.possible) == 1:
            self.number = self.possible.pop()

    def remove_impossible(self, n):
        if n in self.possible:
            self.possible.remove(n)

    def check_only_possible(self, row, col, sqr):
        for a in self.possible:
            cr = 0
            cc = 0
            cs = 0
            for r in row:
                if a in r.possible:
                    cr = cr+1
            for r in col:
                if a in r.possible:
                    cc = cc+1
            for r in sqr:
                if a in r.possible:
                    cs = cs+1
            if cr == 1 or cc == 1 or cs == 1:
                self.number = a
                self.possible = [-1]
                break


class Sudoku:
    def __init__(self):
        self.grid = [Element(q) for q in range(81)]

    def get_row(self, i):
        rows = [
            [0, 1, 2, 3, 4, 5, 6, 7, 8],
            [9, 10, 11, 12, 13, 14, 15, 16, 17],
            [18, 19, 20, 21, 22, 23, 24, 25, 26],
            [27, 28, 29, 30, 31, 32, 33, 34, 35],
            [36, 37, 38, 39, 40, 41, 42, 43, 44],
            [45, 46, 47, 48, 49, 50, 51, 52, 53],
            [54, 55, 56, 57, 58, 59, 60, 61, 62],
            [63, 64, 65, 66, 67, 68, 69, 70, 71],
            [72, 73, 74, 75, 76, 77, 78, 79, 80]
        ]
        for row in rows:
            if i in row:
                return [self.grid[q] for q in row]

    def get_column(self, i):
        cols = [
            [0, 9, 18, 27, 36, 45, 54, 63, 72],
            [1, 10, 19, 28, 37, 46, 55, 64, 73],
            [2, 11, 20, 29, 38, 47, 56, 65, 74],
            [3, 12, 21, 30, 39, 48, 57, 66, 75],
            [4, 13, 22, 31, 40, 49, 58, 67, 76],
            [5, 14, 23, 32, 41, 50, 59, 68, 77],
            [6, 15, 24, 33, 42, 51, 60, 69, 78],
            [7, 16, 25, 34, 43, 52, 61, 70, 79],
            [8, 17, 26, 35, 44, 53, 62, 71, 80]
        ]
        for col in cols:
            if i in col:
                return [self.grid[q] for q in col]

    def get_square(self, i):
        squares = [
            [0, 1, 2, 9, 10, 11, 18, 19, 20],
            [3, 4, 5, 12, 13, 14, 21, 22, 23],
            [6, 7, 8, 15, 16, 17, 24, 25, 26],
            [27, 28, 29, 36, 37, 38, 45, 46, 47],
            [30, 31, 32, 39, 40, 41, 48, 49, 50],
            [33, 34, 35, 42, 43, 44, 51, 52, 53],
            [54, 55, 56, 63, 64, 65, 72, 73, 74],
            [57, 58, 59, 66, 67, 68, 75, 76, 77],
            [60, 61, 62, 69, 70, 71, 78, 79, 80]
        ]
        for square in squares:
            if i in square:
                return [self.grid[q] for q in square]

    def print_sudoku(self):
        for q in range(0, 73, 9):
            k = self.grid[q:q+9]
            for a in k:
                print(a.number, end='  ')
            print('\n')
        #print([k.number for k in self.grid])
    
    def print_sudoku_from_list(self, ip):
        for q in range(0,73,9):
            k = ip[q:q+9]
            for a in k:
                print(a,end='  ')
            print('\n')
    
    def solve_sudoku(self, ip):
        for el in self.grid:
            el.number = ip[el.index]
        #self.print_sudoku()
        for el in self.grid:
            n = el.number
            ind = el.index
            if n != 0:
                el.possible = [-1]
                row = self.get_row(ind)
                for x in row:
                    x.remove_impossible(n)
                col = self.get_column(ind)
                for x in col:
                    x.remove_impossible(n)
                sqr = self.get_square(ind)
                for x in sqr:
                    x.remove_impossible(n)
        count = 0
        while 0 in [x.number for x in self.grid]:
            for el in self.grid:
                if el.number == 0:
                    row = self.get_row(el.index)
                    col = self.get_column(el.index)
                    sqr = self.get_square(el.index)
                    el.remove_impossible_from([q.number for q in row], [
                                              q.number for q in col], [q.number for q in sqr])
                    el.check_only_possible(row, col, sqr)
            count = count+1
            #print(count)
            #self.print_sudoku()
            #print([k.number for k in self.grid])
        print('number of iterations to solve the sudoku = ' + str(count))

        self.print_sudoku()
        
        return [k.number for k in self.grid]

# easy
#ip = [0,6,8,0,0,0,9,3,0,0,4,2,0,0,0,6,0,0,1,9,0,0,8,0,0,4,0,0,8,5,2,0,1,0,0,7,7,0,0,8,9,0,0,0,0,2,0,9,0,0,7,5,0,3,0,2,0,1,0,0,0,5,0,8,5,0,0,4,0,7,6,0,4,7,3,0,5,2,0,0,9]
# medium
#ip = [8,0,0,1,0,0,0,7,0,0,2,0,0,4,0,8,0,0,0,6,0,7,0,0,0,0,0,0,0,0,4,7,0,9,0,8,2,4,0,0,8,0,0,0,0,0,3,8,0,0,0,0,0,5,0,8,0,6,0,4,1,0,0,9,0,0,0,0,7,2,0,4,0,0,5,8,1,0,0,0,6]
# hard
#ip = [5,8,6,0,7,0,0,0,0,0,0,0,9,0,1,6,0,0,0,0,0,6,0,0,0,0,0,0,0,7,0,0,0,0,0,0,9,0,2,0,1,0,3,0,5,0,0,5,0,9,0,0,0,0,0,9,0,0,4,0,0,0,8,0,0,3,5,0,0,0,6,0,0,0,0,0,2,0,4,7,0]
# expert
# ip=[0,0,0,4,0,0,0,3,0,0,0,0,7,0,0,1,9,0,0,6,0,0,0,8,0,0,0,0,2,0,0,3,1,0,0,0,0,0,0,6,0,0,0,0,7,0,0,5,0,2,0,0,0,0,0,0,0,0,0,2,0,7,0,6,0,7,0,0,5,0,0,9,0,0,9,0,0,0,0,0,1]

if __name__ == '__main__':
    ip = [4, 2, 0, 0, 0, 3, 0, 8, 1, 0, 0, 1, 0, 0, 0, 0, 0, 3, 0, 7, 8, 0, 1, 5, 0, 6, 9, 0, 0, 0, 6, 0, 0, 0, 3, 5, 2, 5, 7, 0, 0, 0, 9, 4, 6, 0, 0, 0, 0, 0, 9, 0, 0, 8, 1, 9, 0, 2, 8, 4, 0, 0, 0, 7, 4, 5, 3, 0, 6, 0, 0, 2, 0, 0, 0, 1, 5, 0, 6, 0, 0]
    Sudoku().solve_sudoku(ip)