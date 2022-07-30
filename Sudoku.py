import random as rand

class Board:

    grid = [['.' for i in range(9)] for j in range(9)]

    def print(self):
            for i in range(len(self.grid)):
                if i % 3 == 0 and i != 0:
                    print("- - - - - - - - - - - ")

                for j in range(len(self.grid[0])):
                    if j % 3 == 0 and j != 0:
                     print("| ", end="")

                    if j == 8:
                         print(self.grid[i][j])
                    else:
                        print(str(self.grid[i][j]) + " ", end="")
            print("\n")

    def __nextEmpty(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == '.':
                    return (i, j)  # _y, _x

        return None
    
    def isValid(self, num, pos):

        for i in range(len(self.grid[0])):
            if self.grid[pos[0]][i] == num and pos[1] != i:
                return False

        for i in range(len(self.grid)):
            if self.grid[i][pos[1]] == num and pos[0] != i:
                return False

        _x = pos[1] // 3
        _y = pos[0] // 3

        for i in range(_y*3, _y*3 + 3):
            for j in range(_x * 3, _x*3 + 3):
                if self.grid[i][j] == num and (i,j) != pos:
                    return False

        return True


    def generate(self, difficulty): 
        self.grid = [['.' for i in range(9)] for j in range(9)]

        _l = list(range(1, 10))
        for _y in range(3):
            for _x in range(3):
                _num = rand.choice(_l)
                self.grid[_y][_x] = _num
                _l.remove(_num)

        _l = list(range(1, 10))
        for _y in range(3, 6):
            for _x in range(3, 6):
                _num = rand.choice(_l)
                self.grid[_y][_x] = _num
                _l.remove(_num)

        _l = list(range(1, 10))
        for _y in range(6, 9):
            for _x in range(6, 9):
                _num = rand.choice(_l)
                self.grid[_y][_x] = _num
                _l.remove(_num)
            
        self.solve(self)
        self.removeNumbers(self, difficulty)

    def removeNumbers(self, difficulty): 
            
        if difficulty == 0:
            _squares_to_remove = 36
        elif difficulty == 1:
            _squares_to_remove = 46
        elif difficulty == 2:
            _squares_to_remove = 52
        else:
            return

        _counter = 0
        while _counter < 4:
            _y = rand.randint(0, 2)
            _x = rand.randint(0, 2)
            if self.grid[_y][_x] != '.':
                self.grid[_y][_x] = '.'
                _counter += 1

        _counter = 0
        while _counter < 4:
            _y = rand.randint(3, 5)
            _x = rand.randint(3, 5)
            if self.grid[_y][_x] != '.':
                self.grid[_y][_x] = '.'
                _counter += 1

        _counter = 0
        while _counter < 4:
            _y = rand.randint(6, 8)
            _x = rand.randint(6, 8)
            if self.grid[_y][_x] != '.':
                self.grid[_y][_x] ='.'
                _counter += 1

        _squares_to_remove -= 12
        _counter = 0
        while _counter < _squares_to_remove:
            _y = rand.randint(0, 8)
            _x = rand.randint(0, 8)

            if self.grid[_y][_x] != '.':
                self.grid[_y][_x] = '.'
                _counter += 1

        return self.grid

    def solve(self):
        _find = self.__nextEmpty(self)
        if not _find:
            return True
        else:
            _y, _x = _find

        for i in range(1,10):
            if self.isValid(self, i, (_y, _x)):
                self.grid[_y][_x] = i

                if self.solve(self):
                    return True

                self.grid[_y][_x] = '.'

        return False

