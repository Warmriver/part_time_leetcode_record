# find the common largest ancestors of two nodes in a tree. -- a q in microsoft interview
"""
        1
      /   \
    3      2
  /  \      
4     6
     /   
    5

4 and 5 最近的祖先是3，需要输出3。 需要在遍历是记录路径，然后匹配即可
"""


class Solution:
    def lca(self, root, target_1, target_2):
        path_1 = self.path_2_x(root, target_1)
        path_2 = self.path_2_x(root, target_2)
        lca_response = -1
        while len(path_1) > 0 and len(path_2) > 0:
            a = path_1.pop() 
            b = path_2.pop()
            if a == b:
                lca_response = a
            else:
                break
        return lca_response
    def path_2_x(self, root, target):
        if root is None:
            return None
        if root.val == target:
            return [target]
        left_path = self.path_2_x(root.left, target)
        if left_path is not None:
            left_path.append(root.val)
            return left_path
        right_path = self.path_2_x(root.right, target)
        if right_path is not None:
            right_path.append(root.val)
            return right_path
        return None


class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


if __name__ == '__main__':
    
    root = Node(1, Node(3, Node(4), Node(6,Node(5))), Node(2))
    s = Solution()
    lca_value = s.lca(root, 4, 5)
    print(lca_value)
