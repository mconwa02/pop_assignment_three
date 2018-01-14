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
