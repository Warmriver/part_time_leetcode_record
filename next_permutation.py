import sys
class Solution:
    # def nextPermutation(self, nums: List[int]) -> None:
    def nextPermutation(self, nums):
        def swap(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
        def rev(i, j):
            while i < j:
                swap(i, j)
                i += 1
                j -= 1
        def find_less(n):
            i = len(nums) - 1
            while i > n:
                if nums[i] > nums[n]:
                    return i
                i -= 1
        if not nums or len(nums) == 1:
            return nums
        less_p = None
        max_p = None
        p = len(nums) - 1
        while True:
#            if not less_p:
#                less_p = p
           # else:
           #     less_p = p if nums[p] < nums[less_p] else less_p
            if not max_p:
                max_p = p
            else:
                max_p = p if nums[p] > nums[max_p] else max_p
            # situation 1 ok
            if p-1 != 0 and nums[p-1] < nums[p]:
                greater = find_less(p-1)
                swap(p-1, greater)
                rev(p, len(nums)-1)
                return nums
            elif p-1 == 0:
                # situation 2 ok
                if nums[p-1] >= nums[max_p]:
                    nums.reverse()
                    return nums
                # situation 3
                else:
                    less_p = find_less(0)
                    print(less_p)
                    swap(0, less_p)
                    rev(1, len(nums) - 1)
                    return nums
            else:
                p -= 1

if __name__ == '__main__':
   c = Solution()
   nums = [1,2,3]
   print(c.nextPermutation(nums))
   nums = [3,2,1]
   print(c.nextPermutation(nums))
   nums = [1,1,5]
   print(c.nextPermutation(nums))
   nums = [1,4,3,2]
   print(c.nextPermutation(nums))

   nums = [1,3,2]
   print(c.nextPermutation(nums))
   nums = [1,2]
   nums = [5,4,7,5,3,2]
   print(c.nextPermutation(nums))










