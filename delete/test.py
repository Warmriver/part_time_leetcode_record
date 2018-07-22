class Solution:
    def fit(self, l, r):
        if l == '{' and r == '}':
            return True
        if l == '(' and r == ')':
            return True
        if l == '[' and r == ']':
            return True
        return False


    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = ('{', '(', '[')
        right = ('}', ')', ']')
        ret = []
        for c in s:
            if c in left:
                ret.append(c)
            else:
                left_pop = ret.pop()
                if not self.fit(left_pop, c):
                    return False
        if not ret:
            return True
        else:
            return False
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = []
        for v in nums:

            if nums[abs(v)-1] > 0:
                ret.append(abs(v))
                nums[abs(v) - 1] = -nums[abs(v) -1]
            else:
                ret.remove(abs(v))
        return ret

    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = []
        for i in range(len(nums)):
            if i + 1 not in nums:
                ret.append(i + 1)
        return ret


if __name__ == '__main__':
    s = Solution()
    # 1. v - 1 is within 1-n, -> self hashtable
    ret = s.findDuplicates([4,3,2,7,8,2,3,1])
    print(ret)