class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix) # assigning row length of matrix to m
        n=len(matrix[0]) # assigning column length of matrix to n
        
        l = 0 # setting the pointer in first 
        h = (m*n)-1 # setting the pointer in last
        
        while l<=h:
            mid=l+(h-l)//2 # finding mid value
            arr = matrix[mid//n][mid%n] # finding the specified index 
            if arr == target: # if target is equal to value
                return True
            elif target<arr: # if target is less than value
                h=mid-1
            else: # if target is greater than value
                l=mid+1
        return False