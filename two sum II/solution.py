class Solution:
    def twoSum(self, list, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # list = [v for v in numbers if v <= target]
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
