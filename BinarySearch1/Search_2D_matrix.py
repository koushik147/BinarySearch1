class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        n=len(matrix[0])
        
        l = 0 
        h = (m*n)-1
        
        while l<=h:
            mid=l+(h-l)//2
            arr = matrix[mid//n][mid%n]
            if arr == target:
                return True
            elif target<arr:
                h=mid-1
            else:
                l=mid+1
        return False