import itertools

class Solution:
    def __init__(self):
        self.dict = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
    def letterCombinations(self, digits):
        if len(digits) < 1:
            return []
        # 例如23， 想要的数据结构， [ [a,b,c], [d,e,f]]
        cases = [[i for i in self.dict[digit]] for digit in digits]
        # 返回 ['ab','cd', ... ]
        return [''.join(i) for i in itertools.product(*cases)]

if __name__ == "__main__":
   s = Solution()
   result = s.letterCombinations("")
   print(result)
