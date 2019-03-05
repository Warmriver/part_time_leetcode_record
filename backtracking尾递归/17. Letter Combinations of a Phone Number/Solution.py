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
    
    # 使用队列来解决问题
    # 空间上，使用一个队列，占据大概3的n次方，时间上则是3n
    def letterCombinationsUsingQueue(self, digits):
        if len(digits) < 1:
            return []
        # initialize
        queue = [i for i in self.dict[digits[0]]]
        for i, v in enumerate(digits[1:]):
            # when the head element's length does not meet, we need to extend it by all the possible alphabets, 
            # then push the result list back to queue in the end
            while len(queue[0]) < i + 2:
                material = queue.pop(0)
                new_add = [material + m for m in self.dict[v]]
                queue.extend(new_add)
        return queue
        

if __name__ == "__main__":
   s = Solution()
#    result = s.letterCombinations("245")
   result = s.letterCombinationsUsingQueue("245")
   print(result, len(result))
