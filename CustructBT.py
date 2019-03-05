from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None
        idc = {}
        indices=[0, len(inorder)-1, 0, len(preorder)-1]
        for index, item in enumerate(inorder):
            idc[item] = index
        return self.helper(indices, preorder, inorder, idc)
    def helper(self, indices, preorder, inorder, idc):
        cur_val = preorder[indices[2]]
        cur = TreeNode(cur_val)
        cur_inorder_index = idc[cur_val]
        # left:
        l_num = cur_inorder_index - indices[0]
        lin = [0 for i in range(4)]
        if l_num > 0:
            lin[0] = indices[0]
            lin[1] = cur_inorder_index - 1
            lin[2] =  indices[2] + 1
            lin[3] = lin[2] + l_num - 1
            cur.left =  self.helper(lin, preorder, inorder, idc)
        else:
            cur.left = None
        #right
        r_num = indices[1] - cur_inorder_index
        if r_num > 0:
            rin = [0 for i in range(4)]
            rin[0] = cur_inorder_index + 1
            rin[1] = indices[1]
            rin[2] = indices[2] + l_num + 1
            rin[3] = rin[2] + r_num - 1
            cur.right = self.helper(rin, preorder, inorder, idc)
        else:
            cur.right = None
        return cur
    def printTree(self, root):
        print(self.getTreeList(root))
    def getTreeList(self, root):
        ret = []
        dq = deque()
        dq.append(root)
        while dq:
            for _ in range(len(dq)):
                cur = dq.popleft()
                if cur:
                    ret.append(cur.val)
                    dq.append(cur.left)
                    dq.append(cur.right)
                else:
                    ret.append(None)
        dell = []
        n = len(ret) -1 

        for i, t in enumerate(reversed(ret)):
            if not t:
                dell.append(n-i)
            else:
                break
        for i in dell:
            ret.pop(i)
                
        return ret
        
if __name__ == '__main__':
    # preorder = [3,9,20,15,7]
    # inorder = [9,3,15,20,7]
    preorder = []
    inorder = []
    solution = Solution()
    root = solution.buildTree(preorder, inorder)
    print("root built")
    
    solution.printTree(root)