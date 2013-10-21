import math
#TODO: remember to add command-line parsing for the filename
class SudokuSolver:

    MAX_LENGTH = 9
    
    rows = "ABCDEFGHI"
    columns = "123456789"
    potential_values = "123456789"
    indexes = [] #contains the row x colum index used to denote a tile
    grid = {} #contains the potential values of each of the tiles
    #squares = [[] for x in range(0,MAX_LENGTH)]
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
            self.remove_used_value(index, self.grid[index])

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
            
    #remove a value from the row, column, and square once it is taken
    def remove_used_value(self, index, value):
        row = index[0]
        column = index[1]
        square = self.get_square(index)
        #remove taken number from the same row and column
        for key in self.grid.keys():
            if key[0] == row or key[1] == column or square == self.get_square(key):
                if value in self.grid.get(key) and key != index:
                    self.grid[key] = self.remove_char_from_string(self.grid.get(key), value)

sd = SudokuSolver('C:\\Users\\Adam\\git\\AIProject2\\state3.txt')
sd.parseFile()
print(sd.grid)


