from sudoku import *
import copy

class TestSudoku2018(pytest.TestCase):

    def testConvertToSets(self):
        ary = [[0, 1, 2], [1, 0, 2], [0, 1, 0]]
        s = set(range(1, 10))
        assert convertToSets(ary) == [[s, {1}, {2}], [{1}, s, {2}], [s, {1}, s]]
        assert type(ary[0][0]) is int

    def testConvertToInts(self):
        sets = [[{1, 2}, {3}, {4}], [{1}, {3, 5, 7}, {2}], [{2, 3}, {2}, {3}]]
        assert convertToInts(sets) == [[0, 3, 4], [1, 0, 2], [0, 2, 3]]
        assert type(sets[0][0]) is set

    def testGetRowLocations(self):
        lst = [(5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8)]
        assert set(getRowLocations(5)) == set(lst)

    def testGetColumnLocations(self):
        lst = [(0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5), (8, 5)]
        assert set(getColumnLocations(5)) == set(lst)

    def testGetBoxLocations(self):
        lst = [(3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2), (5, 0), (5, 1), (5, 2)]
        assert set(getBoxLocations((3, 2)) == set(lst)

    def testEliminate(self):
        sets = [[{1, 2}, {3}, {4}], [{1}, {3, 5, 7}, {2}], [{2, 3}, {2}, {1, 2, 3}]]
        location = (1, 2) # contains {2}
        count = eliminate(sets, location, [(0, 0), (1, 0), (2, 2)])
        assert count == 2               
        assert sets == [[{1}, {3}, {4}], [{1}, {3, 5, 7}, {2}], [{2, 3}, {2}, {1, 3}]]              
                          
    def testIsSolved(self):
        # Just check whether every cell has been reduced to one number
        array = [[{1}] * 9] * 9
                assert all([len(array[r][c]) == 1 for r in range(0, 9) for c in range(0, 9)])
	
	def testNotIsSolved(self):
        array[3][5] = {1, 2}
        assert not all([len(array[r][c]) == 1 for r in range(0, 9) for c in range(0, 9)])
        
    
    def testSolve(self):
        # Easy
        sudoku1 = [[4, 0, 0,  0, 0, 3,  0, 7, 0],
                   [0, 0, 1,  0, 0, 9,  5, 0, 8],
                   [0, 0, 0,  6, 0, 8,  4, 1, 3],

                   [0, 1, 0,  9, 0, 0,  3, 0, 0],
                   [0, 0, 0,  0, 5, 0,  0, 0, 0],
                   [0, 0, 4,  0, 0, 6,  0, 8, 0],

                   [7, 9, 2,  8, 0, 5,  0, 0, 0],
                   [3, 0, 5,  4, 0, 0,  9, 0, 0],
                   [0, 4, 0,  2, 0, 0,  8, 0, 5]]
                   
        solved1 = [[4, 6, 8,  5, 1, 3,  2, 7, 9], 
                   [2, 3, 1,  7, 4, 9,  5, 6, 8], 
                   [5, 7, 9,  6, 2, 8,  4, 1, 3], 

                   [6, 1, 7,  9, 8, 2,  3, 5, 4], 
                   [8, 2, 3,  1, 5, 4,  7, 9, 6], 
                   [9, 5, 4,  3, 7, 6,  1, 8, 2], 

                   [7, 9, 2,  8, 3, 5,  6, 4, 1], 
                   [3, 8, 5,  4, 6, 1,  9, 2, 7], 
                   [1, 4, 6,  2, 9, 7,  8, 3, 5]]
        # Easy
        sudoku2 = [[0, 0, 0,  7, 0, 0,  6, 8, 9],
                   [3, 0, 8,  0, 0, 0,  2, 0, 0],
                   [0, 0, 0,  8, 1, 0,  0, 4, 0],

                   [6, 0, 0,  0, 0, 0,  8, 0, 4],
                   [8, 0, 0,  3, 4, 9,  0, 0, 5],
                   [7, 0, 5,  0, 0, 0,  0, 0, 3],

                   [0, 8, 0,  0, 7, 6,  0, 0, 0],
                   [0, 0, 7,  0, 0, 0,  1, 0, 8],
                   [9, 5, 1,  0, 0, 8,  0, 0, 0]]
                   
        solved2 = [[1, 2, 4,  7, 5, 3,  6, 8, 9],
                   [3, 7, 8,  9, 6, 4,  2, 5, 1],
                   [5, 9, 6,  8, 1, 2,  3, 4, 7],

                   [6, 3, 9,  5, 2, 7,  8, 1, 4],
                   [8, 1, 2,  3, 4, 9,  7, 6, 5],
                   [7, 4, 5,  6, 8, 1,  9, 2, 3],

                   [4, 8, 3,  1, 7, 6,  5, 9, 2],
                   [2, 6, 7,  4, 9, 5,  1, 3, 8],
                   [9, 5, 1,  2, 3, 8,  4, 7, 6]]

        # Hard
        sudoku3 = [[9, 0, 0,  0, 0, 8,  0, 0, 0],
                   [0, 0, 0,  0, 3, 2,  0, 0, 0],
                   [6, 8, 0,  9, 0, 1,  0, 7, 0],

                   [8, 0, 9,  5, 2, 0,  0, 3, 0],
                   [2, 0, 0,  0, 0, 0,  0, 0, 5],
                   [0, 4, 0,  0, 9, 3,  7, 0, 8],

                   [0, 2, 0,  3, 0, 9,  0, 6, 4],
                   [0, 0, 0,  2, 8, 0,  0, 0, 0],
                   [0, 0, 0,  6, 0, 0,  0, 0, 3]]
                   
        solved3 = [[9, 0, 0,  0, 0, 8,  0, 0, 0],
                   [0, 0, 0,  0, 3, 2,  0, 0, 0],
                   [6, 8, 0,  9, 0, 1,  0, 7, 2],

                   [8, 0, 9,  5, 2, 0,  0, 3, 0],
                   [2, 0, 0,  0, 0, 0,  0, 0, 5],
                   [5, 4, 6,  1, 9, 3,  7, 2, 8],

                   [0, 2, 0,  3, 0, 9,  0, 6, 4],
                   [0, 0, 0,  2, 8, 0,  0, 0, 0],
                   [0, 0, 0,  6, 0, 0,  0, 0, 3]]
                   
		assert tryToSolve(sudoku1) == solved1
		assert tryToSolve(sudoku2) == solved2
		assert tryToSolve(sudoku3) == solved3

    def tryToSolve(self, problem, solution):
##        print_sudoku(problem)
        problemAsSets = convertToSets(problem)
        solve(problemAsSets)
        solved = convertToInts(problemAsSets)
##        print_sudoku(solution)
        assert solved == solution

pytest.main()
