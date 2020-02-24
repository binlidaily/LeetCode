#
# @lc app=leetcode id=617 lang=python3
#
# [617] Merge Two Binary Trees
#
import collections
# @lc code=start
# Time: O(logn)
# Space: O(logn)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 and t2:
            root = TreeNode(t1.val + t2.val)
            root.left = self.mergeTrees(t1.left, t2.left)
            root.right = self.mergeTrees(t1.right, t2.right)
            return root
        else:
            return t1 or t2

# 183/183 cases passed (92 ms)
# Your runtime beats 53.67 % of python3 submissions
# Your memory usage beats 82.86 % of python3 submissions (13.6 MB)
# @lc code=end

