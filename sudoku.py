def read_sudoku(file):
    """haven't told how to read from files """
    stream = open(file)
    data = stream.readlines()
    stream.close()
    return eval("".join(data))
