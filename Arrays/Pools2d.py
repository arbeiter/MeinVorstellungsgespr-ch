'''
Count number of islands where every island is row-wise and column-wise separated
Given a rectangular matrix which has only two possible values ‘X’ and ‘O’. 
The values ‘X’ always appear in form of rectangular islands and these islands
 are always row-wise and column-wise separated by at least one line of ‘O’s. 
 Note that islands can only be diagonally adjacent. Count the number of islands in the given matrix.

def visit(matrix, i, j, visited):
    visited[i][j]=True
    return matrix[i][j]=='0'

def findNeighbors(mat, i, j):
  return []

def nextCell(mat, visited):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if visited[i][j]==False:
                return(i,j)
    return None

def findIslands(mat):
    numIslands = 1
    visited = [row[:] for row in mat]
    i,j = 0,0
    while(nextCell(mat, visited)!=None):
        queueSoFar = []
        islands = []
        cell = nextCell(mat,visited)

        queueSoFar.append(mat[i][j])
      #figure out a way to stop the 
        while(len(queueSoFar)!=None):
            valid = visit(queueSoFar[0], i, j, visited)
            if queueSoFar[0]=='0':
                currIsland+=1
              del(queueSoFar[0])
            neighbors = getNeighbors(mat, i, j)
            for neighbor in neighbors:
                queueSoFar.append(neighbor)
        islands.append(currIsland)
    return len(islands)
'''

def main():
    mat =  [		 	  	
    		  ['O', 'O', 'O'],
             ['X', 'X', 'O'],
              ['X', 'X', 'O'],
              ['O', 'O', 'X'],
              ['O', 'O', 'X'],
              ['X', 'X', 'O']
             ]
    assert findIslands(mat)==3
    mat =  [['X', 'O', 'O', 'O', 'O', 'O'],
              ['X', 'O', 'X', 'X', 'X', 'X'],
              ['O', 'O', 'O', 'O', 'O', 'O'],
              ['X', 'X', 'X', 'O', 'X', 'X'],
              ['X', 'X', 'X', 'O', 'X', 'X'],
              ['O', 'O', 'O', 'O', 'X', 'X'],
             ]
    assert findIslands(mat)==4

if __name__ == '__main__':
    main()
