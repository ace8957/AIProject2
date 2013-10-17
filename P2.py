print("hello world")
import math
#TODO: remember to add command-line parsing for the filename
class SudokuSolver:
    grid = []
    statefile = ''
    def __init__(self, filename):    
        self.statefile = filename
        
    def parseFile(self):
        file = open(self.statefile, 'r')
        for line in file:
            #take each of the characters and place it into a list
            for char in line:
                #handle EOL char
                if char == '\n':
                    continue
                else:
                    #append the character to the grid list
                    self.grid.append(char)

    def printGrid(self):
        sideLenght = math.sqrt(len(self.grid))
        print(len(self.grid))
        formatGrid = ''
        count = 0
        for entry in self.grid:
            if count == sideLenght:
                formatGrid += '\n'
                count = 0
            else:
                formatGrid += entry
            count += 1
        print(formatGrid)
        
sd = SudokuSolver('C:\\Users\\Adam\\workspace\\AIProject2\\state3.txt')
sd.parseFile()
sd.printGrid()