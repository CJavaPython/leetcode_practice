from typing import Optional
import math

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        
        nodeList = []

        def inorder(cur):
            global nodeList
            if cur == None:
                return
            inorder(cur.left)
            nodeList.append(cur)
            inorder(cur.right)
        
        inorder(root)

        sortList = sorted(nodeList, key=lambda x : x.val)
        for i in range(len(sortList)):
            nodeList[i].val = sortList[i]

#test case
t = TreeNode()
t.val = 1
t1 = TreeNode()
t1.val = 3
t2 = TreeNode()
t2.val = 2
t.left = t1
t.right = t2

s = Solution()
print(s.isValidBST(t))
