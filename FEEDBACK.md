Could you have written this without *magic numbers* and by combining the tests or using helper functions to avoid repeated code?

```
def getBoxLocations(location):
    """Return a list of all nine "locations" (row, column)
        tuples in the same box as the given location """
    if location[0] in [0, 1, 2] and location[1] in [0, 1, 2]:
        s = [0]*3 + [1]*3 + [2]*3
        t = [0,1,2]*3
        return list(zip(s, t))
    if location[0] in [0, 1, 2] and location[1] in [3, 4, 5]:
        s = [0]*3 + [1]*3 + [2]*3
        t = [3, 4, 5]*3
        return list(zip(s, t)) 
    if location[0] in [0, 1, 2] and location[1] in [6, 7, 8]:
        s = [0]*3 + [1]*3 + [2]*3
        t = [6, 7, 8]*3
        return list(zip(s, t))
    if location[0] in [3, 4, 5] and location[1] in [0, 1, 2]:
        s = [3]*3 + [4]*3 + [5]*3
        t = [0, 1, 2]*3
        return list(zip(s, t))
    if location[0] in [3, 4, 5] and location[1] in [3, 4, 5]:
        s = [3]*3 + [4]*3 + [5]*3
        t = [3, 4, 5]*3
        return list(zip(s, t))
    if location[0] in [3, 4, 5] and location[1] in [6, 7, 8]:
        s = [3]*3 + [4]*3 + [5]*3
        t = [6, 7, 8]*3
        return list(zip(s, t))
    if location[0] in [6, 7, 8] and location[1] in [0, 1, 2]:
        s = [6]*3 + [7]*3 + [8]*3
        t = [0, 1, 2]*3
        return list(zip(s, t))
    if location[0] in [6, 7, 8] and location[1] in [3, 4, 5]:
        s = [6]*3 + [7]*3 + [8]*3
        t = [3, 4, 5]*3
        return list(zip(s, t))
    if location[0] in [6, 7, 8] and location[1] in [6, 7, 8]:
        s = [6]*3 + [7]*3 + [8]*3
        t = [6, 7, 8]*3
        return list(zip(s, t))
```
