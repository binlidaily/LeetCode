#
# @lc app=leetcode id=44 lang=python3
#
# [44] Wildcard Matching
#

# @lc code=start
### 1. Backtracking
# Time: O()
# Space: O()
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i = 0
        j = 0
        backtrack = 0
        star = -1
        while i < len(s):
            ## first case compare ? or whether they are exactly the same
            if j < len(p) and (s[i] == p[j] or p[j] == '?'):
                i += 1
                j += 1
            ## if there is a * in p we mark current j and i    
            elif j < len(p) and p[j] == '*':
                star = j
                j += 1
                backtrack = i
            ## if current p[j] is not * we check whether prior state has *
            elif star != -1:
                j = star + 1 
                backtrack += 1
                i = backtrack
            else:
                return False
        while j < len(p) and p[j] == '*':
            j += 1
        if j == len(p):
            return True
        return False
# 1809/1809 cases passed (44 ms)
# Your runtime beats 98 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.8 MB)


### 2. DP
# Time: O()
# Space: O()
# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
#         length = len(s)
#         if len(p) - p.count('*') > length:
#             return False
#         dp = [True] + [False]*length
#         for i in p:
#             if i != '*':
#                 for n in reversed(range(length)):
#                     dp[n+1] = dp[n] and (i == s[n] or i == '?')
#             else:
#                 for n in range(1, length+1):
#                     dp[n] = dp[n-1] or dp[n]
#             dp[0] = dp[0] and i == '*'
#         return dp[-1]
# 1809/1809 cases passed (216 ms)
# Your runtime beats 81.47 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.7 MB)


### 3. 记忆化递归
# Time: O()
# Space: O()
# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
#         """
#         p[0] is literal
#             if s[0] == p[0]
#                 return match(s[1:], p[1:])
#             return False
#         p[0] is '?'
#             return match(s[1:], p[1:])
#         p[0] is '*'
#             return match(s[1:], p) or match(s, p[1:])        
#         """
#         self.memo = dict()
#         result = self.match(s, p)
#         return result
        
#     def match(self, s, p) -> bool:  
#         if len(s) == 0 and len(p) == 0:
#             return True
#         if len(p) == 0:
#             return False
#         if len(s) == 0 and p[0] != "*":
#             return False
#         if (len(p), len(s)) in self.memo:
#             return self.memo[(len(p), len(s))]
        
#         if p[0] == "?":
#             result = self.match(s[1:], p[1:])
#         elif p[0] == "*" and len(s) > 0:
#             result = self.match(s[1:], p) or self.match(s, p[1:])
#         elif p[0] == "*":
#             result = self.match(s, p[1:])
#         else:
#             if s[0] == p[0]:
#                 result = self.match(s[1:], p[1:])
#             else:
#                 result = False
        
#         self.memo[(len(p), len(s))] = result
#         return result
# 1809/1809 cases passed (1164 ms)
# Your runtime beats 15.23 % of python3 submissions
# Your memory usage beats 50 % of python3 submissions (93.2 MB)

# @lc code=end

