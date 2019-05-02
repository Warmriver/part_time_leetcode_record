"""
从下到上遍历,存储二叉树每层的所有非none值，例如
输入：
   1
2     3
     4  5
输出：
[
    [4, 5],
    [2, 3],
    [1]
]
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root):
        if not root:
            return []
        queue = [[root.left, root.right]]
        ret = [[root.val]]
        while queue:
            cur = queue.pop()
            single_ret = []
            next_cur = []
            for node in cur:
                if node:
                    single_ret.append(node.val)
                    if node.left:
                        next_cur.append(node.left)
                    if node.right:
                        next_cur.append(node.right) 
            if single_ret:
                ret.insert(0, single_ret) 
            if next_cur:
                queue.insert(0, next_cur)
        return ret


if __name__ == "__main__":
    n = TreeNode(1)
    s = Solution()
    ret = s.levelOrderBottom(n)
    print(ret)