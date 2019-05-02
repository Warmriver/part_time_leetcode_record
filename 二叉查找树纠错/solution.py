"""
等级： hard
二叉查找树中有两个元素交换了位置，导致二叉查找树不再合规，找到这两个元素并且交换回来

解法：

中序遍历为 左根右，所以中序遍历一定是个升序序列，找到生序序列中的两个异常点，交换回来即可

例如
7 3 4 5 1
正确应该是 1 3 4 5 7， 3 4 5为升序，7和1交换了位置导致bst不再合规
"""
import sys
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.firstNode = None
        self.secondNode = None
        self.curNode = None

    def fix(self, root):
        cur = root
        self.curNode = TreeNode(-sys.maxsize)
        self.mid_traversal(cur)
        temp = self.firstNode.val
        self.firstNode.val = self.secondNode.val
        self.secondNode.val = temp
        return root
    def mid_traversal(self, root):
        if not root:
            return
        self.mid_traversal(root.left)

        # 找到升序数列的错误点
        if not self.firstNode and self.curNode.val > root.val:
            self.firstNode = self.curNode
        if self.firstNode and self.curNode.val > root.val:
            self.secondNode = root
        self.curNode = root

        self.mid_traversal(root.right)
    
if __name__ == "__main__":
    s = Solution()
    root = TreeNode(3)
    n1 = TreeNode(1)
    n4 = TreeNode(4)
    n2 = TreeNode(2)
    root.left = n1
    root.right = n4
    n4.left = n2
    s.fix(root)
    print(root.val)
    print(n2.val)