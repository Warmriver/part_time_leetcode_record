"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
"""

class Solution:
    def canJump(self, nums):
        # 只有最后一个点时，目标已经达成，此点记为ok点
        lastPos = len(nums) - 1
        for i in reversed(range(len(nums)-1)):
            # 查看ok点的邻居，如果邻居点和ok点的距离小于邻居点的大小，邻居点也是ok点
            if nums[i] >= lastPos - i:
                #如果邻居点是ok点，那么ok点更新为此邻居，能跳到新ok点的，那么一定可以跳到最开始的ok点
                lastPos = i
        #遍历完后ok点是否在第一位
        return lastPos == 0

if __name__=='__main__':
    solution = Solution()
    nums = [3,2,1,0,4]
    nums = [2,3,1,1,4]
    print(solution.canJump(nums))
