
class Solution:
    def get_sum(self, a, b):
        if a == 0:
            return b
        elif b == 0:
            return a
        while b != 0:
            carry = a & b
            a = a ^ b
            b = carry << 1
        return a

if __name__ == '__main__':
    solution  = Solution()
    ret = solution.get_sum(1, 3)
    print(ret)