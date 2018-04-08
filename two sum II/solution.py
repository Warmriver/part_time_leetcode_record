"""
问题：给定一个数组，和一个目标数字，如果数组中有两个数字之和等于这个目标数字，则输出这两个数字在数组中的位置

例如 list = [2, 7, 13, 4], target = 9
在list中，2+7 = 9， 那么应该输出 [1, 2]，对应第0为和第一位数字

"""
class Solution:
    def twoSum(self, list, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i, item in enumerate(list):
            if item in dict.keys():
                return [dict[item]+1,i+1]
            else:
                dict[target - item] = i

if __name__ == '__main__':
    input = [-1,0]
    target = -1
    s = Solution()
    output = s.twoSum(input,target)
    print(output)
