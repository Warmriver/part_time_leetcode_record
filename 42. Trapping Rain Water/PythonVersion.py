"""
问题：
给定一个包含正整数的数组，对于每个数字，下标为一个圆柱体在二维坐标图中x轴的左端，圆柱的宽度为1，
按照以上规则，一个数组组成的图形如果用来盛水，那么水的体积最多是多少

方法：
从左到右找大于当前柱子高度，且距离大于0的最高柱子，即为一个有效容器。 然后从右向左再同样遍历一样；已经寻找到的有效容器则不再进行记载。
"""

def trap_water(nums):
    sum = 0 # sum is the final number returned
    i = 0 # i is the index from left
    numlen = len(nums)
    for j in range(i+1, numlen):
        if nums[j] < nums[i]:
            continue # a trap is not finished, just increase 
        if nums[j] >= nums[i]:
            sum += nums[i] * (j-i) # a convex that can trap water, add the volume to sum
            i = j

    # do this again in reverse order
    m = numlen - 1
    for n in reversed(range(0, m)):
        if nums[n] < nums[m]:
            continue # a trap is not finished, just increase 
        if nums[n] >= nums[m]:
            sum += nums[m] * (m-n) # a convex that can trap water, add the volume to sum
            m = n
    return sum

if __name__ == '__main__':
    ret = trap_water([2, 1, 1, 3, 4, 2, 3])
    print(ret)

        #                 1
        #             1   1       1
        # 1           1   1   1   1
        # 1   1   1   1   1   1   1