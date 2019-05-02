class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # 按照二叉堆进行生成
    @staticmethod
    def generate(nums):
        if not nums:
            return None
        node_store = {}
        def generate_child(index, left_tag):
            if index < len(nums):
                cur_child = None
                if index in node_store:
                    cur_child = node_store[index]
                else:
                    cur_child = Node(nums[index])
                    node_store[index] = cur_child
                if left_tag == 1:
                    cur.left = cur_child 
                else:
                    cur.right = cur_child
        for i in range(0, len(nums)):
            if i in node_store:
                cur = node_store[i]
            else:
                cur = Node(nums[i])
                node_store[i] = cur
            generate_child(2*i+1, 1)
            generate_child(2*i+2, 0)
        return node_store[0]

    # 帮忙打印下
    @staticmethod
    def print(root):
        res = []
        stack = []
        stack.append(root)
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            if cur.left:
                stack.insert(0, cur.left)
            if cur.right:
                stack.insert(0, cur.right)
        print(res)

        
        
