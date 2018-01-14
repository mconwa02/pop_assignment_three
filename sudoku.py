def read_sudoku(file):
    """reads in files"""
    stream = open(file)
    data = stream.readlines()
    stream.close()
    return eval("".join(data))

def convertToSets(problem):
    """Converts a 2D array of integers into a 2D array of sets"""
    for i in range(len(problem)):
        for j in range(len(problem[i])):
            if problem[i][j] == 0:
                problem[i][j] = {1, 2, 3, 4, 5, 6, 7, 8, 9}
            else:
                problem[i][j] = {problem[i][j]}
    return problem

def convertToInts(problem):
    """Converts a 2D array of sets into 2D array of integers"""
    for i in range(len(problem)):
        for j in range(len(problem[i])):
            if len(problem[i][j]) == 1:
                problem[i][j] = list(problem[i][j])[0]
            elif len(problem[i][j]) == 0:
                problem[i][j] = 0
            else:
                problem[i][j] = 0
    return problem          

def getRowLocations(rowNumber):
    """Given a rowNumber, return a list of all nine "locations"
            (row, column) tuples in that row. """
    row = [rowNumber]*9
    columns = list(range(0, 9))
    return list(zip(row, columns))
