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

def isSolved(problem):
    """ Given a 2D array problem of sets, return True if the Sudoku problem has been solved
        every set contains exactly one element) and False otherwise. """
    M = []
    for i in range(len(problem)):
        for j in range(len(problem[i])):
            if len(problem[i][j]) == 1:
                M.append('T') 
            else:
                M.append('F')
    if 'F' in M:
        ans = False
    if 'F' not in M:
        ans = True
    return ans

def listOfLocations(location):
    ListA = getRowLocations(location[0]) + getColumnLocations(location[1]) + getBoxLocations(location)
    setA = set(ListA)
    setA.remove(location)
    ListB = list(setA)
    return ListB

def solve(problem):
    """ Given a 2D array problem of sets, try to solve it.
        This function changes the array problem and returns True
        if the problem has been solved, False otherwise. """
    check = 0
    while check <= 81:
        check += 1
        for i in range(len(problem)):
            for j in range(len(problem[i])):
                if len(problem[i][j]) == 1:
                    location =(i, j)
                    eliminate(problem, location, listOfLocations(location))  
    return isSolved(problem)

def print_sudoku(problem):
    """ Prints the Sudoku array (given as a list of lists of integers)
        using dots to represent zeros """
    x = '+'
    y = '-'
    z = '|'
    a = ' .'
    f = (x + y*6)*3 + x
    L = []
    for i in range(len(problem)):
        for j in range(len(problem[i])):
            if problem[i][j]==0:
                L.append(' .') 
            else:
                L.append(' '+ str(problem[i][j]))
    print(f)
    print(z+str(L[0])+str(L[1])+str(L[2])+z+str(L[3])+str(L[4])+str(L[5])+z+str(L[6])+str(L[7])+str(L[8])+z)
    print(z+str(L[9])+str(L[10])+str(L[11])+z+str(L[12])+str(L[13])+str(L[14])+z+str(L[15])+str(L[16])+str(L[17])+z)
    print(z+str(L[18])+str(L[19])+str(L[20])+z+str(L[21])+str(L[22])+str(L[23])+z+str(L[24])+str(L[25])+str(L[26])+z)    
    print(f)
    print(z+str(L[27])+str(L[28])+str(L[29])+z+str(L[30])+str(L[31])+str(L[32])+z+str(L[33])+str(L[34])+str(L[35])+z)
    print(z+str(L[36])+str(L[37])+str(L[38])+z+str(L[39])+str(L[40])+str(L[41])+z+str(L[42])+str(L[43])+str(L[44])+z)
    print(z+str(L[45])+str(L[46])+str(L[47])+z+str(L[48])+str(L[49])+str(L[50])+z+str(L[51])+str(L[52])+str(L[53])+z)    
    print(f)
    print(z+str(L[54])+str(L[55])+str(L[56])+z+str(L[57])+str(L[58])+str(L[59])+z+str(L[60])+str(L[61])+str(L[62])+z)
    print(z+str(L[63])+str(L[64])+str(L[65])+z+str(L[66])+str(L[67])+str(L[68])+z+str(L[69])+str(L[70])+str(L[71])+z)
    print(z+str(L[72])+str(L[73])+str(L[74])+z+str(L[75])+str(L[76])+str(L[77])+z+str(L[78])+str(L[79])+str(L[80])+z)    
    print(f)
