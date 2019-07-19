# 在一个数组中找到第一次出现目标数字，和最后一次出现目标数字的未知，找不到目标数字则结果为-1，把这两个数字组成一个数组返回
class Solution:
    def searchRange(self, nums, target):
        def binarySearch(x, y):
            if x > y:
                return -1
            mid = (x&y) + ((x^y)>>1)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return binarySearch(x, mid-1)
            elif nums[mid] < target:
                return binarySearch(mid+1, y)
        placeIndex = binarySearch(0, len(nums)-1)
        if placeIndex == -1:
            return [-1, -1]
        b, f = placeIndex, placeIndex
        while b-1 >= 0 and nums[b-1] == nums[placeIndex]:
            b -= 1
        while f+1 <= len(nums) - 1 and nums[f+1] == nums[placeIndex]:
            f += 1
        return [b, f]

if __name__ == "__main__":
    obj = Solution()
    ret = obj.searchRange([5,7,7,8,8,10], 8)
    # ret = obj.searchRange([1], 1)
    print(ret)
