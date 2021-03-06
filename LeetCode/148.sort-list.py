#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#

# @lc code=start
# Definition for singly-linked list.
# 1. merge
# Top-down (recursion)
# Time complexity: O(nlogn)
# Space complexity: O(logn)
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def sortList(self, head: ListNode) -> ListNode:
#         if not head or not head.next:
#             return head
#         slow, fast = head, head.next
#         while fast and fast.next:
#             fast = fast.next.next
#             slow = slow.next
#         # find mid node
#         mid = slow.next
#         slow.next = None
#         return self.merge(self.sortList(head),self.sortList(mid))

#     def merge(self, left, right):
#         dummy = ListNode(0)
#         # where we need to append the non None list
#         tail = dummy
#         while left and right:
#             if left.val > right.val:
#                 left, right = right, left
#             tail.next = left
#             left = left.next
#             tail = tail.next
#         if left:
#             tail.next = left
#         if right:
#             tail.next = right
#         return dummy.next

# 16/16 cases passed (232 ms)
# Your runtime beats 61.56 % of python3 submissions
# Your memory usage beats 15.38 % of python3 submissions (21.9 MB)

# Botton up
# Time: O(n)
# Space: O(1)

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        size = 1
        cur = head
        cur = cur.next
        while cur:
            size += 1
            cur = cur.next
        
        dummy = ListNode(0)
        dummy.next = head
        i = 1
        while i < size:
            cur = dummy.next
            tail = dummy
            while cur:
                l = cur
                r = self.split(l, i)
                cur = self.split(r, i)
                first, second = self.merge(l, r)
                tail.next = first
                tail = second
            i = i << 1
        return dummy.next

    def split(self, head, n):
        # Splits the list into two parts, first n element and the rest.
        # Returns the head of the rest.
        while n > 1 and head:
            head = head.next
            n -= 1
        rest = head.next if head else None
        if head:
            head.next = None
        return rest

    def merge(self, left, right):
        dummy = ListNode(0)
        tail = dummy
        while left and right:
            if left.val > right.val:
                left, right = right, left
            tail.next = left
            left = left.next
            tail = tail.next
        tail.next = left if left else right
        while tail.next:
            tail = tail.next
        return dummy.next, tail

# 16/16 cases passed (252 ms)
# Your runtime beats 36.81 % of python3 submissions
# Your memory usage beats 15.38 % of python3 submissions (21.8 MB)
# @lc code=end


def cout(node):
    while node:
        print(node.val)
        node = node.next
a = ListNode(4)
b = ListNode(2)
c = ListNode(1)
d = ListNode(3)
a.next = b
b.next = c
c.next = d
d = Solution().sortList(a)
cout(d)