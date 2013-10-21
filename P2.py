import math
#TODO: remember to add command-line parsing for the filename
class SudokuSolver:

    rows = "ABCDEFGHI"
    columns = "123456789"
    potential_values = "123456789"
    indexes = [] #contains the row x colum index used to denote a square
    grid = {} #contains the potential values of each of the squares
    
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

    #remove a value from the row, column, and square once it is taken
    def remove_used_value(self, index, value):
        row = index[0]
        column = index[1]
        #remove taken number from the same row and column
        for key in self.grid.keys():
            if key[0] == row or key[1] == column:
                if value in self.grid.get(key) and key != index:
                    self.grid[key] = self.remove_char_from_string(self.grid.get(key), value)

sd = SudokuSolver('C:\\Users\\Adam\\git\\AIProject2\\state3.txt')
sd.parseFile()
print(sd.grid)


