def GenerateRow(n):
    prevRow, currRow = [1,1],[]
    if n == 1:
        return [1]
    if n == 2:
        return [1,1]

    for i in range(3,n+1):
        currRow=[]
        currRow = [1]*i
        for j in range(1,i-1):
            currRow[j]=(prevRow[j-1]+prevRow[j])
        prevRow = currRow[:]
    return currRow

print(GenerateRow(5))