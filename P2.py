#TODO: remember to add command-line parsing for the filename
class SudokuSolver:

    MAX_LENGTH = 9
    rows = "ABCDEFGHI"
    columns = "123456789"
    potential_values = "123456789"
    indexes = [] #contains the row x colum index used to denote a tile
    grid = {} #contains the potential values of each of the tiles
    squares = [['A1','A2','A3','B1','B2','B3','C1','C2','C3'],
               ['D1','D2','D3','E1','E2','E3','F1','F2','F3'],
               ['G1','G2','G3','H1', 'H2','H3','I1','I2','I3'],
               ['A4','A5','A6','B4','B5','B6','C4','C5','C6'],
               ['D4','D5','D6','E4','E5','E6','F4','F5','F6'],
               ['G4','G5','G6','H4', 'H5','H6','I4','I5','I6'],
               ['A7','A8','A9','B7','B8','B9','C7','C8','C9'],
               ['D7','D8','D9','E7','E8','E9','F7','F8','F9'],
               ['G7','G8','G9','H7', 'H8','H9','I7','I8','I9']]
    
    def __init__(self, filename):    
        self.statefile = filename
        for c in self.rows:
            for d in self.columns:
                self.indexes.append(c+d)
                
    #a utility function to print a dict of potential values
    def print_grid(self, grid):
        print("---|---|---")
        count = 0
        lineCount = 0
        totalCount = 0
        for index in self.indexes:
            if lineCount >= 9:
                print()
                count = 0
                lineCount = 0
            elif count >= 3:
                print("|-", end='')
                count = 0
            print(grid[index] + "-", end='')
            count += 1
            lineCount += 1
            totalCount += 1
        print()
        print("Total Count: " + str(totalCount)) 

    #parsing the file will also create a dict which has the potential
    #values for each square included in it
    def parseFile(self):
        file = open(self.statefile, 'r')
        counter = 0
        elim = []
        for line in file:
            #take each of the characters and place it into a list
            for char in line:
                #handle EOL char
                if char == '\n':
                    continue
                else:
                    #append the character to the grid list
                    if char != '.':
                        self.grid[self.indexes[counter]] = char
                        elim.append(self.indexes[counter])
                    else:
                        self.grid[self.indexes[counter]] = self.potential_values
                    counter += 1
        for index in elim:
            self.grid = self.remove_used_value(self.grid, index, self.grid[index])

    #remove a provided character from a string and return the new string
    def remove_char_from_string(self, s, c):
        n  = ''
        if c not in s:
            return
        for char in s:
            if char != c:
                n += char
        return n

    def get_square(self, index):
        for x in range(0,self.MAX_LENGTH):
            if index in self.squares[x]:
                return x

    def is_valid_state(self, grid):
        for key in grid.keys():
            row = key[0]
            column = key[1]
            square = self.get_square(key)
            value = grid[key]
            if len(value) == 0:
                print("Failed min length check")
                return False
            elif len(value) > 9:
                print("Failed max length check")
                return False
            else:
                #check that the number does not already exist as a final value in row, column, square
                for k in grid.keys():
                    if (row == k[0] or k[1] == column or square == self.get_square(k)) and k != key:
                        if len(grid[k]) == 1 and grid[k] == value:
                            print("Failed row/column/square with key " + str(key) +" and offender " + str(k))
                            return False
        return True
                
    #remove a value from the row, column, and square once it is taken
    def remove_used_value(self, grid, index, value):
        row = index[0]
        column = index[1]
        square = self.get_square(index)
        #remove taken number from the same row and column
        for key in grid.keys():
            if key[0] == row or key[1] == column or square == self.get_square(key):
                if value in grid.get(key) and key != index:
                    grid[key] = self.remove_char_from_string(grid.get(key), value)
                    if len(grid[key]) == 1:
                        grid = self.remove_used_value(grid, key, grid[key])
        return grid     

    def is_win(self, grid):
        for value in grid.values():
            if len(value) != 1:
                return False
        return True

    def search(self, grid):
        potential_tiles = {}
        for key in grid.keys():
            if len(grid[key]) > 1:
                potential_tiles[key] = grid[key]
        for key in potential_tiles.keys():
            for num in potential_tiles[key]:
                new_grid = grid.copy()
                new_grid[key] = num
                self.remove_used_value(new_grid, key, new_grid[key])
                if self.is_valid_state(new_grid):
                    if self.is_win(new_grid):
                        self.grid = new_grid
                        return True
                    return self.search(new_grid)
                else:
                    return False

sd = SudokuSolver('C:\\Users\\Adam\\workspace\\AIProject2\\state0-1sol.txt')
sd.parseFile()
if sd.search(sd.grid) is False:
    print("No solution found.")
elif sd.is_win(sd.grid):
    print("We Won!")
sd.print_grid(sd.grid)
