class Solution(object):
    def longestIncreasingPath(self, matrix):
        i, j = 0, 0
        self.findSum(0,0,matrix,len(matrix)-1, len(matrix[0])-1, 0)
    
    def check_bounds(self, i, j):
        return True
    
    def findSum(self, i, j, matrix, max_i, max_j, curr_sum):
        if i==max_i and j==max_j:
            return curr_sum+matrix[i][j]
        
        return max(findSum(i+1, j, matrix, max_i, max_j, curr_sum+matrix[i][j]),
                   findSum(i, j+1, matrix, max_i, max_j, curr_sum+matrix[i][j]),
                   findSum(i-1, j, matrix, max_i, max_j, curr_sum+matrix[i][j]),
                   findSum(i, j-1, matrix, max_i, max_j, curr_sum+matrix[i][j])
                   )
