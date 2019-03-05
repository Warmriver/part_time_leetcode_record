from functools import reduce
class Solution:
    # using recursive dp（使用递归）
    def max_sub_array_dp(self, nums):
        return self._helper(len(nums)-1, nums)[0]

    def _helper(self, index, nums):
        # escap condition
        if index==0:
            return nums[index], 0
        last_sum, last_index = self._helper(index-1, nums)
        distance = self.sum_list(nums[last_index+1: index])
        if nums[index] + last_sum + distance >= nums[index] and nums[index] + last_sum + distance >= last_sum:
            return nums[index] + last_sum + distance, index
        elif nums[index] >= last_sum:
            return nums[index], index
        elif nums[index] < last_sum:
            return last_sum, last_index
    

    # using iteration 使用迭代
    def max_sub_array(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return nums
        self.max_num = nums[0]
        self.max_num_list = []
        last_num = [nums[0]]
        self.find_max_sub(1, nums, last_num, nums[0])
        return self.max_num, self.max_num_list

    def find_max_sub(self, index, nums, last_num, last_sum):
        while index < len(nums) - 1:
            this_sum = self.max_num - 1 # just make it smaller than max
            if nums[index] >= last_sum + nums[index]:
                last_num = [nums[index]]
                this_sum = nums[index]            
            else:
                last_num = last_num + [nums[index]]
                this_sum = self.sum_list(last_num)
            if this_sum > self.max_num:
                self.max_num = this_sum
                self.max_num_list = last_num
            index += 1
            last_sum = this_sum
        return
    
    def sum_list(self, list):
        return reduce(lambda x,y:x+y, list) if list else 0

    # bad case
    def find_max_sub_b(self, index, nums, last_num, last_sum):
        this_sum = self.max_num - 1
        if nums[index] >= last_sum + nums[index]:
            last_num = [nums[index]]
            this_sum = nums[index]            
        else:
            last_num = last_num + [nums[index]]
            this_sum = self.sum_list(last_num)
        if this_sum > self.max_num:
            self.max_num = this_sum
            self.max_num_list = last_num
        if index == len(nums) - 1:
            return
        return self.find_max_sub(index+1, nums, last_num, this_sum)





if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    solution = Solution()
    ret, ret1 = solution.max_sub_array(nums)
    print(ret, ret1)
    #ret = solution.max_sub_array_dp(nums)
    #print(ret)
    # kadane's algo but timeout try this one
    '''
    ret, sum = nums[0], 0
    for i in len(nums):
        sum += nums[i]
        ret = max(sum, ret)
        sum = max(sum,0)
    return ret
    '''