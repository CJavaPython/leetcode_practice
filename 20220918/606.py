# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        temp = root
        def dfs(node):
            string = str(node.val)
            left = 
            right = dfs(node.left())
            

        return 0

s = Solution()
s.tree2str(root = [1,2,3,4])