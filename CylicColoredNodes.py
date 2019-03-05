class Node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next
    def __str__(self):
        return str(self.val)

class Solution:
    def minSeq(self, m, n, root):
        if not root:
            return -1
  
        colors = []
        colors.append(root.val)
        head = root
        cur = root
        count = 1
        for _ in range(m):
            if len(colors) == n:
                return count
            if _ == 0:
                cur = cur.next
                continue
            
            if cur.val == head.val:
                head = head.next
                count -= 1
            else:
                if cur.val not in colors:
                    colors.append(cur.val)
            cur = cur.next
            count += 1
            if len(colors) == n:
                return count
        return -1

if __name__ == '__main__':
    n1 = Node("R")
    n2 = Node("G")
    n3 = Node("R")
    n4 = Node("B")
    n5 = Node("B")
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n1

    s = Solution()
    count = s.minSeq(5, 3, n1)
    print(count)

            
