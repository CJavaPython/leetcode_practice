from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None : return False
        targetSum -= root.val
        result = False
        left_result = False
        right_result = False
        if root.left == None and root.right == None:
            result = (targetSum == 0)
        else:
            left_result = self.hasPathSum(root.left, targetSum)
            right_result = self.hasPathSum(root.right, targetSum)
        result = result or left_result or right_result
        return result
s = Solution()
print(s.hasPathSum(root = TreeNode(val = 1, left = TreeNode(val=2)), targetSum = 0))
