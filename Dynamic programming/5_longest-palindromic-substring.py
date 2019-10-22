class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:return s
        size=len(s)
        dp=[[False]*size for i in range(size)]
        maxlenth=1
        res=s[0]
        for r in range(1,size):
            for l in range(r):
                if (s[l]==s[r] and (r-l<=2 or dp[l+1][r-1])):
                    dp[l][r]=True
                    curlenth=r-l+1
                    if curlenth>maxlenth:
                        maxlenth=curlenth
                        res=s[l:r+1]
        return res
 /*
 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
 */       
