import math
import operator
"""
离原点最近的k个点
"""
class Solution:
    def output_k_closest_points(self, tuples, k):
        #最多存k个点的列表
        max_heap = []
        #所有的点
        with_d = []
        #遍历目标点的集合，k应该小于等于这个集合的大小
        if k > len(tuples):
            print(tuples)
            return
        #对于所有的点，计算每个点离原点的距离，存入with_d
        for t in tuples:
            d = math.sqrt(abs(t[0]) ** 2 + abs(t[1]) ** 2)
            p = Point(d, t)
            with_d.append(p)
        # 将前k个with_d集合中的点存入max_heap
        for i in range(k):
            max_heap.append(with_d[i])
        # max_heap按照点的距离进行从小到大排序
        max_heap.sort(key = lambda p:p.d)
        # 遍历with_d集合中剩余的点，如果有点b，距离小于max_heap中最后一个点a的距离（排序后最后一个点的距离最大）
        # ，则把a排出，纳入b
        for left_point in with_d[k:]:
            if left_point.d < max_heap[-1].d:
                max_heap.pop()
                max_heap.append(left_point)
        for res_p in max_heap:
            print(res_p)
class Point:
    def __init__(self, d, tuple):
        self.d = d
        self.tuple = tuple
    def __str__(self):
        return str(self.tuple) + ": distince is " + str(self.d)

if __name__ == '__main__':
    s = Solution()
    tuples = [(1,0),(-2,0),(1,-1)]
    s.output_k_closest_points(tuples,4)
        