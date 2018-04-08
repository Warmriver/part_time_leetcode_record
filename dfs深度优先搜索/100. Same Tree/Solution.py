# Given two binary trees, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

# difficulty: easy


class Solution:
    # 50%
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return p is q

    # higher 97%
    def isSameTree_dfs(self, p, q):
        stack = [(p, q)]
        while stack:
            x, y = stack.pop()
            if x and y:
                if x.val == y.val:
                    stack.append((x.left, y.left))
                    stack.append((x.right, y.right))
                else:
                    return False
            elif x is y:
                continue
            else:
                return False
        return True


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


if __name__ == '__main__':
    solution = Solution()
    t1_root = TreeNode(0)
    t1_left = TreeNode(-5)
    # t1_right = TreeNode(1)
    t1_root.left = t1_left
    # t1_root.right = t1_right

    t2_root = TreeNode(0)
    t2_left = TreeNode(-8)
    # t2_right = TreeNode(2)
    t2_root.left = t2_left
    # t2_root.right = t2_right

    print(solution.isSameTree_dfs(t1_root, t2_root))
