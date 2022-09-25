# invert binary tree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
from collections import deque
# can solve with level order
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None : return list()
        q = deque()
        result = TreeNode()
        q.append((root, result))
        while q:
            tmp, traverse = q.popleft()
            if tmp.right!=None:
                q.append((tmp.right, traverse.right))
            if tmp.left!=None:
                q.append((tmp.left, traverse.left))
        return result


s = Solution()
print(s.invertTree(root = [4,2,7,1,3,6,9]))