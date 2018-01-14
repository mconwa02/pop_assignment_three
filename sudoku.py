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
            
def getColumnLocations(columnNumber):
    """ Given a columnNumber, return a list of all nine "locations"
            (row, column) tuples in that column. """
    rows = list(range(0, 9))
    column = [columnNumber]*9
    return list(zip(rows, column))    


def getBoxLocations(location):
    """Return a list of all nine "locations"
        (row, column) tuples in the same box as the given location """
    if location[0] in [0,1,2] and location[1] in [0,1,2]:
        s = [0]*3+[1]*3+[2]*3
        t = [0,1,2]*3
        return list(zip(s, t))
    if location[0] in [0,1,2] and location[1] in [3,4,5]:
        s = [0]*3+[1]*3+[2]*3
        t = [3,4,5]*3
        return list(zip(s, t)) 
    if location[0] in [0,1,2] and location[1] in [6,7,8]:
        s = [0]*3+[1]*3+[2]*3
        t = [6,7,8]*3
        return list(zip(s, t))
    if location[0] in [3,4,5] and location[1] in [0,1,2]:
        s = [3]*3+[4]*3+[5]*3
        t = [0,1,2]*3
        return list(zip(s, t))
    if location[0] in [3,4,5] and location[1] in [3,4,5]:
        s = [3]*3+[4]*3+[5]*3
        t = [3,4,5]*3
        return list(zip(s, t))
    if location[0] in [3,4,5] and location[1] in [6,7,8]:
        s = [3]*3+[4]*3+[5]*3
        t = [6,7,8]*3
        return list(zip(s, t))
    if location[0] in [6,7,8] and location[1] in [0,1,2]:
        s = [6]*3+[7]*3+[8]*3
        t = [0,1,2]*3
        return list(zip(s, t))
    if location[0] in [6,7,8] and location[1] in [3,4,5]:
        s = [6]*3+[7]*3+[8]*3
        t = [3,4,5]*3
        return list(zip(s, t))
    if location[0] in [6,7,8] and location[1] in [6,7,8]:
        s = [6]*3+[7]*3+[8]*3
        t = [6,7,8]*3
        return list(zip(s, t))

def eliminate(problem, location, listOfLocations):
    """The given location in the array problem should contain a set containing a single number.
    For each location in the listOfLocations except location**, remove the number in location from the set in each other location.
    This function changes the array problem and returns a count of the number of eliminations (removals) actually made. """
    count = 0
    x = location[0]
    y = location[1]
    value = list(problem[x][y])[0]
    for u in range(len(listOfLocations)):
        tp = listOfLocations[u]
        s = tp[0]
        t = tp[1]           
        if value in problem[s][t]:
            count += 1
            problem[s][t].remove(value)      
    return count 

