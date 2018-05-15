from functools import reduce
class Solution:
    max_sum = 0
    def max_sub_array(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return nums
        self.max_num = nums[0]
        last_num = [nums[0]]
        self.find_max_sub(1, nums, last_num, nums[0])
        return self.max_num

    def find_max_sub(self, index, nums, last_num, last_sum):
        this_sum = self.max_num - 1
        if nums[index] >= last_sum + nums[index]:
            last_num = [nums[index]]
            this_sum = nums[index]            
        else:
            last_num = last_num + [nums[index]]
            this_sum = self.sum_list(last_num)
        if this_sum > self.max_num:
            self.max_num = this_sum
        if index == len(nums) - 1:
            return
        return self.find_max_sub(index+1, nums, last_num, this_sum)
            
    def sum_list(self, list):
        return reduce(lambda x,y:x+y, list)
 



if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    solution = Solution()
    ret = solution.max_sub_array(nums)
    print(ret)
    # kadane's algo but timeout try this one
    '''
    ret, sum = nums[0], 0
    for i in len(nums):
        sum += nums[i]
        ret = max(sum, ret)
        sum = max(sum,0)
    return ret
    '''