class solution:
    def dfs(self, root, k):
        visited = set()
        return self.find_dfs(root, k, visited)
    def find_dfs(self, node, k, visited):
        if not node:
            return False
        if k - node.val in visited:
            return True
        visited.add(node.val)
        return self.find_dfs(node.left, k, visited) or self.find_dfs(node.right, k, visited)

    def bfs(self, root, k):
        visited = set()
        queue = []
        queue.append(root)
        while len(queue) != 0:
            cur = queue.pop()
            if cur:
                if cur.val in visited:
                    return True
                visited.add(cur.val)
                queue.append(cur.left)
                queue.append(cur.right)
        return False
    
    def bst(self, root, k):
        nodelist = []
        self.inorder(root, nodelist)
        l, r = 0, len(nodelist)
        while l < r:
            sum = nodelist[l] + nodelist[r]
            if  sum == k:
                return True
            elif sum < k:
                l += 1
            else:
                r -= 1
        return False
    def inorder(self, root, nodelist):
        if not root:
            return
        self.inorder(root.left, nodelist)
        nodelist.add(root.val)
        self.inorder(root.right, nodelist)



class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right