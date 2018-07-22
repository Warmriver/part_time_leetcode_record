import copy

class Solution:
    def merge(self, intervals):
        merged = []
        intervals.sort(key = lambda x:x.start)
        #practice : what if sort by end
        # intervals.sort(key = lambda x:x.end)
        #  for interval in intervals:
        #     if not merged or merged[-1][1] < interval.start:
        #         merged.append([interval.start, interval.end])
        #     else:
        #         merged[-1][1] = max(merged[-1][1], interval.end)
        for interval in intervals:
            if not merged or merged[-1][1] < interval.start:
                merged.append([interval.start, interval.end])
            else:
                merged[-1][1] = max(merged[-1][1], interval.end)
        return merged


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
            if self.is_intersected(ret[-1], [interval.start, interval.end]):
                self.overlap(ret, [interval.start, interval.end])
            else:
                ret.append([interval.start, interval.end])
        return ret
    def is_intersected(self, m, n):
        '''
        :rtype: bool
        '''
        return max(m[1], n[1]) - min(m[0], n[0]) <= m[1] - m[0] + n[1] - n[0]
    def overlap(self, ret, n):
        '''
        :rtype: [start, end]
        '''
        last = [min(ret[-1][0], n[0]), max(ret[-1][1], n[1])]
        ret[-1] = last
        list.reverse(ret)
        # for index,item in enumerate(ret):
        index = len(ret) - 1
        while index >= 0:
            if index == len(ret) - 1:
                index = index - 1
                continue
            if self.is_intersected(ret[index], last):
                temp = copy.copy(last)
                last = self.two_overlap(ret[index], last)
                ret.remove(temp)
                ret[-1] = last
                index = index + 1
            index = index - 1
        list.reverse(ret) 
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
    # materials = [i1,i2,i3,i4]
    ret = s.merge(materials)
    print(ret)       

    '''
[[2,3],[4,5],[6,7],[8,9],[1,10]]
[[1,3],[2,6],[8,10],[15,18]]
    '''