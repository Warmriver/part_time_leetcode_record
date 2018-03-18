def subsets2(nums):
    res = []
    nums.sort()
    for i in range(1<<len(nums)):
        tmp = []
        for j in range(len(nums)):
            temp1 = 1 << j
            temp2 = i & temp1
            if i & 1 << j:  # if i >> j & 1:
                tmp.append(nums[j])
        res.append(tmp)
    return res

if __name__ == '__main__':
    nums = [1,2,3]
    print(subsets2(nums))

"""
对于每一个subset，用其 下标（0，1，2，3，4，5，6，7）
分别与每个元素的下标&1（即 1， 2， 4）
进行
&运算

"""