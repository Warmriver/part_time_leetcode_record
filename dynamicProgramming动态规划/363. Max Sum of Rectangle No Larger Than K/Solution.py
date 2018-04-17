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
    # def __max_subset(self, slice, k):
    #     max_sum = slice[0]
    #     max_up = 0
    #     max_dn = 0
    #     max_sum, max_up, max_dn = self.__get_max_subset_of_index(slice, 0, [slice[0]], max_sum, max_up, max_dn, k)
    #     return max_sum, max_up, max_dn
    # def __get_max_subset_of_index(self, slice, end_index, last_max_slice, max_sum, max_up, max_dn, k):
    #     end_index += 1
    #     if end_index > len(slice) - 1 or max_sum == k:
    #         # 只取最大subset，会漏掉次大的subset，可能会是答案
    #         return max_sum, max_up, max_dn
    #     last_sum = reduce(lambda x,y:x+y, last_max_slice)
    #     possible_max = last_sum + slice[end_index]
    #     current_sum = slice[end_index]
    #     if current_sum >= possible_max and current_sum <= k:   
    #         if current_sum > max_sum:    
    #             max_sum = current_sum
    #             max_up = end_index
    #             max_dn = end_index
    #         return self.__get_max_subset_of_index(slice, end_index, [slice[end_index]], max_sum, max_up, max_dn,k)
    #     elif current_sum < possible_max and possible_max <= k:
    #         if possible_max > max_sum:
    #             max_sum = possible_max
    #             max_dn = end_index
    #         return self.__get_max_subset_of_index(slice, end_index, last_max_slice + [slice[end_index]], max_sum, max_up, max_dn,k)
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
    matrix = [[27,5,-20,-9,1,26,1,12,7,-4,8,7,-1,5,8],[16,28,8,3,16,28,-10,-7,-5,-13,7,9,20,-9,26],[24,-14,20,23,25,-16,-15,8,8,-6,-14,-6,12,-19,-13],[28,13,-17,20,-3,-18,12,5,1,25,25,-14,22,17,12],[7,29,-12,5,-5,26,-5,10,-5,24,-9,-19,20,0,18],[-7,-11,-8,12,19,18,-15,17,7,-1,-11,-10,-1,25,17],[-3,-20,-20,-7,14,-12,22,1,-9,11,14,-16,-5,-12,14],[-20,-4,-17,3,3,-18,22,-13,-1,16,-11,29,17,-2,22],[23,-15,24,26,28,-13,10,18,-6,29,27,-19,-19,-8,0],[5,9,23,11,-4,-20,18,29,-6,-4,-11,21,-6,24,12],[13,16,0,-20,22,21,26,-3,15,14,26,17,19,20,-5],[15,1,22,-6,1,-9,0,21,12,27,5,8,8,18,-1],[15,29,13,6,-11,7,-6,27,22,18,22,-3,-9,20,14],[26,-6,12,-10,0,26,10,1,11,-10,-16,-18,29,8,-8],[-19,14,15,18,-10,24,-9,-7,-19,-14,23,23,17,-5,6]]
    k = -100
    s = Solution()
    ret = s.maxSumSubmatrix(matrix, k)
    print(ret)

"""
    1    0  1
    0    -2  3
    



    2
    9
    1
"""