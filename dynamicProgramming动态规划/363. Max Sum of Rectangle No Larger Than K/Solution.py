import numpy as np
from functools import reduce
class Solution:
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        max_sum, max_up, max_dn, max_left, max_right = 0, 0, 0, 0, 0
        for left in range(len(matrix)):
            for right in range(left, len(matrix)):
                slice = [list(ele) for ele in np.array(matrix)[:,left:right+1]]
                current_sum, current_max_up, current_max_dn = self.__max_subset(slice)
                if current_sum > max_sum and current_sum <= k:
                    max_up = current_max_up
                    max_dn = current_max_dn
                    max_left = left
                    max_right = right
        print(max_up, max_dn, max_left, max_right)
        return max_sum
    def __max_subset(self, slice):
        max_sum = slice[0]
        max_up = 0
        max_dn = 0
        self.__get_max_subset_of_index(slice, 0, [slice[0]], max_sum, max_up, max_dn )
        return max_sum, max_up, max_dn
    def __get_max_subset_of_index(self, slice, end_index, last_max_slice, max_sum, max_up, max_dn):
        end_index += 1
        if end_index > len(slice) - 1:
            return
        last_sum = reduce(lambda x,y:x+y, last_max_slice)
        possible_max = last_sum + slice[end_index]
        current_sum = slice[end_index]
        if current_sum > possible_max:
            if current_sum > max_sum:    
                max_sum = current_sum
                max_up = end_index
                max_dn = end_index
            self.__get_max_subset_of_index(slice, end_index, [slice[end_index]], max_sum, max_up, max_dn)
        else:
            if possible_max > current_sum:
                max_sum = possible_max
                max_dn = end_index
            self.__get_max_subset_of_index(slice, end_index, last_max_slice + [slice[end_index]], max_sum, max_up, max_dn)
        
            
if __name__ == '__main__':
    matrix = [[1,0,1],[0,-2,3]]
    k = 2
    s = Solution()
    print(s.maxSumSubmatrix(matrix, k))