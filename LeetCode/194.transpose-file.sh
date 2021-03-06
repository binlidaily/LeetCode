#
# @lc app=leetcode id=194 lang=bash
#
# [194] Transpose File
#
# https://leetcode.com/problems/transpose-file/description/
#
# shell
# Medium (23.91%)
# Likes:    57
# Dislikes: 167
# Total Accepted:    12.4K
# Total Submissions: 52.1K
# Testcase Example:  'a'
#
# Given a text file file.txt, transpose its content.
# 
# You may assume that each row has the same number of columns and each field is
# separated by the ' ' character.
# 
# Example:
# 
# If file.txt has the following content:
# 
# 
# name age
# alice 21
# ryan 30
# 
# 
# Output the following:
# 
# 
# name alice ryan
# age 21 30
# 
# 
# 
# 
#

# @lc code=start
# Read from the file file.txt and print its transposed content to stdout.
awk '{
    for (i=1;i<=NF;i++){
        if (NR==1){
            res[i]=$i
        }
        else{
            res[i]=res[i]" "$i
        }
    }
}
END{
    for(j=1;j<=NF;j++){
        print res[j]
    }
}
' file.txt

# 17/17 cases passed (8 ms)
# Your runtime beats 80.27 % of bash submissions
# Your memory usage beats 100 % of bash submissions (3.5 MB)

# @lc code=end

