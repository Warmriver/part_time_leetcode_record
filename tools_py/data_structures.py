class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __str__(self):
        cur = self
        ret = []
        while cur:
            ret.append(cur.val)
            cur = cur.next
        return "->".join(str(x) for x in ret)
