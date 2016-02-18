class Solution:
    # @param A : tuple of list of integers
    # @return a list of integers
    def spiralOrder(self, A):
        result = []
        ## Actual code to populate result
        for i in range(len(A)):
            for j in range(len(A[0])):
                result.append(A[i][j])
        return result

print(Solution().spiralOrder([[1,2],[3,4]]))