from functools import reduce

class Solution:
    dict = {}
    def maxSubset(self, end_index, last_max_num, nums):
        end_index += 1
        if(end_index > len(nums) - 1):
            return
        last_max_sum = reduce(lambda x,y:x+y, last_max_num)
        r_sum = last_max_sum + nums[end_index]
        s_sum = nums[end_index]
        if r_sum < s_sum:
            self.dict[end_index] = [nums[end_index]]
            self.maxSubset(end_index, [nums[end_index]], nums)
        else:
            self.dict[end_index] = last_max_num + [nums[end_index]]
            self.maxSubset(end_index, last_max_num + [nums[end_index]], nums)

if __name__ == '__main__':
    s = Solution()
    nums = [1,-2,-3,5,1,3]
    s.maxSubset(0,[nums[0]], nums)
    print(s.dict)
