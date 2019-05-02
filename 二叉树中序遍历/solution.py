from tools import Node
"""
class Node:
    val
    left
    right
"""

class solution:
    # 递归的方法
    @staticmethod
    def traverse_recursion(root):
        ret = []
        def _helper(node, ret):
            if node:
                if node.left:
                    _helper(node.left, ret)
                ret.append(node.val)
                if node.right:
                    _helper(node.right, ret)
        _helper(root, ret)
        return ret
    # 迭代的方法，思路和递归是一样的, 使用一个stack
    @staticmethod
    def traverse_iterative(root):
        ret = []
        stack = []
        cur = root
        # cur不为none时，意味着此次循环的cur不是叶子节点，反之则是叶子节点，从stack中取其未被处理的父节点即可
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            ret.append(cur.val)
            cur = cur.right
        return ret
    # Morris 遍历, 更改了树
    @staticmethod
    def traversal_morris(root):
        ret = []
        cur = root
        pre = None
        while cur:
            if not cur.left:
                ret.append(cur.val)
                cur = cur.right
            else:
                pre = cur.left
                while pre.right:
                    pre = pre.right
                pre.right = cur
                temp = cur
                cur = cur.left
                temp.left = None
        return ret

# 后序遍历
def traversal_backward(root):
    ret = []
    cur = root
    stack = [cur]
    while stack:
        cur = stack.pop()
        ret.insert(0, cur.val)
        if cur.left:
            stack.append(cur.left)
        if cur.right:
            stack.append(cur.right)
    return ret
        
def traversal_forward(root):
    ret = []
    def _helper(node, ret):
        if node:
            ret.append(node.val)
            _helper(node.left, ret)
            _helper(node.right, ret)
    cur = root
    _helper(cur, ret)       
    return ret


if __name__ == "__main__":
    root = Node.generate([1,2,3,4,5,6])
    # ret = solution.traverse_recursion(root)
    # ret = solution.traverse_iterative(root)
    # ret = solution.traversal_morris(root)
    # ret = traversal_backward(root)
    ret = traversal_forward(root)
    print(ret)



