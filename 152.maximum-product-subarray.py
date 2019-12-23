#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#
from typing import List
# @lc code=start
# Time: O(n)
# Space: O(2n)
# class Solution:
#     def maxProduct(self, nums: List[int]) -> int:
#         if not nums or len(nums) == 0:
#             return 0
#         n = len(nums)
#         max_dp = [0 for _ in range(n)]
#         min_dp = [0 for _ in range(n)]
#         max_sofar = max_dp[0] = min_dp[0] = nums[0]
#         for i in range(1, n):
#             max_dp[i] = max(max_dp[i-1] * nums[i], min_dp[i-1] * nums[i], nums[i])
#             min_dp[i] = min(max_dp[i-1] * nums[i], min_dp[i-1] * nums[i], nums[i])
#             max_sofar = max(max_sofar, max_dp[i])
#         return max_sofar
# 184/184 cases passed (80 ms)
# Your runtime beats 7.36 % of python3 submissions
# Your memory usage beats 17.24 % of python3 submissions (14.1 MB)


# 2. O(1)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # store the result that is the max we have found so far
        if not nums or len(nums) == 0:
            return 0
        n = len(nums)
        max_v = min_v = max_sofar = nums[0]
        for i in range(1, n):
            if nums[i] < 0:
                max_v, min_v = min_v, max_v
            max_v = max(nums[i], max_v * nums[i])
            min_v = min(nums[i], min_v * nums[i])
            max_sofar = max(max_sofar, max_v)
        return max_sofar
# 184/184 cases passed (44 ms)
# Your runtime beats 99.46 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (13 MB)

# @lc code=end

print(Solution().maxProduct([2,3,-2,4]))
print(Solution().maxProduct([-2,0,-1]))
print(Solution().maxProduct([-2]))
print(Solution().maxProduct([-3, -4]))
print(Solution().maxProduct([-2,3,-4]))