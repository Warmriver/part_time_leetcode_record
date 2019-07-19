def permutation(nums):
    return [[n] + p
            for i, n in enumerate(nums)
            for p in permutation(nums[:i]+nums[i+1:])] or [[]]

def permutation_without_duplicates(nums):
    nums = sorted(nums)
    def _helper(nums):
        return [[n] + p
                for i, n in enumerate(nums) if (i == 0 or (i > 0 and nums[i] != nums[i-1]))
                for p in permutation_without_duplicates(nums[:i]+nums[i+1:])] or [[]]
    return _helper(nums)

if __name__ == "__main__":
    nums = [1,2,1]
    ret = permutation_without_duplicates(nums)
    print(ret)
    ret = permutation(nums)
    print(ret)
    print(nums)