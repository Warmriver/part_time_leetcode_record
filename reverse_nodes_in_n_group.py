"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
"""
from tools_py.data_structures import ListNode
# ListNode structures like this
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    @staticmethod
    def reverse(root, k):
        if k <= 1 or not root:
            return root
        # first group
        nextNode, nn, head, finish = Solution.helper(None, root, k-1)
        ret = nextNode
        while nextNode and nn and not finish:
            nextNode, nn, head, finish = Solution.helper(head, nn, k-1)
        return ret   
    @staticmethod
    def helper(prev, root, step, finish=False):
        n2 = root.next
        n1 = root
        count = 0
        if not n2:
            return n1, n2, root, True
        while count < step and n2:
            tmp = n2.next
            n2.next = n1
            n1, n2 = n2, tmp
            count += 1
        if prev:
            prev.next = n1
        root.next = n2
        if count < step:
            return helper(prev, n1, count, True)
        return n1, n2, root, finish

if __name__ == "__main__":
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)
    n1.next=n2
    n2.next=n3
    n3.next=n4
    n4.next=n5
    print("after reverse")
    ret = Solution.reverse(n1, 2)
    print(ret)
    assert str(ret) == "2->1->4->3->5"
