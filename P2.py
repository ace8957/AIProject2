print("hello world")
import math
#TODO: remember to add command-line parsing for the filename
class SudokuSolver:
    grid = []
    frontier = []
    currentNode = []
    rows = []
    columns = []
    squars = []
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
        #I'm wasting a bunch of memory doing this, but I want to make it
        #easier to code
        
    #A function which will update the programmer-friendly data structures
    #which contain the values in each row, column, and square
    def updateHelperStructures(self):
        sideLength = int(math.sqrt(len(self.grid)))
        l = []
        count = 0
        self.columns = [[] for j in range(sideLength)]
        for entry in self.grid:
            l.append(entry)
            self.columns[count].append(entry)
            count += 1
            if count == sideLength:
                self.rows.append(l)
                l = []
                count = 0

    #a function to test row parsing and print current values
    def printRows(self):
        for row in self.rows:
            s = ''
            for entry in row:
                s += entry
            print(row)
        
    def printGrid(self):
        sideLenght = int(math.sqrt(len(self.grid)))
        formatGrid = ''
        count = 0
        for entry in self.grid:
            if count == sideLenght:
                formatGrid += '\n'
                count = 0
            formatGrid += entry
            count += 1
        print(formatGrid)

sd = SudokuSolver('C:\\Users\\Adam\\workspace\\AIProject2\\state3.txt')
sd.parseFile()
sd.updateHelperStructures()
sd.printGrid()
print("Printing rows")
sd.printRows()