class Node:
    def __init__(self, v, l=None, r=None):
        self.v = v
        self.l = l
        self.r = r

ret = 0
def maxPathSum(root):
    global ret
    onePath(root, ret)
    print(ret)

def onePath(node, ret):
    if not node:
        return 0
    l = onePath(node.l, ret)
    r = onePath(node.r, ret)
    ret = max(ret, max(0, l)+max(0,r) +node.v)
    gg =  max(0, max(l,r)) + node.v
    print(gg)
    return gg

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n1.left = n2
n1.right = n3
n4 = Node(4)
n5 = Node(5)
n2.left = n4
n2.right = n5
n6 = Node(6)
n3.left = n6

maxPathSum(n1)
