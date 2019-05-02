import sys
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    ret = -sys.maxsize
    def maxPathSum(self, root: TreeNode) -> int:
        self.onePath(root)
        return self.ret
    def onePath(self, node):
        if not node:
            return 0
        l = self.onePath(node.left)
        r = self.onePath(node.right)
        self.ret = max(self.ret, l+node.val, r+node.val, l+r+node.val)
        if l>r:
            if l+node.val > 0:
                return l+node.val
            else:
                return 0
        else:
            if r+node.val > 0:
                return r+node.val
            else:
                return 0

if __name__ == "__main__":
    s = Solution()
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n1.left = n2
    n1.right = n3
    ret = s.maxPathSum(n1)
    print(ret)
