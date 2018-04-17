import numpy as np
from functools import reduce
import sys
class Solution:
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        # 最大的和，拥有最大的和的长方形的四个顶点, 注意max_sum不能用0，否则会大于负数的结果
        max_sum, max_up, max_dn, max_left, max_right = -sys.maxsize, 0, 0, 0, 0
        for left in range(len(matrix[0])):
            # slice_left要定义好
            slice_left = np.array([ele[0] for ele in np.array(matrix)[:,left:left+1]])
            for right in range(left, len(matrix[0])):
                slice_right = np.array([ele[0] for ele in np.array(matrix)[:,right:right+1]])
                if left != right:
                    slice_left = slice_right + slice_left
                slice = list(slice_left)
                current_sum, current_max_up, current_max_dn = self.max_subset(slice, k)
                if current_sum > max_sum and current_sum <= k:
                    max_up = current_max_up
                    max_dn = current_max_dn
                    max_left = left
                    max_right = right
                    max_sum = current_sum
        print(max_up, max_dn, max_left, max_right)
        return int(max_sum)
    def max_subset(self, num, k):
        dict = {}
        sumi = num[0]
        sumj = 0
        max_sum = num[0]
        dn = 0
        up = 0
        if max_sum > k:
            max_sum = -sys.maxsize
        for i in range(1, len(num)):
            sumi = sum(num[:i+1])
            for j in range(0,i):
                if j in dict.keys():
                    sumj = dict[j]
                else:
                    sumj = sum(num[:j+1])
                    dict[j] = sumj
                if sumi - sumj <= k and sumi - sumj > max_sum:
                    max_sum = sumi - sumj
                    up = j+1
                    dn = i
        return max_sum, up, dn      

        
            
if __name__ == '__main__':
    matrix = [[

    ]]
    k = -100
    s = Solution()
    ret = s.maxSumSubmatrix(matrix, k)
    print(ret)