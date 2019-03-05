import copy

class Solution:
    # 排序的方法
    def merge(self, intervals):
        merged = []
        intervals.sort(key = lambda x:x.start)
        for interval in intervals:
            if not merged or merged[-1][1] < interval.start:
                merged.append([interval.start, interval.end])
            else:
                merged[-1][1] = max(merged[-1][1], interval.end)
        return merged

    # 不排序的方法
    def merge_d(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        ret = []
        if not intervals:
            return ret 
        for interval in intervals:
            if not ret:
                ret.append([interval.start, interval.end])
                continue
            self.add_or_overlap(ret, [interval.start, interval.end])
        return ret
    
    # 集合是否有重合
    def is_intersected(self, m, n):
        '''
        :rtype: bool
        '''
        return max(m[1], n[1]) - min(m[0], n[0]) <= m[1] - m[0] + n[1] - n[0]
    
    # 添加新的集合
    def add_or_overlap(self, ret, n):
        '''
        :rtype: [start, end]
        '''
        ret.append(n)
        index = len(ret) - 2
        # 对于每个新集合的添加都要遍历整个列表，因为没有排序，所以时间复杂度上升到n的n次方
        while index >= 0:
            if self.is_intersected(ret[index], n):
                new_n = self.two_overlap(ret[index], n)
                ret[-1] = new_n
                ret.remove(ret[index])
            index = index - 1

    # 返回并集合
    def two_overlap(self, m, n):
        return [min(m[0], n[0]), max(m[1], n[1])]

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


if __name__ == '__main__':
    s = Solution()
    i1 = Interval(2,3)
    i2 = Interval(4,5)
    i3 = Interval(6,7)
    i4 = Interval(8,9)
    i5 = Interval(1,10)
    # i1 = Interval(1,3)
    # i2 = Interval(2,6)
    # i3 = Interval(8,10)
    # i4 = Interval(15,18)

    materials = [i1,i2,i3,i4,i5]
    ret = s.merge(materials)
    print(ret)       

    j1 = Interval(2,3)
    j2 = Interval(-10,-5)
    #j3 = Interval(5,7)
    j4 = Interval(1,10)
    j5 = Interval(1,10)
    n = [j1,j2,j4,j5]
    print(s.merge_d(n))
    print(s.merge(n))

    '''
[[2,3],[4,5],[6,7],[8,9],[1,10]]
[[1,3],[2,6],[8,10],[15,18]]
    '''