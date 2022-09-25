# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional
from collections import deque, defaultdict
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None : return list()
        q = deque()
        q.append((root, 0))
        l = defaultdict(list)
        while q:
            tmp, level = q.popleft()
            l[level].append(tmp.val)
            level += 1
            if tmp.left!=None:
                q.append((tmp.left, level))
            if tmp.right!=None:
                q.append((tmp.right, level))
        result = []
        for key in l:
            result.append(l[key])
        return result