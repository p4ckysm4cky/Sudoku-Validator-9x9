def validSolution(board):
    correctArray = [1, 2, 3, 4, 5, 6, 7, 8, 9,]
    rowCount = 0
    columnCount = 0
    gridCount = 0
    
    #<- Checking rows ->    
    
    for row in board:
        check = [] #used to compare with "correctArray"
        for j in row: # values in rows
            check.append(j) #adds value to check
        check.sort()
        if check == correctArray:
            rowCount += 1
        else:
            return False
    print(f"rowCount: {rowCount}")

    #<- Checking columns ->

    counter = 0
    while counter < 9:
        check = [column[counter] for column in board] #values in column
        check.sort()
        if check == correctArray:
            columnCount += 1
        else:
            return False
        counter += 1
    print(f"columnCount: {columnCount}")
    print(f"counter: {counter}")

    #<- Checking 3x3 grids ->

    check = []
    for row in board:
        check += row[:3]
        if len(check) == 9: #ensures only 9 values
            check.sort()
            if check == correctArray:
                gridCount += 1
                check = []
            else:
                return False

    

    for row in board:
        check += row[3:6]
        if len(check) == 9:
            check.sort()
            if check == correctArray:
                gridCount += 1
                check = []
            else:
                return False
    for row in board:
        check += row[6:9]
        if len(check) == 9:
            check.sort()
            if check == correctArray:
                gridCount += 1
                check = []
            else:
                return False
   
    #<- Final Verification ->
    
    print(f"gridCount: {gridCount}")
    if rowCount == 9 and columnCount == 9 and gridCount == 9:
        return True
    else:
        return False
        




