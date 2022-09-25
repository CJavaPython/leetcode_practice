from typing import Optional
import math
#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        leftMinVal, rightMaxVal = -math.inf, math.inf
        return self.dfs(root, leftMinVal, rightMaxVal)
        
    def dfs(self, cur: Optional[TreeNode], leftMinVal, rightMaxVal) -> bool:
        #depth first
        ## leef node
        if cur == None:
            return True
        ## validate check
        left_result = True
        right_result = True
        ## validate check
        if not (leftMinVal < cur.val < rightMaxVal):
            return False
        ## left Node validate
        if cur.left != None:
            left_result = self.dfs(cur.left, leftMinVal, cur.val)
        ## right Node validate
        if cur.right != None:
            right_result = self.dfs(cur.right, cur.val, rightMaxVal)

        return left_result and right_result
#test case
t = TreeNode()
t.val = 2
t1 = TreeNode()
t1.val = 2
t2 = TreeNode()
t2.val = 2
t.left = t1
t.right = t2

s = Solution()
print(s.isValidBST(t))
